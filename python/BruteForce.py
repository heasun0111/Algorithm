import sys

student1=[1,2,3,4,5]
student2=[2,1,2,3,2,4,2,5]
student3=[3,3,1,1,2,2,4,4,5,5]

cnt1=0
cnt2=0
cnt3=0

ans=[]

def solution(answers):
    answer=[]
    global cnt1
    global cnt2
    global cnt3

    for i in range(len(answers)):
        num1=i%5
        num2=i%8
        num3=i%10
        if answers[i]==student1[num1]:
            cnt1=cnt1+1
        if answers[i]==student2[num2]:
            cnt2=cnt2+1
        if answers[i] == student3[num3]:
            cnt3=cnt3+1

    ans=[cnt1, cnt2, cnt3]

    for student, score in enumerate(ans):
        if score == max(ans):
            answer.append(student+1)

    return answer
