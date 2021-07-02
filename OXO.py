from random import choice
x=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
q=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
z=[]
a=int(input('Enter - '))
x[a]='X'
if a==0:z = choice([1,3])
elif a==2:z = choice([1,5])
elif a==6:z = choice([7,3])
elif a==8:z = choice([5,7])
elif a==1 or a==3 or a==5 or a==7:z = 4
elif a==4:z=choice([0,2,6,8])
x[z]='O'
print(x[:3])
print(x[3:6])
print(x[6:])
for i in range(3):
    a=int(input('Enter - '))
    x[a]='X'
    z=[]
    for i in range(len(x)):
        if x[i]=='O':z.append(i)    
    u=list(x)
    for k in range(len(q)):
        if   (q[k][0] in z) and (q[k][1] in z):
            if q[k][2] not in z:
                if x[q[k][2]]==' ':x[q[k][2]]='O'
                break
            else:pass
        elif (q[k][0] in z) and (q[k][2] in z):
            if q[k][1] not in z:
                if x[q[k][1]]==' ':x[q[k][1]]='O'
                break
            else:pass
        elif (q[k][1] in z) and (q[k][2] in z):
            if q[k][0] not in z:
                if x[q[k][0]]==' ':x[q[k][0]]='O'
                break
            else:pass
    if u==x:
        z=[]
        for i in range(len(x)):
            if x[i]=='X':z.append(i)
        for k in range(len(q)):
            if   (q[k][0] in z) and (q[k][1] in z):
                if q[k][2] not in z:
                    x[q[k][2]]='O'
                    break
                else:pass
            elif (q[k][0] in z) and (q[k][2] in z):
                if q[k][1] not in z:
                    x[q[k][1]]='O'
                    break
                else:pass
            elif (q[k][1] in z) and (q[k][2] in z):
                if q[k][0] not in z:
                    x[q[k][0]]='O'
                    break
                else:pass

    if u==x:
        z=[]
        for i in range(len(x)):
            if x[i]==' ':z.append(i)
        x[choice(z)]='O'
    print(x[:3])
    print(x[3:6])
    print(x[6:])
    if x[:3]==['X','X','X'] or x[3:6]==['X','X','X'] or x[6:]==['X','X','X'] or (x[0]=='X' and x[3]=='X' and x[6]=='X') or (x[1]=='X' and x[4]=='X' and x[7]=='X') or (x[2]=='X' and x[5]=='X' and x[8]=='X') or (x[0]=='X' and x[4]=='X' and x[8]=='X') or (x[2]=='X' and x[4]=='X' and x[6]=='X'):
        print('P1 WON!!!')
        exit()
    if x[:3]==['O','O','O'] or x[3:6]==['O','O','O'] or x[6:]==['O','O','O'] or (x[0]=='O' and x[3]=='O' and x[6]=='O') or (x[1]=='O' and x[4]=='O' and x[7]=='O') or (x[2]=='O' and x[5]=='O' and x[8]=='O') or (x[0]=='O' and x[4]=='O' and x[8]=='O') or (x[2]=='O' and x[4]=='O' and x[6]=='O'):
        print('P2 WON!!!')
        exit()
a=int(input('Enter - '))
x[a]='X'
print(x[:3])
print(x[3:6])
print(x[6:])
if x[:3]==['X','X','X'] or x[3:6]==['X','X','X'] or x[6:]==['X','X','X'] or (x[0]=='X' and x[3]=='X' and x[6]=='X') or (x[1]=='X' and x[4]=='X' and x[7]=='X') or (x[2]=='X' and x[5]=='X' and x[8]=='X') or (x[0]=='X' and x[4]=='X' and x[8]=='X') or (x[2]=='X' and x[4]=='X' and x[6]=='X'):
    print('P1 WON!!!')
elif x[:3]==['O','O','O'] or x[3:6]==['O','O','O'] or x[6:]==['O','O','O'] or (x[0]=='O' and x[3]=='O' and x[6]=='O') or (x[1]=='O' and x[4]=='O' and x[7]=='O') or (x[2]=='O' and x[5]=='O' and x[8]=='O') or (x[0]=='O' and x[4]=='O' and x[8]=='O') or (x[2]=='O' and x[4]=='O' and x[6]=='O'):
    print('P2 WON!!!')
else:print('DRAW!!!')
