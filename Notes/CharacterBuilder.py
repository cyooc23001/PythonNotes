#!/usr/bin/env python3
import random
class Build:
    
    def __init__(self):
        self.job = input('Pick a class: ')
        self.exp = 0
        self.level = 1
        self.actions = []
        if self.job == 'Fighter':
            self.actions.append('Attack')
        elif self.job == 'Cleric' or self.job == 'Druid':
            self.actions.append('Attack')
            self.actions.append('Heal')

    def gainExp(self,exp):
        self.exp += exp
        self.levelCheck()

    def action(self,*args):
        numActions = (self.level // 4) + 1
        x = random.randint(1,10)
        if self.job == 'Fighter':
            numActions += 1
        for action in args:
            x = random.randint(1,10)
            if action in self.actions:
                if action == 'Attack':
                    print('You attack with lightning speed and deal {}'.format(x))
                    numActions -= 1
                elif action == 'Heal':
                    print('You heal yourself for {} hitpoints'.format(x))
                    numActions -= 1
            if not numActions:
                break

    def loseExp(self,exp):
        self.exp -= exp
        self.levelCheck()

    def levelCheck(self):
        if self.exp >= (100 * self.level):
            self.exp = 0
            self.level += 1
        elif self.exp < 0:
            self.level -= 1
            self.exp = (100*self.level) - abs(self.exp)



if __name__ == '__main__':
    pass

