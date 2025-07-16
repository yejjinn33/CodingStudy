score = int(input())

for i in range(100-score+1) :
    if score >= 90 :
        print("A", end=' ')
    elif score >= 80 :
        print("B", end=' ')
    elif score >= 70 :
        print("C", end=' ')
    elif score >= 60 :
        print("D", end=' ')
    else :
        print("E", end=' ')
    score+=1