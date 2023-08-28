#!/usr/bin/env python
# coding: utf-8


# In[1]:


#볼링게임
f_total=i=0 #0프레임부터, 총합의 초기값은 0
score=[]
while True: #점수 입력
    first=int(input('첫번째 점수 입력 : '))
    second=int(input('두번째 점수 입력 : '))
    
    if i<=9 and first==10: #0~9프레임에서 스트라이크
        result='STRIKE'
        next_first=int(input('다음 세트 첫번째 점수 입력 : '))
        next_second=int(input('다음 세트 두번째 점수 입력 : '))
        score=first+second+next_first+next_second
        f_total += first+second+next_first+next_second
        
        if i<8 and next_first==10:#더블 스트라이크
            next_next_first=int(input('첫번째 점수 입력 : '))
            next_next_second=int(input('두번째 점수 입력 : '))
            score +=next_next_first+next_next_second
            f_total += next_next_first+next_next_second
            i+=1  
        elif i<8 and (next_first+next_second)==10 : #스트라이크 후 스페어
            result='SPARE'
            next_next_first=int(input('보류! 다다음세트 첫번째 점수 입력 : '))
            score +=next_first+next_second+ next_next_first
            f_total += next_first+next_second+next_next_first   
            i+=1
        elif i<8 and (next_first+next_second)!=10 : #스트라이크 후 일반 
            score=first+second+2*(next_first+next_second)
            f_total += (next_first+next_second)
        else: #스트라이크 후 보너스
            print('결과 : ',result,'현재점수:',score, '총점수 : ',f_total)
            break
           
    elif i<=9 and (first+second)==10 : #스페어
        result='SPARE'
        next_first=int(input('보류! 다음 세트 첫번째 점수 입력 : '))
        next_second=int(input('보류! 다음 세트 두번째 점수 입력 : '))
        
        score= first+second+ next_first
        f_total += first+second+ next_first
        if i!=9 and (next_first+next_second)==10: #스페어 후 스페어
            next_next_first=int(input('보류! 다다음세트 첫번째 점수 입력 : '))
            score +=next_first+next_second+ next_next_first
            f_total += next_first+next_second+next_next_first
            i+=1
        elif i!=9 and next_first==10: #스페어 후 스트라이크
            next_next_first=int(input('첫번째 점수 입력 : '))
            next_next_second=int(input('두번째 점수 입력 : '))
            score += next_next_first+next_next_second
            f_total += next_next_first+next_next_second
            i+=1
           
    elif i<=9 and (first+second)!=10: #스트라이크, 스페어 아무것도 아님 
        score = first+second
        f_total+=first+second
        result= "NONE"
        
    else: # 보너스가 없다면 9프레임 후 종료 
        print('결과 : ',result,'현재점수:',score, '총점수 : ',f_total)
        break
    i+=1
    print('결과 : ',result,'현재점수:',score, '누적점수 : ',f_total)






