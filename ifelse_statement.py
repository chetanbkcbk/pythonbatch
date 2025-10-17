#if-else statement:->used when we have exactly 2 possible outcomes

age=int(input('enter age'))

print('above if')#1
if age>18:
    print("adult")#2
if age>60:
    print("senior citizen")
#1)dont have any executable line of code in btw if and else block,if-else shud be together
else :
    print("Child")
#2)only 1 else block shud be there and it shud be at the last
#3)when we have multiple if blocks and 1 else block,,the last if-else will be chosen as pair
#4)either if or else will be executed
    
