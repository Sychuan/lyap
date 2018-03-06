#An algorithm, for computing the fractal is summarized as follows.

#    1.Choose a string of As and Bs of any nontrivial length (e.g., AABAB).
#    2.Construct the sequence S formed by successive terms in the string, repeated as many times as necessary.
#    3.Choose a point (a,b) \in [0,4] \times [0,4].
#    4.Define the function r_n = a if S_n = A, and r_n = b if S_n = B.
#    5.Let x_0 = 0.5, and compute the iterates x_{n+1} = r_n x_n (1 - x_n).
#    6.Compute the Lyapunov exponent:
#    \lambda = \lim_{N \rightarrow \infty} {1 \over N} \sum_{n = 1}^N \log \left|{dx_{n+1} \over dx_n}\right| = \lim_{N \rightarrow \infty} {1 \over N} \sum_{n = 1}^N \log |r_n (1 - 2x_n)|
#    7.In practice, \lambda is approximated by choosing a suitably large N.
#   8.Color the point (a,b) according to the value of \lambda obtained.
#    9.Repeat steps (3–7) for each point in the image plane.
#________________________________________________________________________


from sys import exit

import liap_fu
from liap_fu import*
import math

import random, string

def randomword(length):
   letters = 'AB'
   return ''.join(random.choice(letters) for i in range(length))
   


try:
    LiapF.rangexy = int(input('window_size='))
except:
     LiapF.rangexy = 100   
try:
    LiapF.scale = int(input('scale='))
except:
     LiapF.scale = 25 
try:
    LiapF.count = int(input('count='))
except:
     LiapF.count = 60     
try:
    LiapF.string = str(input('string='))
    if LiapF.string=='':
        LiapF.string = randomword(10)
        print(LiapF.string)
        
except:
    LiapF.string = 'AB'

LiapF.method = 1
LiapF.pos = (0,0)#(1320,1320)



Cl_InitPygame.Init()
Cl_InitPygame.Size(LiapF.rangexy,LiapF.rangexy)
print(LiapF.scale)
window = Cl_InitPygame.MainSurface()
methods = {
   
1:LiapF.f_space,

}

methods[LiapF.method](window)
Cl_InitPygame.Flip()



LiapF.pxarray = None
LiapF.ImgSave(window,"untitled_"+str(LiapF.rangexy)+'_'+str(LiapF.count)+'_'+LiapF.string+".png")
Cl_InitPygame.Flip()

print ("finished")

#Cl_InitPygame.finish()



   
while True:
   for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:           
            LiapF.PointInfo(window)
            Cl_InitPygame.Flip()
            
           
            
            
            
           
            
  
  

