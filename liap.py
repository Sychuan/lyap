# An algorithm, for computing the fractal is summarized as follows.

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
# ________________________________________________________________________


import sys

from liap_fu import LiapF
from liap_fu import Cl_InitPygame

import pygame
import random


def generate():
    Cl_InitPygame.Size(LiapF.rangexy[0], LiapF.rangexy[1])
    window = Cl_InitPygame.MainSurface()
    LiapF.f_space(window)
    Cl_InitPygame.Flip()
    LiapF.pxarray = None
    LiapF.ImgSave(window, "lf_" + str(LiapF.rangexy) + '_' + str(LiapF.count) + '_' + LiapF.string + ".png")
    Cl_InitPygame.Flip()
    print("finished")


# Cl_InitPygame.finish()
def randomword(length):
    letters = 'AB'
    return ''.join(random.choice(letters) for i in range(length))


try:
    LiapF.rangexy = int(input('window_size='))
except:
    LiapF.rangexy = [50, 50]
try:
    LiapF.scale = int(input('scale='))
except:
    LiapF.scale = 25
try:
    LiapF.count = int(input('count='))
except:
    LiapF.count = 20
try:
    LiapF.string = str(input('string='))
    if LiapF.string == '':
        LiapF.string = randomword(LiapF.wordlength)
        print(LiapF.string)

except:
    LiapF.string = 'AB'

LiapF.method = 1
LiapF.pos = [0, 0]

Cl_InitPygame.Init()
Cl_InitPygame.Size(LiapF.rangexy[0], LiapF.rangexy[1])
window = Cl_InitPygame.MainSurface()

print(window)

generate()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # LiapF.PointInfo(window)

            this_pos = pygame.mouse.get_pos()
            LiapF.pos[0] = LiapF.pos[0] + this_pos[0] / LiapF.scale
            LiapF.pos[1] = LiapF.pos[1] + this_pos[1] / LiapF.scale
            LiapF.scale *= 2
            generate()

            Cl_InitPygame.Flip()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_KP_ENTER]:
                print('new')
                LiapF.string = randomword(LiapF.wordlength)

                generate()
            if keys[pygame.K_1]:
                print('new')
                LiapF.rangexy[0] //= 2
                LiapF.rangexy[1] //= 2
                LiapF.scale *= 2
                generate()
            if keys[pygame.K_2]:
                print('new')
                LiapF.rangexy[0] *= 2
                LiapF.rangexy[1] *= 2
                LiapF.scale *= 2
                generate()
            if keys[pygame.K_3]:
                print('new')
                LiapF.rangexy[0] *= 10
                LiapF.rangexy[1] *= 10
                LiapF.scale *= 10
                generate()
            elif keys[pygame.K_RIGHT]:
                LiapF.pos[0] -= 50 / LiapF.scale
                generate()
            elif keys[pygame.K_LEFT]:
                print('new')
                LiapF.pos[0] += 50 / LiapF.scale
                generate()
            elif keys[pygame.K_UP]:
                print('new')
                LiapF.pos[1] -= 50 / LiapF.scale
                generate()
            elif keys[pygame.K_DOWN]:
                LiapF.pos[1] += 50 / LiapF.scale
                print('new')
                generate()
            elif keys[pygame.K_z]:
                LiapF.scale *= 1.5
                print('new')
                generate()
            elif keys[pygame.K_x]:
                LiapF.scale /= 1.5
                print('new')
                generate()
            elif keys[pygame.K_m]:

                LiapF.method = (LiapF.method + 1) % 5
                print(LiapF.method)
                generate()
            elif keys[pygame.K_n]:
                LiapF.method = (LiapF.method - 1) % 5
                generate()
