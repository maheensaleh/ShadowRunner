import pygame
import time
from media import colors

blocks = []
positions = []
neighbour_size = 70


# from playgame2 import enemies

class Runner:

    def __init__(self, window, color, size, speed, twoplay=False, color2=colors["player2"]):
        global neighbour_size
        self.neighbour_size = neighbour_size
        self.run_x = 620
        self.run_y = 550
        self.window = window
        self.color = colors["player1"]
        self.size = size
        self.speed = speed
        self.x_chng = 0
        self.y_chng = 0
        self.game_start = False
        self.start = 0
        self.show = []
        self.twoplay = twoplay
        self.play = True
        self.glimpse = False
        self.glimpse_count = 0
        self.glimpse_time = 0.25
        if self.twoplay:
            self.run_x2 = 820
            self.run_y2 = 550
            self.color2 = color2
            self.x_chng2 = 0
            self.y_chng2 = 0
            self.show2 = []

    def check_around(self, rx, ry, r):
        c_r = self.window.window.get_at_mapped((rx + r, ry))
        c_l = self.window.window.get_at_mapped((rx - r, ry))
        c_u = self.window.window.get_at_mapped((rx, ry + r))
        c_d = self.window.window.get_at_mapped((rx, ry - r))
        return c_r, c_l, c_u, c_d

    def draw(self, pos, color):
        pygame.draw.circle(self.window.window, color, pos, 10)

    def move(self):

        for x in pygame.event.get():
            if x.type == pygame.QUIT:
                pygame.quit()
                quit()

            if x.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print((mx, my))

                cx, cy = pygame.mouse.get_pos()
                print((cx, cy))

                if 1000 < cx < 1000 + 160 and 200 < cy < 200 + 50:
                    self.play = not self.play
                    print("pause", self.play)

            if x.type == pygame.KEYDOWN:

                # MOVES FOR PLAYER 1
                if x.key == pygame.K_RIGHT:
                    self.x_chng = self.speed
                    self.y_chng = 0
                elif x.key == pygame.K_LEFT:
                    self.x_chng = -self.speed
                    self.y_chng = 0
                elif x.key == pygame.K_UP:
                    self.x_chng = 0
                    self.y_chng = -self.speed
                elif x.key == pygame.K_DOWN:
                    self.x_chng = 0
                    self.y_chng = self.speed

                # MOVES FOR PLAYER 2
                if self.twoplay:
                    if x.key == pygame.K_d:
                        self.x_chng2 = self.speed
                        self.y_chng2 = 0
                    elif x.key == pygame.K_a:
                        self.x_chng2 = -self.speed
                        self.y_chng2 = 0
                    elif x.key == pygame.K_w:
                        self.x_chng2 = 0
                        self.y_chng2 = -self.speed
                    elif x.key == pygame.K_s:
                        self.x_chng2 = 0
                        self.y_chng2 = self.speed

                # GAME START:
                if self.game_start == False:
                    if x.key == pygame.K_SPACE:
                        self.game_start = True
                        self.start = pygame.time.get_ticks()

            if x.type == pygame.KEYUP:
                if x.key == pygame.K_RIGHT or x.key == pygame.K_LEFT or x.key == pygame.K_UP or x.key == pygame.K_DOWN:
                    self.x_chng = 0
                    self.y_chng = 0

                if x.key == pygame.K_a or x.key == pygame.K_w or x.key == pygame.K_s or x.key == pygame.K_d:
                    self.x_chng2 = 0
                    self.y_chng2 = 0  #

        self.run_x, self.run_y = self.cal_move(self.x_chng, self.y_chng, self.run_x, self.run_y)
        if self.twoplay:
            self.run_x2, self.run_y2 = self.cal_move(self.x_chng2, self.y_chng2, self.run_x2, self.run_y2)

        if self.glimpse is True:

            # glimpse 1
            if self.glimpse_count == 0:
                pass
            if self.glimpse_count == 1:
                time.sleep(self.glimpse_time)
            if self.glimpse_count == 2:
                if not self.twoplay:
                    self.hide_maze(self.run_x, self.run_y)
                if self.twoplay:
                    self.hide_maze(self.run_x, self.run_y, self.run_x2, self.run_y2)
            if self.glimpse_count == 3:
                time.sleep(self.glimpse_time)
            if self.glimpse_count == 4:
                #pass
                time.sleep(self.glimpse_time)
            if self.glimpse_count == 5:
                if not self.twoplay:
                    self.hide_maze(self.run_x, self.run_y)
                if self.twoplay:
                    self.hide_maze(self.run_x, self.run_y, self.run_x2, self.run_y2)
            if self.glimpse_count == 6:
                time.sleep(self.glimpse_time)
            if self.glimpse_count == 7:
                time.sleep(self.glimpse_time)
                self.glimpse = False
                # if enemies_toggle:
                #     enemies.ghost_active = True

            if self.glimpse == False:
                self.glimpse_count = 0
            else:
                self.glimpse_count += 1

        #
        else:
            if not self.twoplay:
                self.hide_maze(self.run_x, self.run_y)

            if self.twoplay:
                self.hide_maze(self.run_x, self.run_y, self.run_x2, self.run_y2)

        self.window.mess("end", colors["red"], 20, 850, 60)

        # self.draw((self.run_x, self.run_y), self.color)
        if self.twoplay:
            # self.draw((self.run_x2, self.run_y2), self.color2)
            print(self.run_x, self.run_y)
            return [((self.run_x, self.run_y), self.color), ((self.run_x2, self.run_y2), self.color2)]

        else:
            return ((self.run_x, self.run_y), self.color)

    def hide_maze(self, rx, ry, rx2=None, ry2=None):
        show = []
        r = 10
        self.x_low = (rx - self.neighbour_size)
        self.x_high = (rx + self.neighbour_size) + 10

        self.y_low = ry - self.neighbour_size
        self.y_high = (ry + self.neighbour_size)

        for nx in range(self.x_low, self.x_high, 10):
            for ny in range(self.y_low, self.y_high, 10):
                show.append((nx, ny))

        # # to hide the remaining maze
        if rx2 is None:
            for p in range(0, self.window.width + 1, r):
                for q in range(0, self.window.height + 1, r):
                    if (p, q) not in show:
                        pygame.draw.circle(self.window.window, colors["black"], (p, q), 10)

                    # if ((p - rx) ** 2 + ((q) - ( ry)) ** 2) > (self.neighbour_size ** 2):
                    #     pygame.draw.circle(self.window.window, colors["black"], (p, q), r)
        else:
            show2 = []

            self.x2_low = (rx2 - self.neighbour_size)
            self.x2_high = (rx2 + self.neighbour_size) + 10

            self.y2_low = ry2 - self.neighbour_size
            self.y2_high = (ry2 + self.neighbour_size)

            for nx2 in range(self.x2_low, self.x2_high, 10):
                for ny2 in range(self.y2_low, self.y2_high, 10):
                    show2.append((nx2, ny2))

            # to hide the maze:
            for p in range(0, self.window.width, r):
                for q in range(0, self.window.height + 1, r):
                    if (p, q) not in show and (p, q) not in show2:
                        pygame.draw.circle(self.window.window, colors["black"], (p, q), 10)
                    # if ((p - rx) ** 2 + ((q) - ( ry)) ** 2) > (self.neighbour_size ** 2):
                    # pygame.draw.circle(self.window.window, colors["black"], (p, q), r)

    def cal_move(self, xc, yc, rx, ry):

        rx += xc
        ry += yc

        if rx <= 0 or rx >= self.window.width:
            rx -= xc
        if ry <= 0 or ry >= self.window.height:
            ry -= yc

        check = 0
        try:
            check_right, check_left, check_up, check_down = self.check_around(rx, ry, 9)
        except:
            pass

        if check_right != 205 and check_left != 205 and check_up != 205 and check_down != 205:
            pass
        else:
            rx -= xc
            ry -= yc

        return rx, ry

    def get_show_x(self):
        return (self.x_low, self.x_high)

    def get_show_y(self):
        return (self.y_low, self.y_high)

    def get_show_x2(self):
        if self.twoplay:
            return (self.x2_low, self.x2_high)

    def get_show_y2(self):
        if self.twoplay:
            return (self.y2_low, self.y2_high)






