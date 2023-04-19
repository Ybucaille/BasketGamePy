import pygame
import random

def main():
    # Initialisation de Pygame
    pygame.init()

    # Définition des dimensions de la fenêtre
    width = 800
    height = 711

    # Définition des couleurs
    white = (255, 255, 255)

    # Création de la fenêtre
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Jeu de Basketball 2")

    # Définition des constantes du joueur
    player_height = 100
    player_speed_X = 1

    # Définition des constantes de la balle
    ball_width = 50
    ball_height = 50
    ball_speed = 10

    # Définition des constantes du panier
    basket_width = 30
    basket_height = 60
    basket_X = 355
    basket_Y = 120
    basket_surface = pygame.Surface((basket_width, basket_height))
    basket_surface.set_alpha(0)

    # Chargement des images
    player_image = pygame.image.load("C:\\Users\\Yann\\Desktop\\basket\\player.png")
    ball_image = pygame.image.load("C:\\Users\\Yann\\Desktop\\basket\\ball.png")
    ball_image = pygame.transform.scale(ball_image, (ball_width, ball_height))
    background_image = pygame.image.load("C:\\Users\\Yann\\Desktop\\basket\\background.png")

    # Initialisation des variables du jeu
    player_x = 200
    player_y = width/2 - player_height/2
    ball_x = player_x + 175
    ball_y = player_y + player_height - ball_height - 30
    ball_speed_x = 0
    ball_speed_y = 0
    score = 0
    font = pygame.font.SysFont(None, 50)

    # Fonction pour afficher le score
    def draw_score():
        score_text = font.render("Score: " + str(score), True, white)
        screen.blit(score_text, (width/2 - score_text.get_width()/2, 20))

    # Boucle principale du jeu
    running = True
    while running:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball_x = player_x + 180
                    ball_y = player_y + player_height/2 - ball_height/2

                    speed = ball_speed + random.uniform(0, 5)
                    ball_speed_x = 0
                    ball_speed_y = -speed
                    initial_ball_x = ball_x
                    initial_ball_y = ball_y

        # Mouvement continu du joueur
        player_x += player_speed_X
        if player_x <= -100 or player_x + player_x-250 >= width:
            player_speed_X = -player_speed_X


        # Mise à jour de la position de la balle
        if ball_x > width:
            ball_x = -ball_width
            ball_speed_x = 0
            ball_speed_y = 0
        elif ball_x >= basket_X and ball_x <= basket_X + basket_width and ball_y >= basket_Y and ball_y <= basket_Y + basket_height:
            score += 3
            ball_x = -ball_width
            ball_speed_x = 0
            ball_speed_y = 0
        elif ball_y < 0:
            ball_x = initial_ball_x
            ball_y = initial_ball_y
            ball_speed_y = -ball_speed_y
        elif ball_y > height:
            ball_x = -ball_width
            ball_speed_x = 0
            ball_speed_y = 0

        # Mise à jour de la position de la balle en fonction de sa vitesse
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Affichage du fond d'écran
        screen.blit(background_image, (0, 0))

        # Affichage du joueur
        screen.blit(player_image, (player_x, player_y))

        # Affichage de la balle
        if ball_x >= 0:
            screen.blit(ball_image, (ball_x, ball_y))

        # Affichage du panier
        screen.blit(basket_surface, (basket_X, basket_Y))

        # Affichage du score
        draw_score()

        # Mise à jour de l'affichage
        pygame.display.update()

    pygame.quit()