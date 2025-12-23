import pygame 
pygame.init()

class Game : # handles how the screen actually looks
    def __init__ (self , size_screen : tuple[width : int , length : int] ) :
       self. screen = pygame.display.set_mode((size_screen[0],size_screen[1])) 
       self.clock = pygame.time.Clock()
       self.running = True

    def user_input(self) :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                self.running = False

    def draw_grid (self, ) :
        pass
        pygame.draw.rect()



main_game = Game((1080,720))

while main_game.running :
    main_game.user_input()




pygame.quit()