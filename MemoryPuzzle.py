from tkinter import *
import random
from tkinter import ttk
window=Tk()
window.title('Project Memory Game')
tabs = ttk.Notebook(window) 
root= ttk.Frame(tabs)
def draw(c,i,j):
    global base
    if c=='A':
        d=base.create_rectangle(100*i+20,j*100+20,100*i+100-20,100*j+100-20,fill='red')
    elif c=='B':
        d=base.create_rectangle(100*i+20,j*100+20,100*i+100-20,100*j+100-20,fill='yellow')
    elif c=='C':
        d=base.create_rectangle(100*i+20,j*100+20,100*i+100-20,100*j+100-20,fill='blue')
    elif c=='D':
        d=base.create_oval(100*i+20,j*100+20,100*i+100-20,100*j+100-20,fill='red')
    elif c=='E':
        d=base.create_oval(100*i+20,j*100+20,100*i+100-20,100*j+100-20,fill='yellow')
    elif c=='F':
        d=base.create_oval(100*i+20,j*100+20,100*i+100-20,100*j+100-20,fill='blue')
    elif c=='G':
        d=base.create_polygon(100*i+50,j*100+20,100*i+20,100*j+100-20,100*i+100-20,100*j+100-20,fill='red')
    elif c=='H':
        d=base.create_polygon(100*i+50,j*100+20,100*i+20,100*j+100-20,100*i+100-20,100*j+100-20,fill='green')
def displayBoard():
    global base,ans,board,moves
    cnt=0
    for i in range(4):
        for j in range(4):
            rect=base.create_rectangle(100*i,j*100,100*i+100,100*j+100,fill="lavender")
            if(board[i][j]!='.'):
                draw(board[i][j],i,j)
                cnt+=1
    if cnt==16:
        base.create_text(200,450,text="Moves: "+str(moves),font=('arial',20))
def callback(event):
    global base,ans,board,moves,prev
    i=event.x//100
    j=event.y//100
    if board[i][j]!='.':
        return
    moves+=1
    if(prev[0]>4):
        prev[0]=i
        prev[1]=j
        board[i][j]=ans[i][j]
        displayBoard()
    else:
        board[i][j]=ans[i][j]
        displayBoard()
        if(ans[i][j]==board[prev[0]][prev[1]]):
            print("matched")
            prev=[100,100]
            displayBoard()
            return
        else:
            board[prev[0]][prev[1]]='.'
            displayBoard()
            prev=[i,j]
            return
base=Canvas(root,width=500,height=500)
base.pack()
ans = list('AABBCCDDEEFFGGHH')
random.shuffle(ans)
ans = [ans[:4],
       ans[4:8],
       ans[8:12],
       ans[12:]]
base.bind("<Button-1>", callback)
moves=IntVar()
moves=0
prev=[100,100]
board=[list('.'*4) for cnt in range(4)]
displayBoard()
tabs.add(root, text ='Easy') 
tabs.pack(expand = 1, fill ="both") 
window.mainloop()