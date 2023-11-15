from reel import *
from settings import *
import pygame

class Machine:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.reel_index = 0
        self.reel_list = {}
        self.can_toggle = True
        self.spinning = False

        self.spawn_reels()

    # Spins only if all reels are not spinning
    def cooldowns(self):
        for reel in self.reel_list:
            if self.reel_list[reel].reel_is_spinning:
                self.can_toggle = False
                self.spinning = True
        
        if not self.can_toggle and [self.reel_list[reel].reel_is_spinning for reel in self.reel_list].count(False) == 5:
            self.can_toggle = True

    def input(self):
        keys = pygame.key.get_pressed()

        # Checking for space key, toggle spin ability, balance for bet sizing
        #if keys[pygame.K_SPACE] and self.can_toggle and self.currPLayer.balance >= self.currPlayer.bet_size:
        if keys[pygame.K_SPACE]:
            self.toggle_spinning()
            self.spin_time = pygame.time.get_ticks()
            #self.currPlayer.place_bet()
            #self.machine_balance += self.currPlayer.bet_size
            #self.currPLayer.last_payout = None

    def draw_reels(self, delta_time):
        for reel in self.reel_list:
            self.reel_list[reel].animate(delta_time)

    def spawn_reels(self):
        if not self.reel_list:
            x_topleft, y_topleft = 60, -300
        while self.reel_index < 5:
            if self.reel_index > 0:
                x_topleft, y_topleft = x_topleft + (300 + OFFSET_X), y_topleft
            self.reel_list[self.reel_index] = Reel((x_topleft, y_topleft))
            self.reel_index += 1

    def toggle_spinning(self):
        if self.can_toggle:
            self.spin_time = pygame.time.get_ticks()
            self.spinning = not self.spinning
            self.can_toggle = False

            for reel in self.reel_list:
                # Spin Delay
                self.reel_list[reel].start_spin(int(reel) * 350)
                #self.spin_sound.play()

    def update(self, delta_time):
        self.input()
        self.draw_reels(delta_time)
        for reel in self.reel_list:
            self.reel_list[reel].symbol_list.draw(self.display_surface)
            self.reel_list[reel].symbol_list.update()