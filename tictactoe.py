import math
import random

class TicTacToe():

    def __init__(self):
        self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
        self.toggle = True

    def add(self, coord: str):
        coord = coord.replace("a","0")
        coord = coord.replace("b","1")
        coord = coord.replace("c","2")
        if self.board[int(coord[0])][int(coord[1])] == ' ':
            if self.toggle:
                self.board[int(coord[0])][int(coord[1])] = 'X'
                self.toggle = False
            else:
                self.board[int(coord[0])][int(coord[1])] = 'O'
                self.toggle = True

    def display(self):
        board = self.board
        str_board = "   0   1   2 \na: {} | {} | {} \n  ---+---+--- \nb: {} | {} | {} \n  ---+---+--- \nc: {} | {} | {}".format(board[0][0],board[0][1],board[0][2],
        board[1][0],board[1][1],board[1][2], board[2][0],board[2][1],board[2][2])
        return str_board

