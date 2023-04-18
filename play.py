import math
import random


class Player :
  def __init__(self ,sign):
      self.sign = sign
      
  def your_move(self ,  game):
       pass

     
class PComputer(Player) :
  def __init__(self ,sign):
      super().__init__(sign)
  
  def your_move(self , game):
       move = random.choice(game.available_spots())
       return move  #here move represent the position you chose between (0-9)


class PHuman( Player) :
  def __init__(self ,sign):
      super().__init__(sign)
  
  def your_move(self , game):
      valid_move = False 
      value = None 
      while not valid_move:
          move = input(self.sign + '\'s turn. Input move (0-8)' )

          try :
              value = int (move)
              if value not in game.available_spots() :
                  raise ValueError
              valid_move = True
               
          except ValueError:
              print ("Invalid move ❌ , try again 👍")
      return value
 
               


