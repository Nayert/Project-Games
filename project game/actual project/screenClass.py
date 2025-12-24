import pygame 
import random
from gridClass import Grid
pygame.init()


class Game:  # handles how the screen actually looks
    def __init__(self, size_screen: tuple[int]):
        self.screen = pygame.display.set_mode((size_screen[0], size_screen[1]))
        pygame.display.set_caption("Minesweeper")
        self.clock = pygame.time.Clock()
        self.running = True

    def user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                self.main_grid.handle_input(event, 50, 500, 50)

    def run(self):
        
        self.main_grid = Minesweeper_grid(10, 10, self.screen, 20)

        while self.running:
            self.user_input()  
            self.screen.fill((60, 179, 113))
            self.main_grid.draw_grid(50, 500, 50) 
           
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()




class Minesweeper_grid(Grid):

    def __init__(self, width, height, screen, bombP):
        Grid.__init__(self, width, height, 3)
        self.set_dimension([False, 0, False])  # [revealed, value, flagged]
        self.screen = screen

        self.bomb_Total = (width * height * bombP) // 100
        bomb_coords = set()

        while len(bomb_coords) < self.bomb_Total:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)

            if (x, y) not in bomb_coords:
                bomb_coords.add((x, y))
                self.arr[y][x][1] = "BOMB"

        for bx, by in bomb_coords:
            for x, y in self.get_surrounding_sqrs(bx, by):
                if 0 <= x < self.width and 0 <= y < self.height:
                    if self.arr[y][x][1] != "BOMB":
                        self.arr[y][x][1] += 1
        while not self.arr[x][y][1] == 0 :
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
        self.arr[x][y][0] = True
    
    

    def handle_input(self, event, png_size, topgrid_x, topgrid_y):
        if event.type != pygame.MOUSEBUTTONDOWN:
            return

        for row in range(self.height):
            for col in range(self.width):
                rect = pygame.Rect(
                    col * png_size + topgrid_x,
                    row * png_size + topgrid_y,
                    png_size,
                    png_size
                )

                if rect.collidepoint(event.pos):
                    if event.button == 1:
                        self.arr[row][col][0] = True      # reveal
                    elif event.button == 3:
                        self.arr[row][col][2] = not self.arr[row][col][2]  # flag
                    return
                    


    def draw_grid(self, png_size, topgrid_x, topgrid_y):
        png_dict = {x: "actual project/MinesweeperPNGs/Minesweeper_" + str(x) + ".png" for x in range(1, 9)} | \
                   {"GRASS" + str(x): "actual project/MinesweeperPNGs/Minesweeper_Grass" + str(x) + ".png" for x in range(1, 3)}

        png_dict.update({
            0: "actual project/MinesweeperPNGs/Minesweeper_EMPTY.png",
            "BOMB": "actual project/MinesweeperPNGs/Minesweeper_BOMB.png",
            "FLAG": "actual project/MinesweeperPNGs/Minesweeper_FLAG.png"
        })

        for key, png_path in png_dict.items():
            image = pygame.image.load(png_path).convert_alpha()
            image = pygame.transform.scale(image, (png_size, png_size))
            png_dict[key] = image

        main_rect = pygame.Rect(
            topgrid_x,
            topgrid_y,
            png_size * self.width,
            png_size * self.height
        )

        pygame.draw.rect(self.screen, (34, 139, 34), main_rect, 0)

        for row in range(self.height):
            for col in range(self.width):
                rect = pygame.Rect(
                    col * png_size + topgrid_x,
                    row * png_size + topgrid_y,
                    png_size,
                    png_size
                )

                pygame.draw.rect(self.screen, (200, 200, 200), rect, 1)

                if self.arr[row][col][0]:  # Revealed
                    if self.arr[row][col][1] == "BOMB":
                        self.screen.blit(png_dict["BOMB"], rect.topleft)
        # Reveal the whole grid
                        for r in range(self.height):
                            for c in range(self.width):
                                self.arr[r][c][0] = True
                    else:
                        self.screen.blit(png_dict[self.arr[row][col][1]], rect.topleft)
        # If the tile is empty (0), reveal its immediate neighbors
                        if self.arr[row][col][1] == 0:
                            for x, y in self.get_surrounding_sqrs(col, row):  # returns [x, y]
                                self.arr[y][x][0] = True

                elif self.arr[row][col][2]:  # Flagged
                    self.screen.blit(png_dict["FLAG"], rect.topleft)
                else:  # Unrevealed tile
                    self.screen.blit(png_dict["GRASS" + str(((row + col) % 2) + 1)], rect.topleft)

            


            
game = Game ((1080,720))
game.run()
             
    
