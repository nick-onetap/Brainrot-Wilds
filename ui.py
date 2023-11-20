from player import *
from settings import *
import pygame, random

class UI:
    def __init__(self, player):
        self.player = player
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.bet_font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.win_font = pygame.font.Font(UI_FONT, WIN_FONT_SIZE)
        self.win_text_angle = random.randint(-4, 4)

    def display_info(self):
        player_data = self.player.get_data()

        # Balance and bet size
        balance_surface = self.font.render("Balance: " + player_data['balance'], True, TEXT_COLOR, None)
        x, y = 20, self.display_surface.get_size()[1] - 30
        balance_rect = balance_surface.get_rect(bottomleft = (x, y))

        bet_surface = self.bet_font.render("Wager: " + player_data['bet_size'], True, TEXT_COLOR, None)
        x = self.display_surface.get_size()[0] - 20
        bet_rect = bet_surface.get_rect(bottomright = (x,y))

        # Player Data
        pygame.draw.rect(self.display_surface, False, balance_rect)
        pygame.draw.rect(self.display_surface, False, bet_rect)
        self.display_surface.blit(balance_surface, balance_rect)
        self.display_surface.blit(bet_surface, bet_rect)

        # Print win amount
        if self.player.last_payout:
            last_payout = player_data['last_payout']
            win_surface = self.win_font.render("GYATT! " + last_payout, True , TEXT_COLOR, None)
            x1 = 800
            y1 = self.display_surface.get_size()[1] - 60
            win_surface = pygame.transform.rotate(win_surface, self.win_text_angle)
            win_rect = win_surface.get_rect(center = (x1, y1))
            self.display_surface.blit(win_surface, win_rect)

    def update(self):
        pygame.draw.rect(self.display_surface, 'Black', pygame.Rect(0, 900, 1600, 100))
        self.display_info()
