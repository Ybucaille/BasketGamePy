import pygame
import sys
import basketball
import basketball2

def main():
    pygame.init()

    width = 800
    height = 600

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Menu")

    # Charger l'image de fond du menu
    menu_background = pygame.image.load("C:\\Users\\Yann\\Desktop\\basket\\menu_background.png")

    menu_font = pygame.font.SysFont(None, 50)
    menu_title = menu_font.render("Menu", True, (255, 255, 255))
    menu_title_rect = menu_title.get_rect(center=(width/2, 100))

    option1 = menu_font.render("Jeu 1", True, (255, 255, 255))
    option1_rect = option1.get_rect(center=(width/2, 200))

    option2 = menu_font.render("Jeu 2", True, (255, 255, 255))
    option2_rect = option1.get_rect(center=(width/2, 300))

    option3 = menu_font.render("Quitter", True, (255, 255, 255))
    option3_rect = option3.get_rect(center=(width/2, 400))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if option1_rect.collidepoint(event.pos):
                    basketball.main()
                elif option2_rect.collidepoint(event.pos):
                    basketball2.main()
                elif option3_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        screen.blit(menu_background, (0, 0))
        screen.blit(menu_title, menu_title_rect)
        screen.blit(option1, option1_rect)
        screen.blit(option2, option2_rect)
        screen.blit(option3, option3_rect)
        pygame.display.update()

if __name__ == "__main__":
    main()
