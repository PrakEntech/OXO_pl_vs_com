from tkinter import *
import tkinter.font as font
from random import choice,randint
open('turn.bin','w+').write('0')

root = Tk()
root.attributes("-fullscreen", False)
root.title('OXO (PL VS COM)')
root.configure(bg='White')
root.iconbitmap(None)
root.geometry("325x400")
root.resizable(height = 0, width = 0)
myFont = font.Font(size=40)
myFont2 = font.Font(size=20)
def mainFunc(m):
    q=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    data=open('turn.bin','r').read()
    open('turn.bin','w+').write(str(int(data)+1))
    data=open('turn.bin','r').read()
    if int(data)<1:
        x=[]
        l[m]['text']='X'
        for i in range(9):x.append(l[i]['text'])
    elif int(data)<4 and int(data)>=1:
        x=[]
        l[m]['text']='X'
        for i in range(9):x.append(l[i]['text'])
        z=[]
        for i in range(len(x)):
            if x[i]=='O':z.append(i)    
        u=list(x)
        for k in range(len(q)):
            if   (q[k][0] in z) and (q[k][1] in z):
                if q[k][2] not in z:
                    if x[q[k][2]]=='':
                        l[q[k][2]]['text']='O'
                        x[q[k][2]]='O'
                    break
                else:pass
            elif (q[k][0] in z) and (q[k][2] in z):
                if q[k][1] not in z:
                    if x[q[k][1]]=='':
                        l[q[k][1]]['text']='O'
                        x[q[k][1]]='O'
                    break
                else:pass
            elif (q[k][1] in z) and (q[k][2] in z):
                if q[k][0] not in z:
                    if x[q[k][0]]=='':
                        l[q[k][0]]['text']='O'
                        x[q[k][0]]='O'
                    break
                else:pass

        if u==x:
            z=[]
            for i in range(len(x)):
                if x[i]=='X':z.append(i)
            for k in range(len(q)):
                if   (q[k][0] in z) and (q[k][1] in z):
                    if q[k][2] not in z:
                        if x[q[k][2]]=='':
                            l[q[k][2]]['text']='O'
                            x[q[k][2]]='O'
                            break
                    else:pass
                elif (q[k][0] in z) and (q[k][2] in z):
                    if q[k][1] not in z:
                        if x[q[k][1]]=='':
                            l[q[k][1]]['text']='O'
                            x[q[k][1]]='O'
                            break
                    else:pass
                elif (q[k][1] in z) and (q[k][2] in z):
                    if q[k][0] not in z:
                        if x[q[k][0]]=='':
                            l[q[k][0]]['text']='O'
                            x[q[k][0]]='O'
                            break
                        break
                    else:pass
        if u==x:
            z=[]
            for i in range(9):
                if l[i]['text']=='':z.append(i)
            p=choice(z)
            x[p]='O'
            l[p]['text']='O'
    else:
        l[m]['text']='X'
        x=[]
        for i in range(9):x.append(l[i]['text'])
        
        for i in range(9):
            if x[i]=='':
                x[i]='O'
                l[i]['text']='O'
        if x[:3]==['X','X','X'] or x[3:6]==['X','X','X'] or x[6:]==['X','X','X'] or (x[0]=='X' and x[3]=='X' and x[6]=='X') or (x[1]=='X' and x[4]=='X' and x[7]=='X') or (x[2]=='X' and x[5]=='X' and x[8]=='X') or (x[0]=='X' and x[4]=='X' and x[8]=='X') or (x[2]=='X' and x[4]=='X' and x[6]=='X'):
            label['text']='P1 WON!!!'
            for i in range(9):l[i].configure(state=DISABLED)
            return 0
        elif x[:3]==['O','O','O'] or x[3:6]==['O','O','O'] or x[6:]==['O','O','O'] or (x[0]=='O' and x[3]=='O' and x[6]=='O') or (x[1]=='O' and x[4]=='O' and x[7]=='O') or (x[2]=='O' and x[5]=='O' and x[8]=='O') or (x[0]=='O' and x[4]=='O' and x[8]=='O') or (x[2]=='O' and x[4]=='O' and x[6]=='O'):
            label['text']='P2 WON!!!'
            for i in range(9):l[i].configure(state=DISABLED)
            return 0
        elif '' not in x:
            label['text']='DRAW!!!'
            for i in range(9):l[i].configure(state=DISABLED)
            return 0
    if x[:3]==['X','X','X'] or x[3:6]==['X','X','X'] or x[6:]==['X','X','X'] or (x[0]=='X' and x[3]=='X' and x[6]=='X') or (x[1]=='X' and x[4]=='X' and x[7]=='X') or (x[2]=='X' and x[5]=='X' and x[8]=='X') or (x[0]=='X' and x[4]=='X' and x[8]=='X') or (x[2]=='X' and x[4]=='X' and x[6]=='X'):
            label['text']='P1 WON!!!'
            for i in range(9):l[i].configure(state=DISABLED)
            return 0
    elif x[:3]==['O','O','O'] or x[3:6]==['O','O','O'] or x[6:]==['O','O','O'] or (x[0]=='O' and x[3]=='O' and x[6]=='O') or (x[1]=='O' and x[4]=='O' and x[7]=='O') or (x[2]=='O' and x[5]=='O' and x[8]=='O') or (x[0]=='O' and x[4]=='O' and x[8]=='O') or (x[2]=='O' and x[4]=='O' and x[6]=='O'):
            label['text']='P2 WON!!!'
            for i in range(9):l[i].configure(state=DISABLED)
            return 0
    for i in range(9):
        if l[i]['text']!='':l[i].configure(state=DISABLED)

