#!/usr/bin/env python
# coding: utf-8

# In[9]:


import random
class CircularDoublyLinkedList:
    class Node:
        def __init__(self, v, n=None, p=None):
            self.value = v  # 데이터
            self.next = n  # 다음 노드 
            self.prev = p  # 이전 노드 
            
    def __init__(self):
        self.head = None  # 첫 생성시 내부에는 노드가 없음
        self.tail = None
        
    def insertNodeAfter(self, v):  # tail로 삽입. v : data
        # 없을 경우
        if self.tail is None:
            self.tail = self.Node(v)
            self.head = self.tail  # 같은 노드를 가리킴
        else: # 기존 tail.next를 새 노드로 지정(새 노드의 prev는 tail, next는 head로 지정)
            self.tail.next = self.Node(v, p=self.tail, n=self.head)
            self.tail = self.tail.next  #tail을 새 노드로 변경
            self.head.prev = self.tail #head.prev를 새 tail로 업데이트
   
    def printNodeBefore(self): #출력함수 
        # 데이터가 없을 때
        if self.head is None:
            print("저장된 데이터가 없음")
            return
        else:
            print("[", end = ' ')
            link = self.head  # 처음은 head를 지정. 이후 next를 지정
            while link:
                print(link.value, end=' ')
                if link == self.tail: 
                    break
                link = link.next  # link를 현 위치 노드의 next로 변경
            print("]",end='')

    def searchNodeBefore(self, v): # head로 조회(탐색)
        # 데이터가 없을 때
        if self.head is None:
            print("저장된 데이터가 없음")
            return
        else:
            link = self.head  # 처음은 head를 지정. 이후부터는 현 노드의 next를 지정
            index = 0  
            while link: 
                if v == link.value:
                    return index  
                else:
                    link = link.next  # link를 현 위치 노드의 next로 변경
                    index += 1  # 위치값 1 증가
                    if link == self.tail: #link가 tail일 경우 멈추기
                        break
  
    def nextdice1(self, n): #1번 player 전진 
        i=0
        link = self.head
        while link:
            if link.value==1:
                link.value=0
                break
            else:
                link=link.next
        while i<n:
            link=link.next
            i+=1
        link.value=1
    def nextdice2(self, n): # 2번 player전진
        i=0
        link=self.head
        while link:
            if link.value==2:
                link.value=0
                break
            else:
                link=link.next
        while i<n:
            link=link.next
            i+=1
        link.value=2        
    def prevdice1(self, n): #1번 player 후진
        i=0
        link=self.head
        while link:
            if link.value==1:
                link.value=0
                break
            else:
                link=link.next
        while i<n:
            link=link.prev
            i+=1
        link.value=1        
    def prevdice2(self, n): #2번 player후진
        i=0
        link=self.head
        while link:
            if link.value==2:
                link.value=0
                break
            else:
                link=link.next
        while i<n:
            link=link.prev
            i+=1
        link.value=2 
    def changeidx(self): #말 위치변경
        curr1=self.searchNodeBefore(1) 
        curr2=self.searchNodeBefore(2)
        link=self.head
        link.value=0
        for i in range(curr2):
            link=link.next
        link.value=1
        link=self.head
        for i in range(curr1):
            link=link.next
        link.value=2
    def changeidx(self):
        curr=self.searchNodeBefore(2)
        link=self.head
        i=0
        while link:
            if link.value==1:
                link.value=2
                break
            else:
                link=link.next
        link=self.head
        while i<curr:
            link=link.next
            i+=1
        link.value=1

lst = CircularDoublyLinkedList() #초기위치 설정
for item in [1,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0]:
    lst.insertNodeAfter(item)
print( "Game start!")
print("player 초기 위치")
lst.printNodeBefore()
print("")
idx=1  # player 1의 방향
idx2=1 # player 2의 방향
while True:
    first1 = random.randint(1,6) #player1 차례
    second1=random.randint(1,6)
    if first1==6 and second1 ==6:
        idx=idx*(-1)
        idx2=idx2*(-1)
        print("1 (6,6) 이동방향 전환")
    elif first1 == 5 and second1 ==5:
        print("1 (5,5) 말의 위치 교환")
        lst.changeidx()
        lst.printNodeBefore()
        print("")
    elif idx==1:# 전진
        if first1 ==1 and second1==1:
            print("1 (1,1) 뒤로 한 칸 ")
            b=lst.searchNodeBefore(2)
            lst.prevdice1(1)
            lst.printNodeBefore()
            print("")
            a=lst.searchNodeBefore(1)
            if(b == a):
                print("1 player won!")
                break
        else: 
            b=lst.searchNodeBefore(2)
            lst.nextdice1(first1+second1)
            print("1 (",first1,",",second1,")칸 전진")
            lst.printNodeBefore()
            print('') 
            a=lst.searchNodeBefore(1)
            if(b == a):
                print("1 player won!")
                break
    else: # 방향이 뒤인경우 
        if first1 ==1 and second1==1:
            print("1 (1,1) 뒤로 한 칸 ")
            b=lst.searchNodeBefore(2)
            lst.nextdice1(1)
            lst.printNodeBefore()
            print("")
            a=lst.searchNodeBefore(1)
            if(b==a):
                print("1 player won!")
                break
        else:
            b=lst.searchNodeBefore(2)
            lst.prevdice1(first1+second1)
            print("1(",first1,",",second1,")칸 전진")
            lst.printNodeBefore()
            print('')
            a=lst.searchNodeBefore(1)
            if(b==a):
                print("1 player won!")
                break
    
    first2=random.randint(1,6) #2번 player 주사위 던짐
    second2=random.randint(1,6)
    if first2==6 and second2 ==6:
        idx=idx*(-1)
        idx2=idx2*(-1)
        print("2 (6,6) 이동방향 전환")
    elif first2 == 5 and second2 ==5:
        print("2 (5,5) 말의 위치 교환")
        lst.changeidx()
        lst.printNodeBefore()
        print("")
    elif idx2==1:
        if first2 ==1 and second2==1:
            print("2 (1,1) 뒤로 한 칸 ")
            a=lst.searchNodeBefore(1)
            lst.prevdice2(1)
            lst.printNodeBefore()
            print("")
            b=lst.searchNodeBefore(2)
            if(a== b):
                print("2 player won!")
                break
        else: 
            a=lst.searchNodeBefore(1)
            lst.nextdice2(first2+second2)
            print("2(",first2,",",second2,")칸 전진")
            lst.printNodeBefore()
            print('')
            b=lst.searchNodeBefore(2)
            if(a== b):
                print("2 player won!")
                break
    else:
        if first2 ==1 and second2==1:
            print("2 (1,1) 뒤로 한 칸 ")
            a=lst.searchNodeBefore(1)
            lst.nextdice2(1)
            lst.printNodeBefore()
            print("")
            b=lst.searchNodeBefore(2)
            if(a == b):
                print("2 player won!")
                break
        else:
            a=lst.searchNodeBefore(1)
            lst.prevdice2(first2+second2)
            print("2(",first2,",",second2,")칸 전진")
            lst.printNodeBefore()
            print('')
            b=lst.searchNodeBefore(2)
            if(a == b):
                print("2 player won!")
                break
    

