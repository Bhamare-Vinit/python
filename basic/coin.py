import random
toss=int(input("enter the number of toss :"))
head=0
tail=0
total=0
for i in range(toss):
    side=random.random()
    if side<0.5:
        tail+=1
        total+=1
    else:
        head+=1
        total+=1
percentage_head=(head*100)/total
percentage_tail=(tail*100)/total
print(f"Percentage of head is {percentage_head} \nPercentage of tail is {percentage_tail}")


