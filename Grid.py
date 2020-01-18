#!/usr/bin/env python 
import random
import pygame
from pygame.locals import *

UP = pygame.K_UP
RIGHT = pygame.K_RIGHT
DOWN = pygame.K_DOWN
LEFT = pygame.K_LEFT


class Grid:
    cells = {}

    def getValue(self, x, y):
        return self.cells[y*10+x]

    def getPos(self, x, y):
        return y*10+x

    def addRandomTile(self, cells):
        isAdded = False
        i = 0
        while(not isAdded and i < 16):
            x = random.randint(0,3)
            y = random.randint(0,3)
            if(cells[y*10+x] == 0):
                cells[y*10+x] = 2
                isAdded = True
            i+=1

    def initCells(self):
        struc = {
            0 : 0,
            1 : 0,
            2 : 0,
            3 : 0,
            10 : 0,
            11 : 0,
            12 : 0,
            13 : 0,
            20 : 0,
            21 : 0,
            22 : 0,
            23 : 0,
            30 : 0,
            31 : 0,
            32 : 0,
            33 : 0                    
        }
        self.addRandomTile(struc)
        self.addRandomTile(struc)
        return struc      
    
    def __init__(self):
        self.cells = self.initCells() 

    def toString(self):
        separateur = ','
        print(str(self.cells[0]) + separateur + str(self.cells[1]) + separateur + str(self.cells[2]) + separateur + str(self.cells[3]))
        print(str(self.cells[10]) + separateur + str(self.cells[11]) + separateur + str(self.cells[12]) + separateur + str(self.cells[13]))
        print(str(self.cells[20]) + separateur + str(self.cells[21]) + separateur + str(self.cells[22]) + separateur + str(self.cells[23]))
        print(str(self.cells[30]) + separateur + str(self.cells[31]) + separateur + str(self.cells[32]) + separateur + str(self.cells[33]))

    def nextInt(self, x, y):
        #Retourne la position et la valeur de la première valeur précédente        
        isFind = False
        y-=1
        while(y>=0 and not isFind): #Je cherche un nombre avant moi            
            if(self.getValue(x,y) != 0):#Si ma case précédente est différente de 0
                isFind = True
            else:
                y-=1
        if(isFind):
            return (y,self.getValue(x,y))
        else:
            return (-1,-1)

    def endRound(self):
        for x in (0,1,2,3):
            #For ligne sauf la première
            for y in (0,1,2,3):
                if(self.cells[self.getPos(x,y)]<0):
                    self.cells[self.getPos(x,y)] = self.getValue(x,y)* -1

    def slideUp(self):
        #For colonne
        for x in (0,1,2,3):
            #For ligne sauf la première
            for y in (0,1,2,3):
                #Gestion de la tuile                
                nextCoord, nextVal = self.nextInt(x,y)
                if(nextCoord == -1):#Je n'ai pas trouvé de valeur avant moi donc je deviens la première case
                    if(y != 0):
                        self.cells[self.getPos(x,0)] = self.cells[self.getPos(x,y)]
                        self.cells[self.getPos(x,y)] = 0
                elif(nextVal == self.getValue(x,y)):
                    self.cells[self.getPos(x,nextCoord)] = self.getValue(x,y)*2 *-1
                    self.cells[self.getPos(x,y)] = 0
                elif((nextCoord+1) != y):                
                    self.cells[self.getPos(x,nextCoord+1)] = self.getValue(x,y)
                    self.cells[self.getPos(x,y)] = 0
        self.endRound()

    def rotateGrid(self):
        tempGrid = {
            0 : self.cells[30],
            1 : self.cells[20],
            2 : self.cells[10],
            3 : self.cells[0],
            10 : self.cells[31],
            11 : self.cells[21],
            12 : self.cells[11],
            13 : self.cells[1],
            20 : self.cells[32],
            21 : self.cells[22],
            22 : self.cells[12],
            23 : self.cells[2],
            30 : self.cells[33],
            31 : self.cells[23],
            32 : self.cells[13],
            33 : self.cells[3]
        }
        self.cells = tempGrid

    def move(self, direction):
        if(direction==UP):
            self.slideUp()
        elif(direction==LEFT):
            self.rotateGrid()
            self.slideUp()
            self.rotateGrid()
            self.rotateGrid()
            self.rotateGrid()
        elif(direction == DOWN):
            self.rotateGrid()
            self.rotateGrid()
            self.slideUp()
            self.rotateGrid()
            self.rotateGrid()
        elif(direction == RIGHT):
            self.rotateGrid()
            self.rotateGrid()
            self.rotateGrid()
            self.slideUp()
            self.rotateGrid()

    def askDirection(self):
        direction = input("Prochaine direction : ") 
        if(direction == 'z'):
            return UP
        elif(direction == 'd'):
            return RIGHT
        elif(direction == 'd'):
            return DOWN
        elif(direction =='q'):
            return LEFT
        else:
            return 0

    def hasSameValueClose(self, x, y):       
        #Je check au dessus
        if(x!=0):
            if(self.getValue(x-1,y)==self.getValue(x,y)):
                return True
        if(x!=3):
            if(self.getValue(x+1,y)==self.getValue(x,y)):
                return True
        if(y!=0):
            if(self.getValue(x,y-1)==self.getValue(x,y)):
                return True
        if(y!=3):
            if(self.getValue(x,y+1)==self.getValue(x,y)):
                return True
        return False

    def calculState(self):
        #Retourne l'etat de victoire dans le premier argument, l'etat de défaite dans le second
        for x in(0,1,2,3):
            for y in (0,1,2,3):
                myVal = self.getValue(x,y)
                if(myVal == 2048):
                    return True,False
                elif(self.hasSameValueClose(x,y)):                    
                    return False, False               
        return False,True

    def letsPlayAGame(self):
        isWin = False
        isLose = False
        while(not isWin and not isLose):
            self.toString()
            direction = self.askDirection()
            if(direction==0):
                print('Erreur, direction non connue')
                continue
            grille.move(direction)
            isWin, isLose = grille.calculState()
            grille.addRandomTile(self.cells)


#grille = Grid()
#grille.letsPlayAGame()
