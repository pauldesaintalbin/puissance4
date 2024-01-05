# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 10:34:07 2024

@author: gabouchomon
"""

class Puissance4:
    def __init__(self):
        self.rows = 6
        self.cols = 7
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * (self.cols * 2 - 1))

    def is_valid_move(self, col):
        return 0 <= col < self.cols and self.board[0][col] == ' '

    def drop_piece(self, col, piece):
        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = piece
                break

    def is_winner(self, piece):
        # Vérifier les lignes
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row][col + i] == piece for i in range(4)):
                    return True

        # Vérifier les colonnes
        for col in range(self.cols):
            for row in range(self.rows - 3):
                if all(self.board[row + i][col] == piece for i in range(4)):
                    return True

        # Vérifier les diagonales (de gauche à droite)
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if all(self.board[row + i][col + i] == piece for i in range(4)):
                    return True

        # Vérifier les diagonales (de droite à gauche)
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if all(self.board[row - i][col + i] == piece for i in range(4)):
                    return True

        return False

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

def play():
    game = Puissance4()
    current_piece = 'X'

    while True:
        game.print_board()
        col = int(input(f"Joueur {current_piece}, choisissez une colonne (0-{game.cols-1}): "))

        if game.is_valid_move(col):
            game.drop_piece(col, current_piece)
            
            if game.is_winner(current_piece):
                game.print_board()
                print(f"Joueur {current_piece} a gagné !")
                break
            elif game.is_board_full():
                game.print_board()
                print("Match nul !")
                break
            else:
                current_piece = 'O' if current_piece == 'X' else 'X'
        else:
            print("Colonne invalide. Veuillez choisir à nouveau.")

if __name__ == "__main__":
    play()
