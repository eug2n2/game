#!/usr/bin/env python
# coding: utf-8

# In[40]:


import math
class Element:
    def __init__(self, v, w, _from):
        # 가중치를 키로 사용한다
        self.w=w 
        self.v=v #트리 밖 정점 
        self._from=_from #자라나고 있는 트리 정점 집합의 정점

class MinHeap:
    MAX_ELEMENTS=200
    def __init__(self):
        self.arr=[None for i in range(self.MAX_ELEMENTS)]
        self.heapsize=0
        self.pos=[None for i in range(self.MAX_ELEMENTS)] #트리 밖 정점의 arr 내 인덱스를 저장

    def is_empty(self):
        if self.heapsize==0:
            return True
        return False

    def is_full(self):
        if self.heapsize>=self.MAX_ELEMENTS:
            return True
        return False

    def parent(self, idx):
        return idx >> 1

    def left(self, idx):
        return idx << 1

    def right(self, idx):
        return (idx << 1) + 1

    def push(self, item):
        if self.is_full():
            raise IndexError("the heap is full")

        self.heapsize+=1
        cur_idx=self.heapsize

        while cur_idx!=1 and item.w < self.arr[self.parent(cur_idx)].w: 
            self.arr[cur_idx]=self.arr[self.parent(cur_idx)]
            # pos의 인덱스는 정점, arr는 weight를 키로 만든 최소 힙
            self.pos[self.arr[cur_idx].v]=cur_idx

            cur_idx=self.parent(cur_idx)

        self.arr[cur_idx]=item
        self.pos[item.v]=cur_idx

    def pop(self): # cycle생성시 제거 
        if self.is_empty():
            return None

        rem_elem=self.arr[1]

        temp=self.arr[self.heapsize]
        self.heapsize-=1

        cur_idx=1
        child=self.left(cur_idx)

        while child <= self.heapsize:
            if child < self.heapsize and                 self.arr[self.left(cur_idx)].w > self.arr[self.right(cur_idx)].w:
                child=self.right(cur_idx)
            
            if temp.w <= self.arr[child].w:
                break

            self.arr[cur_idx]=self.arr[child]
            self.pos[self.arr[cur_idx].v]=cur_idx

            cur_idx=child
            child=self.left(cur_idx)
        
        self.arr[cur_idx]=temp
        self.pos[temp.v]=cur_idx

        return rem_elem

    def decrease_weight(self, new_elem): # 더 가중치가 작은 edge를 발견했을 때 더 작은 가중치로 업데이트
        cur=self.pos[new_elem.v] # 업데이트될 정점의 현재 인덱스
        
        #cur가 루트가 아니고 업데이트될 원소의 weight< 부모 원소의 weight라면 부모 원소를 아래로 내리고 cur가 루트 쪽으로 올라감
        while cur!= 1 and new_elem.w < self.arr[self.parent(cur)].w: 
            self.arr[cur]=self.arr[self.parent(cur)] # 부모 원소를 한 칸 아래로 내림
            self.pos[self.arr[cur].v]=cur    

            cur=self.parent(cur)

        self.arr[cur]=new_elem
        self.pos[new_elem.v]=cur

class Edge:
    def __init__(self, u, v, w):
        self.u=u
        self.v=v
        self.w=w

class Graph:
    def __init__(self, vertex_num):
        self.adj_list=[[] for _ in range(vertex_num+1)]
        self.edge_list=[]
        self.total = 0
        self.vertex_num=vertex_num
    
    def add_edge(self, u, v, w):
        # (정점, 에지의 가중치)를 인접 리스트에 추가
        self.adj_list[u].append((v, w))
        self.adj_list[v].append((u, w))
        self.edge_list.append(Edge(u, v, w))

    def MST_prim(self):
        mst=Graph(self.vertex_num)

        w_list=[math.inf for _ in range(self.vertex_num+1)] #각 정점마다 가중치를 저장

        self.TV = set() #TV = {}: MST 정점의 집합으로 중복되지 않게 하기위해  ;tree vertex
        h=MinHeap()

        for i in range(1, self.vertex_num+1):
            h.push(Element(i, math.inf, None))  #Element(v, w, _from)

        w_list[0] = input("시작노드를 입력하세요: ")
        
        while not h.is_empty():
            elem_v=h.pop()
            v=elem_v.v 
            w=elem_v.w 
            _from=elem_v._from
            
            self.TV.add(v)
            if _from != None:
                mst.add_edge(v, _from, w)
                self.total += w
            adj_v=self.adj_list[v]
            for u, w_u_v in adj_v:  #w_u_v: weight(u, v)
                if u not in self.TV and w_u_v < w_list[u]:
                    w_list[u]=w_u_v
                    h.decrease_weight(Element(u, w_u_v, v)) 

        return mst

    def print_edges(self):
        for edge in self.edge_list:
            print("({}, {}, {})".format(edge.u, edge.v, edge.w))

            
if __name__=="__main__":
    g=Graph(7)

    g.add_edge(1, 2, 5)
    g.add_edge(1, 4, 3)
    g.add_edge(2, 5, 10)
    g.add_edge(4, 5, 6)
    g.add_edge(4, 6, 7)
    g.add_edge(5, 3, 8)
    g.add_edge(5, 7, 13)
    g.add_edge(6, 7, 15)
    g.add_edge(7, 3, 11)
    mst = g.MST_prim()
    
    print('spanning tree vertices = ', g.TV)
    print("spanning tree edges: ")
    mst.print_edges()
    
    print('cost total = ', g.total)

