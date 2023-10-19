import pygame


class Escape:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.visible = False
        self.font = "assets/fonts/iknowaghost.ttf"
        self.font = pygame.font.Font(self.font, 50)

    def display(self, event):
        if self.visible:
            pygame.draw.rect(self.screen, (0, 0, 0),
                             (1920//2 - 500//2, 1080//2 - 700//2, 500, 700))
            pygame.draw.rect(self.screen, (255, 255, 255),
                             (1920//2 - 500//2, 1080//2 - 700//2, 504, 704), 3)
            self.button_resume(event)
            save = self.button_save(event)
            value = self.button_quit(event)
            if value == False:
                return value
            if save == "save":
                return save

    def detecte_escape(self, event: pygame.event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if self.visible == False:
                    self.visible = True
                else:
                    self.visible = False

    def button_resume(self, event):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        button_x = (1920 - 300) // 2  # Largeur du bouton = 300
        button_y = (1080 - 50) // 2 - 200  # Hauteur du bouton = 50

        button_rect = pygame.Rect(button_x, button_y, 300, 50)

        if button_rect.collidepoint(mouse_x, mouse_y):
            texte_surface = self.font.render("Resume", True, (255, 128, 0))
            self.resume_button_hovered = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Réalisez l'action que vous souhaitez exécuter lors du clic du bouton
                self.visible = False
        else:
            texte_surface = self.font.render("Resume", True, (255, 255, 255))
            self.resume_button_hovered = False

        text_rect = texte_surface.get_rect()
        text_rect.center = (1920 // 2, 1080 // 2 - 200)

        self.screen.blit(texte_surface, text_rect)

    def button_save(self, event):

        mouse_x, mouse_y = pygame.mouse.get_pos()

        button_x = (1920 - 300) // 2  # Largeur du bouton = 300
        button_y = (1080 - 50) // 2   # Hauteur du bouton = 50

        button_rect = pygame.Rect(button_x, button_y, 300, 50)

        if button_rect.collidepoint(mouse_x, mouse_y):
            texte_surface = self.font.render("Save", True, (255, 128, 0))
            self.resume_button_hovered = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Réalisez l'action que vous souhaitez exécuter lors du clic du bouton
                return "save"
        else:
            texte_surface = self.font.render("Save", True, (255, 255, 255))
            self.resume_button_hovered = False

        text_rect = texte_surface.get_rect()
        text_rect.center = (1920 // 2, 1080 // 2)

        self.screen.blit(texte_surface, text_rect)

    def button_quit(self, event):

        mouse_x, mouse_y = pygame.mouse.get_pos()

        button_x = (1920 - 300) // 2  # Largeur du bouton = 300
        button_y = (1080 - 50) // 2 + 200  # Hauteur du bouton = 50

        button_rect = pygame.Rect(button_x, button_y, 300, 50)

        if button_rect.collidepoint(mouse_x, mouse_y):
            texte_surface = self.font.render("Quit", True, (255, 128, 0))
            self.resume_button_hovered = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Réalisez l'action que vous souhaitez exécuter lors du clic du bouton
                self.visible = False
                return False
        else:
            texte_surface = self.font.render("Quit", True, (255, 255, 255))
            self.resume_button_hovered = False

        text_rect = texte_surface.get_rect()
        text_rect.center = (1920 // 2, 1080 // 2 + 200)

        self.screen.blit(texte_surface, text_rect)
