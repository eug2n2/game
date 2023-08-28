#!/usr/bin/env python
# coding: utf-8

# In[92]:



class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.tree = None
        self.temp = None
        self.prev=None
        self.direction = None

    # 삽입
    def insert(self, item):
        node=Node(item)
        if not self.tree: self.tree=node
        else:
            temp = self.tree
            prev = None
            while True:
                prev=temp
                if item < prev.data:
                    temp = temp.left
                    if not temp:
                        prev.left = node
                        return
                elif item>prev.data:
                    temp = temp.right
                    if not temp:
                        prev.right = node
                        return
                else: return


    def height(self,root):  #높이구하는 함수 
        if not root : return 0
        if root.left:
            l_height =1+self.height(root.left)
        else: l_height =0
            
        if root.right:
            r_height = 1+self.height(root.right)
        else:r_height = 0
            
        if l_height >= r_height: return r_height
        else:return l_height
        
    def delete_node(self, node, item): #node:삭제할 노드 
        
        if node is None: return None
        if node.data > item:
            node.left= self.delete_node(node.left,item)
            return node
        elif node.data<item:
            node.right = self.delete_node(node.right,item)
            return node
        else:                    #삭제 노드발견
            if node.left is None: #오른쪽 자식 노드만 존재
                return node.right
            elif node.right is None: #왼쪽 자식 노드만 존재
                return node.left
            elif node.left is None and node.right is None: #단말노드
                return None
            else: #자식이 2개인 노드 삭제  : 더 높이 작은거 선택 
                left_max = self.find_max(node.left) #왼쪽의 최댓값
                right_min =self.find_min(node.right) #오른쪽의 최솟값
                if self.height(node.left) >= self.height(node.right): 
                    node.data = left_max.data 
                    node.left = self.delete_node(node.left, left_max.data)
                    return node
                else:
                    node.data =right_min.data 
                    node.right = self.delete_node(node.right, right_min.data)
                    return node
                

    def find_delete(self,item):
        self.tree = self.delete_node(self.tree, item)
        
    def find_max(self,root):
        if not root: return None
        node =root
        while node.right:
            node = node.right
        return node
    
    def find_min(self,root):
        if not root: return None
        node =root
        while node.left:
            node = node.left
        return node
    
    def postorder(self,ptr):
        if ptr:
            self.postorder(ptr.left)
            self.postorder(ptr.right)
            print(ptr.data,end=' ')

bst=BST()

for i in [30,20,10,40,60,50,25]:
    bst.insert(i) 
    bst.postorder(bst.tree)
    print() 
print() 

for i in [30,25,40,50,20,60]:
    bst.find_delete(i) #삭제
    bst.postorder(bst.tree) 
    print()

