from random import *
class Lion:
  def __init__(self,name):
    self.name=name
    self.hunger = False
    self.htimer = 0
    self.injured = False
    self.asleep = False
    self.hunting = False
    self.bored = True
    self.is_alive = True
    
  def live(self):
    if self.injured==False:
      print('***Lion is  injured!')
      self.injured=True
    elif self.injured==True:
      print('***Sadly your lion died(')
      self.is_alive=False
  def stats(self):
    print('Lion' + self.name)
    if self.hunger == True:
      print('Lion want to eat!')
    if self.hunger == False:
      print('Lion is fed up!')
    if self.injured == True:
      print('Lion is injured, he needs to heal!')
    if self.injured == False:
      print('Lion is healthy!')
    if self.bored == True:
      print("Lion doesn't know what to do!")
    if self.bored == False:
      print("Lion is satisfied!")
    if self.asleep == True:
      print('Lion is sleeping!')
    if self.asleep == False:
      print('Lion is not asleep!')
    if self.hunting==True:
      print('Lion is on the hunt!')
    if self.hunting==False:
      print('Lion is not hunting!')
  def hunt(self):
    print('***Lion is hunting!')
    self.hunting=True
    if self.hunting == True:
      self.eat()
  def eat(self):
    print('***Hunt success!')
    self.htimer=0
    self.hunger=False
    self.hunting=False
  def bores(self):
    print('***Lion Wants to play!')
    self.bored=True
  def plays(self):
    print('***Lion trained and is no more bored!')
    self.bored=False
  def sleep(self):
    print('***Lion fell asleep after a hard work!')
    self.asleep=True
  def do_live(self, move):
    for i in range(4):
      number=randint(1,4)
      if number==1:
        if self.injured == False:
          self.live()
        else:
          numberlive=randint(1,4)
          if numberlive==1:
            self.live()
          elif numberlive==2:
            self.injured == False
          elif numberlive==3:
            self.injured = False
          elif numberlive==4:
            self.injured = False
      elif number==2:
        if self.htimer>=1:
          numberis=randint(1,2)
          if numberis==1:
            self.hunt()
      elif number==3:
        self.bores()
      elif number==4:
        self.plays()
      self.htimer+=1
    self.stats()
lion=Lion(" Sergiy")
for move in range(9):
	if lion.is_alive == False:
		break
	lion.do_live(move)
    
    
    