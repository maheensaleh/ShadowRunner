import pygame
pygame.init()
from media import colors,bg_copy,sbg
from gamewindow import GameWindow
from runnerfor2 import Runner
from media import play_music
from enemy import enemy
import  time
fps=pygame.time.Clock()
twplayer = False


# to display main menu
def menu(play_window2):
    global twplayer

    play_music('main.mp3')

    #menu= True
    while True:
        mode = play_window2.main_menu()
        if mode != None:
            if mode == 'single':
                twplayer = False
                break
            elif mode == 'multi':
                twplayer = True
                break
        pygame.display.update()
        fps.tick(20)


# to run maze game things
def gameloop(play_window2,playback_window2,enemies,enemies2=None):
    # startcontdown = True
    runner = Runner(play_window2, colors["yellow"], 10, 10, twplayer)
    maze1 = True
    time_passed = 0

    while True:
        if runner.play:
            # set backgroundmess
            playback_window2.window.fill(colors["black"])
            play_window2.set_background(bg_copy)

            # score area backgrnd
            playback_window2.window.blit(sbg, (920, 0))

            # give instruction:
            pygame.draw.circle(playback_window2.window, colors["player1"], (950,360), 10)
            playback_window2.mess(''':UP-DOWN-RIGHT-LEFT''',colors["black"],20,960,350)

            playback_window2.mess('''BEWARE OF GHOST-> ''',colors["black"],20,950,380)
            pygame.draw.circle(playback_window2.window, colors["red"], (1180,390), 10)

            if twplayer:  # then give extra instructions:

                playback_window2.mess('''PLAYER-1''', colors["black"], 30, 1000, 300)
                playback_window2.mess('''PLAYER-2''', colors["black"], 30, 1000, 470)

                playback_window2.mess('''-----------''', colors["black"], 30, 1000, 420)
                pygame.draw.circle(playback_window2.window, colors["player2"], (1000, 530-5), 10)
                playback_window2.mess(''': A-W-S-D''', colors["black"], 20, 1020, 520-5)

                playback_window2.mess('''BEWARE OF GHOST-> ''', colors["black"], 20, 950, 540)
                pygame.draw.circle(playback_window2.window,colors["ghost2"], (1180, 550), 10)

            # end instruction

            # draw gems:
            playback_window2.put_gems()

            # check if get gem
            if (runner.run_x, runner.run_y) in playback_window2.gem_cods:
                # print("got ghem")
                i = playback_window2.gem_cods.index((runner.run_x, runner.run_y))
                playback_window2.gem_cods.pop(i)
                runner.glimpse = True

            if twplayer:
                if (runner.run_x2, runner.run_y2) in playback_window2.gem_cods:
                    # print("got ghem")
                    i = playback_window2.gem_cods.index((runner.run_x2, runner.run_y2))
                    playback_window2.gem_cods.pop(i)
                    runner.glimpse = True

            # get gem check ends


            # game win
            if runner.run_x== 860 and runner.run_y==70:
                play_window2.n = "yellow"
                break
            if twplayer:
                if runner.run_x2==860 and runner.run_y2==70:
                    play_window2.n = "pink"
                    break


            # maze switch and display
            if maze1:
                play_window2.set_maze_1()
            else:
                play_window2.set_maze_2()
            # end maze switch display

            # move runner
            draw_args = runner.move()  ##get player pos and color
            if runner.game_start == False:  ## if space not pressed then draw player at strating pos
                runner.run_x,runner.run_y = 620,550
                if twplayer:
                    runner.run_x2,runner.run_y2 = 820,550

            if twplayer:
                runner.draw(draw_args[0][0], draw_args[0][1])  # draw plyer1
                runner.draw(draw_args[1][0], draw_args[1][1])  # draw plyer2

            else:
                print(draw_args[0])
                runner.draw(draw_args[0], draw_args[1])  # draw 1 player only

            # GHOST WORK

            runner_pos = (runner.run_x,runner.run_y)
            max_x = runner.get_show_x()
            max_y = runner.get_show_y()

            # FOR RUNNER 1
            g_pos = enemies.move(runner_pos, max_x, max_y,runner.glimpse)

            if g_pos == False:
                if twplayer:
                    play_window2.n = "player 2"
                else:
                    play_window2.n = 'gameover'
                break
            enemies.draw(g_pos)
            ## runner 1 ghost end here

            # Runner 2 ghost
            if twplayer:
                runner_pos2 = (runner.run_x2,runner.run_y2)
                max_x2 = runner.get_show_x2()
                max_y2= runner.get_show_y2()

                g_pos2 = enemies2.move(runner_pos2, max_x2, max_y2,runner.glimpse)
                if g_pos2 == False:
                    play_window2.n = 'player 1'
                    #dispaly that player won
                    break
                enemies2.draw(g_pos2)
            # ghost 2 end here


            # window separator:
            pygame.draw.rect(play_window2.window, colors["darkbrown"], [899, 0, 40, 600])

            # making play pause button:
            pygame.draw.rect(play_window2.window, colors["darkbrown"], [1000 - 10, 200 - 10, 160 + 20, 50 + 20])
            pygame.draw.rect(play_window2.window, colors["l_violet"], [1000, 200, 160, 50])
            play_window2.mess("PAUSE", colors["black"], 35, 1022, 206)

            # timer
            pygame.draw.rect(play_window2.window, colors["darkbrown"], [1000 - 10, 300 - 10 - 100-100, 160 + 20, 50 + 20])
            pygame.draw.rect(play_window2.window, colors["l_violet"], [1000, 300 - 100-100, 160, 50])
            play_window2.mess(str(time_passed // 1000), colors["black"], 35, 1070, 303 - 100-100)



            # timer to switch maze
            if runner.game_start:
                time_passed = pygame.time.get_ticks() - runner.start

                if time_passed > 40000:

                    # reset the gems:
                    playback_window2.gem_cods = [(760, 530), (470, 230), (360, 370), (620, 70), (400, 150), (760, 290), (
                        440, 390), (440, 550)]

                    #reset the enemy
                    enemies = enemy(play_window2, colors["red"], 10, 10, 490, 510)
                    enemies.ghost_active = False

                    runner.start = pygame.time.get_ticks()
                    maze1 = not maze1
                    runner.run_x, runner.run_y = 620,550

                    if twplayer:
                        runner.run_x2, runner.run_y2 = 820, 550
                        enemies2 = enemy(play_window2, colors["ghost2"], 10, 10, 300, 510)
                        enemies2.ghost_active = False

            if runner.game_start==False :  ## to give game sart instruction
                play_window2.mess(''' Enter SPACE to START the game''',colors["red"], 30, 200, 200)
            pygame.display.update()

        else:  # when in pausd state
            pygame.draw.rect(play_window2.window, colors["l_violet"], [1000, 200, 160, 50])
            play_window2.mess("RESUME", colors["black"], 35, 1019, 206)
            # pause_start = time_passed

            for x in pygame.event.get():
                if x.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if x.type == pygame.MOUSEBUTTONDOWN:
                    cx, cy = pygame.mouse.get_pos()
                    print((cx, cy))

                    if 1000 < cx < 1000 + 160 and 200 < cy < 200 + 50:
                        pause_time = pygame.time.get_ticks() - time_passed
                        runner.start = pause_time
                        runner.play = not runner.play

            pygame.display.update()

        fps.tick(20)

# end of function definitoosn

#create windows
play_window2 = GameWindow(900, 600, "Shadow Runner")
playback_window2 = GameWindow(1200, 600, "main window")
playback_window2.window.blit(play_window2.window, (0, 0))

# main loop
while True:
    enemies = enemy(play_window2, colors["red"], 10, 10, 490, 510)
    enemies2 = enemy(play_window2, colors["ghost2"], 10, 10, 300, 510)
    enemies.ghost_active, enemies2.ghost_active = False, False
    menu(play_window2)
    play_music('ingame.mp3')
    playback_window2.gem_cods = [(760, 530), (470, 230), (360, 370), (620, 70), (400, 150), (760, 290), (
        440, 390), (440, 550)]
    if twplayer:
        gameloop(play_window2,playback_window2,enemies,enemies2)
    else:
        gameloop(play_window2,playback_window2,enemies)

