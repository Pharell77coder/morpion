import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Morpion")
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
current_player = 1
winner = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            # Convertir les coordonnées de la souris en coordonnées de grille
            column = pos[0] // 100
            row = pos[1] // 100
            if board[row][column] == 0:
                board[row][column] = current_player
                if current_player == 1:
                    current_player = 2
                else:
                    current_player = 1
    # Dessiner les lignes de la grille
    for i in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (i * 100, 0), (i * 100, 300), 2)
        pygame.draw.line(screen, (0, 0, 0), (0, i * 100), (300, i * 100), 2)
    # Dessiner les symboles 'X' et 'O' sur l'écran
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                pygame.draw.line(screen, (255, 0, 0), (col * 100 + 25, row * 100 + 25), (col * 100 + 75, row * 100 + 75), 2)
                pygame.draw.line(screen, (255, 0, 0), (col * 100 + 75, row * 100 + 25), (col * 100 + 25, row * 100 + 75), 2)
            elif board[row][col] == 2:
                pygame.draw.circle(screen, (0, 0, 255), (col * 100 + 50, row * 100 + 50), 25, 2)
    # Vérifiez si un joueur a gagné
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != 0:
            winner = board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != 0:
            winner = board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != 0:
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        winner = board[0][2]
    if winner != 0:
        if winner == 1:
            winner_text = "Joueur 1 a gagné!"
        else:
            winner_text = "Joueur 2 a gagné!"
        font = pygame.font.Font(None, 30)
        text = font.render(winner_text, True, (255, 0, 0))
        text_rect = text.get_rect()
        text_rect.centerx = screen.get_rect().centerx
        text_rect.centery = screen.get_rect().centery
        screen.blit(text, text_rect)
        pygame.display.update()
        pygame.time.wait(3000)
        running = False
    pygame.display.update()
    pygame.time.wait(100)
pygame.quit()