def b_0():mainFunc(0)
def b_1():mainFunc(1)
def b_2():mainFunc(2)
def b_3():mainFunc(3)
def b_4():mainFunc(4)
def b_5():mainFunc(5)
def b_6():mainFunc(6)
def b_7():mainFunc(7)
def b_8():mainFunc(8)

def resetNow():
    for i in range(9):l[i].configure(state=NORMAL,text='')
    label['text']=''
    i=randint(0,8)
    l[i]['text']='O'
    l[i].configure(state=DISABLED)
    open('turn.bin','w+').write('0')

l=[None,None,None,None,None,None,None,None,None]

#Button
label = Label(root,fg='Red',bg='White',text='',borderwidth=1,font=myFont2)
label.place(x=0,y=356)
reset = Button(root,fg='Orange',bg='White',text='Reset',borderwidth=0,activebackground='Orange',activeforeground='White',command=resetNow,font=myFont2)
reset.place(x=231,y=349)
l[0] = Button(root,fg='Orange',bg='Black',text='',borderwidth=1,activebackground='Orange',activeforeground='White',command=b_0,font=myFont)
l[0].place(x=0,y=0,width=106, height=114)
l[1] = Button(root,fg='Orange',bg='Black',text='',borderwidth=1,activebackground='Orange',activeforeground='White',command=b_1,font=myFont)
l[1].place(x=110,y=0,width=106, height=114)
l[2] = Button(root,fg='Orange',bg='Black',text='',borderwidth=1,activebackground='Orange',activeforeground='White',command=b_2,font=myFont)
l[2].place(x=220,y=0,width=106, height=114)

l[3] = Button(root,fg='Orange',bg='Black',text='',borderwidth=1,activebackground='Orange',activeforeground='White',command=b_3,font=myFont)
l[3].place(x=0,y=117,width=106, height=114)
l[4] = Button(root,fg='Orange',bg='Black',text='',borderwidth=1,activebackground='Orange',activeforeground='White',command=b_4,font=myFont)
l[4].place(x=110,y=117,width=106, height=114)
l[5] = Button(root,fg='Orange',bg='Black',text='',borderwidth=1,activebackground='Orange',activeforeground='White',command=b_5,font=myFont)
l[5].place(x=220,y=117,width=106, height=114)

l[6] = Button(root,fg='Orange',bg='Black',text='',borderwidth=1,activebackground='Orange',activeforeground='White',command=b_6,font=myFont)
l[6].place(x=0,y=234,width=106, height=114)
l[7] = Button(root,fg='Orange',bg='Black',text='',borderwidth=1,activebackground='Orange',activeforeground='White',command=b_7,font=myFont)
l[7].place(x=110,y=234,width=106, height=114)
l[8] = Button(root,fg='Orange',bg='Black',text='',borderwidth=1,activebackground='Orange',activeforeground='White',command=b_8,font=myFont)
l[8].place(x=220,y=234,width=106, height=114)

i=randint(0,8)
l[i]['text']='O'
l[i].configure(state=DISABLED)
root.mainloop()
