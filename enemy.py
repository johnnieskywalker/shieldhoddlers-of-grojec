from character import *
from random import randint, choice
from enemytype import *

class Enemy(Character):
  def __init__(self, player):
    Character.__init__(self)
    self.name = str(choice(list(EnemyType))).split('.')[1]
    self.health = randint(1, player.health)