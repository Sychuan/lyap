import pygame, sys, colorsys 
from pygame import*
from math import modf, log, sin
import math
import numpy as np
from scipy import ndimage
class Cl_InitPygame:    
    def Init():
        pygame.init()
       
    def Size(width,height):
        return pygame.display.set_mode((width, height))
    def MainSurface():
        return pygame.display.get_surface()
    def Flip():
        pygame.display.flip()      
    def finish():
         pygame.quit()
         exit()
                
    
   

class LiapF:
      
     pxarray = pygame.pixelarray
     string = 'AB'
     rangexy = 400
     scale = 100
     count = 100
     method = 1
     pxarray = pygame.PixelArray
     k  = 1
     pos = (0,0)
     
          
     
     
     def Status(x):            
         proc = x/(LiapF.rangexy/100)
         if modf(proc)[0] == 0:
            print ('-'*int(proc)+str(int(proc))+'%')         
         Cl_InitPygame.Flip()
            
     def Exchange_par (a,b):
         return b,a

     def PointInfo(window):
         this_pos = pygame.mouse.get_pos()
         print(str(this_pos)+"-->"+str(LiapF.pos_to_liap(this_pos[0],this_pos[1])))
         LiapF.scale = LiapF.scale * 2
         LiapF.pos = (this_pos)
         LiapF.f_space(window)
         LiapF.pxarray = None
         LiapF.ImgSave(window,"untitled1_"+str(LiapF.rangexy)+'_'+str(LiapF.count)+'_'+LiapF.string+".png")
         print('finished')
         
         
        
                  
    

     def ImgSave (surf,name):
         image.save(surf,name)
         
     def planearray(window):
         LiapF.pxarray=pygame.PixelArray(window)
         
         
     def pos_to_liap(a,b):
        
        a = (a+LiapF.pos[0])/LiapF.scale
        b = (LiapF.rangexy-(b-LiapF.pos[1]))/LiapF.scale
        return a,b


     


     def r_n(p,n):
        
        case = LiapF.string[n%len(LiapF.string)]        
        if case=='A':            
            return p[0]
        elif case=='B':            
            return p[1]
        

     def Exponent(xx,yy,N):
         p = (xx,yy)
         npNlog = np.frompyfunc(LiapF.Nlog,1,1)
         x = 0.5
         E = 0
         for i in range(1,N):             
             xp = (LiapF.r_n(p,i))*x*(1-x)
             #E += LiapF.Nlog(abs((LiapF.r_n(p,i))*(1-2*x)))
             E += npNlog(abs((LiapF.r_n(p,i))*(1-2*x)))
             x = xp
         return E/N

     def Nlog(x):
         if x==0:
             return 0
         else:
             #return   
             try:
                 res = log(x) #1/math.exp(x) 
             except:
                 res = 0
             return res   
     
     def f_space(window):
         
         LiapF.planearray(window) 
         x = np.arange(0,(LiapF.rangexy))
         y = np.arange(0,(LiapF.rangexy))
         xx, yy = np.meshgrid(x, y, sparse=True)
         
         
         
         
         pxx, pyy = LiapF.pos_to_liap(xx,yy)
         
        
         npExp = np.frompyfunc(LiapF.Exponent,3,1)         
         e = npExp(pxx,pyy,LiapF.count)
         e = np.array([list(arr) for arr in e])
         #e = np.flipud(np.fliplr(np.rot90(e))) 
         npColoring = np.frompyfunc(LiapF.f_coloring1,3,0)
         npColoring(e,xx,yy)
         LiapF.pxarray=ndimage.gaussian_filter(LiapF.pxarray, sigma=0.5)
         #LiapF.f_coloring1(e,xx,yy)
         #for x in range(LiapF.rangexy):
             #LiapF.Status(x)
             #for y in range(LiapF.rangexy):
                 #p = LiapF.pos_to_liap(x,y)
                 #e = LiapF.Exponent(p,LiapF.count)
                # LiapF.f_coloring1(e,x,y)
                 

     def f_coloring1(e,x,y):
            if e>=0:
                #e = e%1 
                e = abs(round(e) - e)
                colors = colorsys.hls_to_rgb(0,e,0)                     
                LiapF.pxarray[x][y]=(colors[0]*255,colors[1]*255,colors[2]*255)
            else:    
                try:
                    #e = e%1 
                    e = abs(round(e) - e)
                    #e = abs(math.ceil(e) - e)
                    colors = colorsys.hls_to_rgb(0,e,1)                     
                    LiapF.pxarray[x][y]=(colors[0]*255,colors[1]*255,colors[2]*255)
                except:
                    LiapF.pxarray[x][y]=(100,255,255)     
                    
                    
                     
            
                

    
                     
                    
                

          
