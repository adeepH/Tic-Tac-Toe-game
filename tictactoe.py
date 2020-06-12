def display(a):
    print(a[7]+'|'+a[8]+'|'+a[9])
    print(a[4]+'|'+a[5]+'|'+a[6])
    print(a[1]+'|'+a[2]+'|'+a[3])
def info():
    n =  int(input("Which player wants to go first? "))
    if n==1:
        m=2
        print('Player 1 is X and 2 is O')
    elif n==2:
        m=1
        print('Player 1 is O and 2 is X')
    else:
        print("Invalid player number")
    return n
def marker(a,pos,mark,count):
    if a[pos]=='_':
        a[pos]=mark
        count=count+1
        return count
    else:
        return 100
def wincheck(a,mark):
    if((a[1]==a[2]==a[3]==mark)or
    (a[4]==a[5]==a[6]==mark)or
    (a[7]==a[8]==a[9]==mark)or
    (a[1]==a[5]==a[9]==mark)or3
    (a[7]==a[5]==a[3]==mark)or
    (a[1]==a[4]==a[7]==mark)or
    (a[2]==a[5]==a[8]==mark)or
    (a[3]==a[6]==a[9]==mark)):
        return 0
    else:
        return 1
def drawcheck(count):
    if count==9:
        return 0
    else:
        return 1
print('Welcome to tictactoe')
a = ['_']*10
mark='X'
count=0
n=info()
y=input('Press 1 to start ')
while y:
    print('Player '+ str(n) +' its your turn')
    pos=int(input('Enter the position you want to place '+ mark+ ' '))
    if pos<10:
        count=marker(a,pos,mark,count)
        if count!=100:
            display(a)
            y=wincheck(a,mark)
            if y==0:
                print('Player '+ str(n)+ ' is the winner!!')
                break
            y=drawcheck(count)
            if y==0:
                print("It is a draw!!")
                break
            if n==1:
                n=2
            elif n==2:
                n=1
            if mark=='X':
                mark='O'
            elif mark=='O':
                mark='X'
        else:
            print("Position is already taken!!")
    else:
        print('Invalid position!!')
    
    
    
    
    
    
    
    
    

