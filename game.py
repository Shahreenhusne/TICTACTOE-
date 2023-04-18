from play import PComputer , PHuman  # object module passing technic 
import os
os.system ('clear')

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None 


    def print_board (self):
        for row in [self.board[i*3:(i+1)*3] for i in range (3)]:
            print('|'.join(row))
    
    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('|'.join(row))

 
    def available_spots(self):
        return [ count for count , position in enumerate(self.board) if position == " " ]

    def empty_spots (self):
        return " " in self.board
    
    def number_emp_spots (self):
        return len(self.available_spots())
    
    def make_move (self , move , sign) :
        if self.board[move] == ' ':
            self.board[move] = sign
            if self.winner(move , sign):
                self.current_winner = sign
            return True
        return False
    
    def winner (self , move , sign):
        #first check the raw 
        row_move = move // 3 # if move 4 , then cal_move is 4//3=1 ; rounding to the nearest value (//)
        row = self.board[row_move*3 : (row_move+1) * 3] #if cal_move is 1 then the list is [0,1,2]
        if all ((spot == sign for spot in row)):
            return True 

        #second check column 
        col_move = move % 3 # if move is 5 , col_move is 2
        col = [self.board[col_move+ i*3] for i in [0,1,2]] # col = [2,5,8]
        if all ((spot == sign for spot in col)):
            return True 
        
        #third check digonal 
        if move%2 == 0:
            diagonal_1 = [self.board[i] for i in [0,4,8]]
            if all ((spot == sign for spot in diagonal_1)):
                 return True 
            diagonal_2 = [self.board[i] for i in [2,4,6]]
            if all ((spot == sign for spot in diagonal_2)):
                 return True 

        return False  


#### end of the class


### outside the class :
def play (playgame , x_player , your_move , print_game = True ):
    if print_game :
        playgame.print_board_nums ()
    
    sign = "O"
    while playgame.empty_spots ():
        if sign == "X":
            move = x_player.your_move(playgame)

        else :
            move =  your_move. your_move(playgame)  

        if playgame.make_move (move , sign):
            if print_game:
               
                print  (sign+ f' have make it\'s  move to the position {move}')
                playgame.print_board()
                print("\n")

            if playgame.current_winner:
                if print_game:
                    print (sign + "wins🏆")
                return sign
 

            sign = "X" if sign == "O" else "O"
        
    if print_game:
        print("It\'s a tie 😬")

    



# main module 
if __name__ == '__main__':
    x_player = PHuman("X")
    y_player = PHuman("Y" )
    playgame = TicTacToe()
    play(playgame ,x_player , y_player , print_game=True )