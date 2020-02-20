import pygame


class enemy:

    def __init__(self,window, color ,size,speed,gx,gy):

        self.g_pos =(gx,gy)
        self.gx = gx
        self.gy = gy
        self.ghost_active =False
        self.window = window
        self.color = color
        self.size = size
        self.speed = speed
        self.list=[]
        self.i=0

    def draw(self, g_pos):

        if g_pos is not None:
            self.gx , self.gy= g_pos
            self.enemy1 = pygame.draw.circle(self.window.window,self.color,(self.gx,self.gy)  , self.size)

    def move(self,runner_pos,show_x, show_y,glimpse):
        self.mx, self.my = runner_pos
        self.x_low, self.x_high = show_x
        self.y_low , self.y_high = show_y

        if self.x_low<self.gx<self.x_high and self.y_low<self.gy<self.y_high:
            self.ghost_active = True

        while self.ghost_active:
            if len(self.list) <= 2 :
                self.list.append(runner_pos)
            elif len(self.list)> 2 and self.list[-1] != runner_pos:
                for f in range(4):
                    self.list.append(runner_pos)

                self.list.pop(0)

            if abs(self.mx - self.gx) < 15 and abs(
                    self.my - self.gy) < 15:
                return False

            if len(self.list) > 40:
                self.g_pos = self.list[self.i]
                if glimpse == True:
                    pass
                else:
                    self.i += 1

            return (self.g_pos)
