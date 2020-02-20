import pygame

# player1 = yellow - ghost - red
# player2 = pink - ghost - white

# defining colors
colors = {"result":(255, 140, 0),"player1":(227, 213, 23),"ghost2":(255,255,255),"player2":(251, 0, 255),"gemcolor":(52, 235, 113), "darkbrown":(90,55,14),"brown":(156, 82, 8),"maze":(255, 255, 0),"black": (0, 0, 0), "white": (255, 255, 255), "red": (255, 0, 0), "yellow": (255, 255, 0),"lime": (0, 255, 0), "blue": (0, 0, 205),"coral": (255, 0, 196), "l_violet": (255,255,0), "l_green": (127, 255, 0)}

# loading images
bg=pygame.image.load('bwbg.jpeg') # maze bacground pic
sbg=pygame.image.load('sbg3.png') # side bar
exit=pygame.image.load('exit_btn.png')
play = pygame.image.load('play_btn.png')
opt = pygame.image.load('opt_btn.png')
gameover = pygame.image.load('out.png')


bg_copy= bg.copy()
# this works on images with per pixel alpha too
alpha = 5
bg_copy.set_alpha(100)


def play_music(music):

    intro_music =pygame.mixer.music
    intro_music.load(music)
    intro_music.set_volume(0.7)
    intro_music.play(-1, 0.0)

