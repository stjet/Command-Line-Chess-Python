import chess
from termcolor import colored
import sys
is_legal=True
board=chess.Board()
def loss():
   global board
   if board.turn==True:
     print(colored("White Lost",'red'))
   else:
     print(colored("Black Lost", 'red'))
   new_game=input("Play again? (y, n)")
   if new_game=="y":
     board.clear_stack()
     chess_game()
   elif new_game=="n":
     sys.exit()
def chess_game():
 global board
 def move(board):
   if board.turn == True:
     print(colored(str(board), attrs=['bold']))
     player_move=input("White to Move: ")
   elif board.turn == False:
     print(colored(str(board)[::-1], attrs=['bold']))
     player_move=input("Black to Move: ")
   if player_move.lower()=="resign":
     loss()
   legal_moves(player_move)
   board=board.push_san(player_move)
   return board
 def legal_moves(player_move):
     #player_move=chess.Move.uci(player_move)
     player_move=str(player_move).lower()
     if player_move in str(board.legal_moves).lower():
         if board.is_check():
           if board.turn==False:
             print(colored("That move is legal, and White put Black in check!",'green'))
           elif board.turn==True:
             print(colored("That move is legal, and Black put White in check!",'green'))
         else:
           print(colored("That move is legal.",'green'))
     else:
       if player_move in str(board.pseudo_legal_moves).lower():
         print(colored("You are in check, or pinned. Can't do that.",'red'))
         loss() 
       else:
         print(colored("That move is not legal.",'red'))
         loss()
 def tie():
   print("It is no longer possible to checkmate.")
   new_game=input("Play again? (y, n)")
   if new_game=="y":
     board.clear_stack()
     chess_game()
   elif new_game=="n":
     sys.exit()
 print('\033[2J')
 print(colored("Welcome to chess!",'blue'))
 print(colored("""Rules:
 1. Normal Chess rules apply
 2. You can only use algebraic notation (FIDE standard)
 3. Try not to do illegal moves""",'blue','on_grey'))

 while True:
   board=chess.Board(board.fen())
   move(board)
   if board.is_game_over():
           if board.is_checkmate():
             loss()
           elif board.is_stalemate() or board.is_insufficient_material():
             tie()
try:
 chess_game()
except:
 print("Something went wrong.")