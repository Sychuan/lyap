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



import sys

from liap_fu import LiapF
from liap_fu import Cl_InitPygame

import pygame
import random

        

def generate():
    
    Cl_InitPygame.Size(LiapF.rangexy,LiapF.rangexy)
    window = Cl_InitPygame.MainSurface()
    methods[LiapF.method](window)
    Cl_InitPygame.Flip()
    LiapF.pxarray = None
    LiapF.ImgSave(window,"untitled_"+str(LiapF.rangexy)+'_'+str(LiapF.count)+'_'+LiapF.string+".png")
    Cl_InitPygame.Flip()
    print ("finished")

#Cl_InitPygame.finish()
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
     LiapF.count = 40     
try:
    LiapF.string = str(input('string='))
    if LiapF.string=='':
        LiapF.string = randomword(LiapF.wordlength)
        print(LiapF.string)
        
except:
    LiapF.string = 'AB'

LiapF.method = 1
LiapF.pos = [0,0]
methods = {   
             1:LiapF.f_space,
             
             }


Cl_InitPygame.Init()
Cl_InitPygame.Size(LiapF.rangexy,LiapF.rangexy)
window = Cl_InitPygame.MainSurface()

print(window)



generate()

   
while True:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:           
            LiapF.PointInfo(window)
            Cl_InitPygame.Flip()
        if event.type == pygame.KEYDOWN:
           keys = pygame.key.get_pressed()
           if keys[pygame.K_KP_ENTER]:              
               print('new')
               LiapF.string = randomword(LiapF.wordlength)
               
               generate()
           if keys[pygame.K_2]:              
               print('new')
               LiapF.rangexy *= 2
               LiapF.scale *= 2
               generate()
           elif keys[pygame.K_RIGHT]:         
               LiapF.pos[0] -= 100            
               generate()
           elif keys[pygame.K_LEFT]:                 
               print('new')
               LiapF.pos[0] += 100                 
               generate()
           elif keys[pygame.K_UP]:                
               print('new')
               LiapF.pos[1] -= 100       
               generate()               
           elif keys[pygame.K_DOWN]:               
               LiapF.pos[1] += 100                
               print('new')             
               generate()
           elif keys[pygame.K_z]:               
               LiapF.scale *= 2                
               print('new')             
               generate()
           elif keys[pygame.K_m]:               
               
               
               LiapF.method = (LiapF.method+1)%len(methods)
               print(LiapF.method)
               generate()
           elif keys[pygame.K_n]:               
               
               LiapF.method = (LiapF.method-1)%len(methods)
               
               generate()
            
           
            
          
            
           
            
  
  

