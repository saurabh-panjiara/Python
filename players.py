# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 20:05:47 2018

@author: saurabh panjiara
"""
from random import choice
file = open('sys.txt','r')
players=[]
players=file.read().splitlines()
teamA=[]
teamB=[]
while len(players)>0:
    
    playerA=choice(players)
    teamA.append(playerA)
    players.remove(playerA)
    if len(players)==0:
        break
    playerB=choice(players)
    teamB.append(playerB)
    players.remove(playerB)
print('teamA:  ',teamA)
print('------------------------------------------')
print('teamB:   ',teamB)
    
