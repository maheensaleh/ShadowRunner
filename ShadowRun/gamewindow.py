import pygame
from media import colors,play,exit,opt, gameover
import time


class GameWindow:

    def __init__(self, width, height, title):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Shadow Runner")
        self.gem_cods=[(760, 530), (470, 230), (360, 370), (620, 70), (400, 150), (760, 290), (
        440, 390), (440, 550)]

        self.n=0

    def set_background(self,image):
        self.window.blit(image,(0,0))

    def set_maze_1(self):
        bars = [[30, 40, 820, 21], [30, 40, 21, 540], [30, 80, 160, 21], [210, 80, 460, 21], [690, 80, 160, 21], [30, 120, 640, 21], [690, 120, 160, 21], [30, 160, 80, 21],[130, 160, 720, 21], [30, 200, 80, 21], [130, 200, 720, 21], [30, 240, 80, 21], [130, 240, 220, 21], [370, 240, 60, 21], [450, 240, 300, 21],[770, 240, 80, 21], [30, 280, 80, 21], [130, 280, 220, 21], [370, 280, 220, 21], [610, 280, 140, 21], [770, 280, 80, 21], [30, 320, 80, 21],[130, 320, 460, 21], [610, 320, 140, 21], [770, 320, 80, 21], [30, 360, 80, 21], [130, 360, 460, 21], [610, 360, 140, 21], [770, 360, 80, 21], [30, 400, 160, 21],[210, 400, 220, 21], [450, 400, 300, 21], [770, 400, 80, 21], [30, 440, 160, 21], [210, 440, 220, 21], [450, 440, 300, 21], [770, 440, 80, 21], [30, 480, 160, 21],  [210, 480, 220, 21], [450, 480, 300, 21], [770, 480, 80, 21], [30, 520, 400, 21], [450, 520, 220, 21], [690, 520, 60, 21], [770, 520, 80, 21], [30, 560, 820, 21],[110, 40, 21, 100], [110, 400, 21, 100], [110, 520, 21, 60], [190, 200, 21, 100], [190, 320, 21, 60], [270, 40, 21, 60], [270, 200, 21, 100], [270, 320, 21, 60],[270, 400, 21, 100], [350, 40, 21, 60], [350, 320, 21, 60], [350, 400, 21, 100], [430, 40, 21, 60], [430, 280, 21, 100], [510, 40, 21, 60], [510, 200, 21, 60],[510, 280, 21, 220], [510, 520, 21, 60], [590, 40, 21, 60], [590, 200, 21, 60], [590, 400, 21, 100], [590, 520, 21, 60], [670, 200, 21, 100], [670, 320, 21, 180],[750, 80, 21, 100], [830, 80, 21, 500]]
        for p in bars:
            pygame.draw.rect(self.window, colors["blue"], [p[0],p[1],p[2],p[3]])

    def set_maze_2(self):

        bars =[[30, 40, 820, 21], [690, 80, 160, 21], [290, 80, 380, 21], [30, 80, 240, 21], [30, 120, 80, 21], [130, 120, 140, 21], [290, 120, 380, 21], [690, 120, 160, 21], [770, 160, 80, 21], [690, 160, 60, 21], [290, 160, 380, 21], [130, 160, 140, 21], [30, 160, 80, 21], [30, 200, 80, 21], [130, 200, 140, 21], [290, 200, 380, 21], [690, 200, 60, 21], [770, 200, 80, 21], [770, 240, 80, 21], [130, 240, 620, 21], [30, 240, 80, 21], [30, 280, 80, 21], [130, 280, 720, 21], [770, 320, 80, 21], [610, 320, 140, 21], [370, 320, 220, 21], [30, 320, 320, 21], [30, 360, 320, 21], [370, 360, 220, 21], [610, 360, 140, 21], [770, 360, 80, 21], [770, 400, 80, 21], [130, 400, 620, 21], [30, 400, 80, 21], [30, 440, 80, 21], [130, 440, 620, 21], [770, 440, 80, 21], [770, 480, 80, 21], [30, 480, 720, 21], [30, 520, 720, 21], [770, 520, 80, 21], [30, 560, 820, 21], [30, 40, 21, 540], [110, 40, 21, 60], [110, 320, 21, 60], [110, 520, 21, 60], [190, 520, 21, 60], [190, 320, 21, 60], [190, 240, 21, 60], [190, 40, 21, 180], [350, 80, 21, 60], [350, 160, 21, 60], [350, 240, 21, 60], [350, 520, 21, 60], [430, 520, 21, 60], [430, 400, 21, 60], [430, 320, 21, 60], [430, 240, 21, 60], [430, 160, 21, 60], [430, 80, 21, 60], [510, 80, 21, 60], [510, 160, 21, 60], [510, 240, 21, 60], [510, 320, 21, 60], [510, 400, 21, 60], [510, 520, 21, 60], [590, 520, 21, 60], [590, 400, 21, 60], [590, 240, 21, 60], [590, 80, 21, 140], [750, 80, 21, 60], [830, 80, 21, 500]]

        for p in bars:
            pygame.draw.rect(self.window, colors["blue"], [p[0],p[1],p[2],p[3]])

    def mess(self,message, color, size, x, y):
        text_type = pygame.font.SysFont("algerian", size)
        test_disp = text_type.render(message, True, color)
        self.window.blit(test_disp, (x, y))

    def put_gems(self):
        for p in self.gem_cods:
            pygame.draw.circle(self.window,colors["gemcolor"],p,10)

    def main_menu(self):

        if self.n == 'gameover':
            self.window.fill((0, 0, 0))
            pygame.display.update()
            for i in range(3):
                self.window.blit(gameover, (200, 200))
                pygame.display.update()
                time.sleep(0.5)
                self.window.fill((0,0,0))
                pygame.display.update()
                time.sleep(0.5)
            self.window.blit(gameover, (200, 200))
            pygame.display.update()
            time.sleep(2)
            self.n =0

        elif self.n == "player 1":
            self.window.fill((0, 0, 0))
            pygame.display.update()
            for i in range(3):
                self.mess("YELLOW PLAYER WON", colors["result"], 50, 300,300)
                self.mess("PINK PLAYER LOSE", colors["result"], 50, 300,350)

                pygame.display.update()
                time.sleep(0.5)
                self.window.fill((0,0,0))
                pygame.display.update()
                time.sleep(0.5)
            self.mess("YELLOW PLAYER WON", colors["result"], 50, 300, 300)
            self.mess("PINK PLAYER\nLOSE", colors["result"], 50, 300, 350)

            pygame.display.update()
            time.sleep(2)
            self.n =0

        elif self.n == "yellow":
            self.window.fill((0, 0, 0))
            pygame.display.update()
            for i in range(3):
                self.mess("YELLOW PLAYER WON", colors["result"], 50, 300,300)

                pygame.display.update()
                time.sleep(0.5)
                self.window.fill((0,0,0))
                pygame.display.update()
                time.sleep(0.5)
            self.mess("YELLOW PLAYER WON", colors["result"], 50, 300, 300)

            pygame.display.update()
            time.sleep(2)
            self.n =0

        elif self.n == "pink":
            self.window.fill((0, 0, 0))
            pygame.display.update()
            for i in range(3):
                self.mess("PINK PLAYER WON", colors["result"], 50, 300,300)

                pygame.display.update()
                time.sleep(0.5)
                self.window.fill((0,0,0))
                pygame.display.update()
                time.sleep(0.5)
            self.mess("PINK PLAYER WON", colors["result"], 50, 300, 300)

            pygame.display.update()
            time.sleep(2)
            self.n =0

        elif self.n == "player 2":
            self.window.fill((0, 0, 0))
            pygame.display.update()
            for i in range(3):
                self.mess("PINK PLAYER WON", colors["result"], 50, 300,300)
                self.mess("YELLOW PLAYER LOSE", colors["result"], 50, 300,350)

                pygame.display.update()
                time.sleep(0.5)
                self.window.fill((0,0,0))
                pygame.display.update()
                time.sleep(0.5)

            self.mess("PINK PLAYER WON", colors["result"], 50, 300, 300)
            self.mess("YELLOW PLAYER LOSE", colors["result"], 50, 300, 350)

            pygame.display.update()
            time.sleep(2)
            self.n =0


        self.window.fill(colors['black'])
        self.mess('shadow', colors['red'], 80, 480,100)
        self.mess('runner', colors['red'], 80, 480, 200)

        pygame.draw.rect(self.window, colors["maze"], [570, 380, 140, 40])
        pygame.draw.rect(self.window, colors["maze"], [570, 480, 140, 40])
        self.mess("play", colors["red"], 30,600, 380)
        self.mess("exit", colors["red"], 30, 600, 480)

        if self.n == 'options':
            pygame.draw.rect(self.window, colors["maze"], [480,550,140,40])
            pygame.draw.rect(self.window, colors["maze"],[680,550,140,40])
            self.mess("singleplayer",colors["coral"],20,480,550)
            self.mess("multiplayer",colors["coral"],20,680,550)
            # self.mess('singleplayer or multiplayer', colors['coral'], 20, 250, 550 )

        for x in pygame.event.get():
            if x.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(mx,my)
                if 550<my<550+40:
                    if 480<mx<480+140:
                        print('singlr') #after clicking play
                        self.n = 'single'
                        return self.n
                    if 680 < mx < 680 + 140:
                        print('multi')  #after clicking play
                        self.n = 'multi'
                        return self.n

                if 570 <mx<570+ 140:
                    if 380<my< 380+ 40: # play btn
                      #  global n
                        self.n = 'options'
                        break


                    if 480<my<480+40: #exit btn
                        print(my)
                        pygame.quit()
                        quit()

                    '''if 505<my<525:
                        print('last if')
                        self.n=2
                        break'''







