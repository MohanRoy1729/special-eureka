from time import sleep
import random
pSym='X'
cSym='O'
p1=p2=c1=c2=0

pos_init=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def stat(): 
 for i in [0,1,2]:
  for j in [0,1,2]:
   print (pos_init[i][j],'|',end ='')
  print('\n')

def pl_move():
 print("enter coordinates of your move: ",end='')
 p1,p2=map(int,input().split())
 if pos_init[p1][p2]!=' ':
  print("Wrong Move!!! \nEnter Again")
  pl_move()
 else:
  return [p1,p2]

def comp_move():
 print("thinking :) ")
 c1=random.choice([0,1,2])
 c2=random.choice([0,1,2])
 if pos_init[c1][c2]!=' ':
  print("Made an error thinking again ")
 else:
  return [c1,c2]

def vacant():
 cont=False
 for i in [0,1,2]:
  for j in [0,1,2]:
   if pos_init[i][j]==' ':
    cont=True
    break
 if cont==True:
   return True
 else:
   return False

def mover():
 p3,p4=pl_move()
 pos_init[p3][p4]=pSym
 c3,c4=comp_move()
 pos_init[c3][c4]=cSym

def win():
 res=None
 if (pos_init[0][0]==pos_init[0][1]==pos_init[0][2]==pSym) or (pos_init[1][0]==pos_init[1][1]==pos_init[1][2]==pSym) or (pos_init[2][0]==pos_init[2][1]==pos_init[2][2]==pSym) or (pos_init[0][0]==pos_init[1][1]==pos_init[2][2]==pSym)
   res=True
 elif (pos_init[0][0]==pos_init[0][1]==pos_init[0][2]==cSym) or (pos_init[1][0]==pos_init[1][1]==pos_init[1][2]==cSym) or (pos_init[2][0]==pos_init[2][1]==pos_init[2][2]==cSym) or (pos_init[0][0]==pos_init[1][1]==pos_init[2][2]==cSym))  
   res=False
 else 
   res=None
 return res
 
def game():
 print("Let's play TIC TAC TOE!!!")
 stat()
 while (vacant()):
  pl_move()
  mover()
  stat()
  if win():
   print ("You Win :( ")
  comp_move()
  mover()
  stat()
  if (!win()):
   print ("I won :)")

game()

sleep(2)
