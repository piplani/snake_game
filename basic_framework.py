import pygame as pg  # import all libraries
import time
import random as rd

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
display_width = 800
display_height = 600
block_size = 20
FPS = 30
score = 0
change = 5
direc = 'right'

x = pg.init()  # Return a tuple of (success, failure)
print(x)

smallfont = pg.font.SysFont("font1.ttf", 25)
mediumfont = pg.font.SysFont("font1.ttf", 50)
largefont = pg.font.SysFont("font1.ttf", 80)


def text_objects(text, col, size):
    if size == 'small':
        text_Surf = smallfont.render(text, True, col)
    elif size == 'medium':
        text_Surf = mediumfont.render(text, True, col)
    elif size == 'large':
        text_Surf = largefont.render(text, True, col)
    return text_Surf, text_Surf.get_rect()


def display_message(msg, color, x_dis=0, y_dis=0, size='small'):
    """text = font.render(msg, True, color)
    gameCanvas.blit(text, [display_width / 2, display_height / 2])"""
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width / 2) + x_dis, (display_height / 2) + y_dis
    gameCanvas.blit(textSurf, textRect)


def gameexit():
    pg.quit()  # uninitialize all the pygame libraries
    quit()  # quit python


""" now come the canvas where you will draw your objects"""
gameCanvas = pg.display.set_mode((display_width, display_height))  # 800 height 600 width
pg.display.set_caption('Python', 'pp.png')
logo = pg.image.load('icon.png')
pg.display.set_icon(logo)
pg.display.update()  # update frame by frame for a motion

cloak = pg.time.Clock()

img_head = pg.image.load('head2.png')
apple = pg.image.load('apple.png')


def sore(score):
    text = smallfont.render('Score is:' + str(score), True, white)
    gameCanvas.blit(text, [0, 0])


def pause():
    paused = True
    while paused:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameexit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    gameexit()
                if event.key == pg.K_SPACE:
                    paused = False
        display_message('Game Paused', green, y_dis=-100, size='medium')
        display_message('Press Control to continue', green, y_dis=25)
        pg.display.update()
        cloak.tick(FPS)


def intro():
    yip = True
    img = pg.image.load('pp.png')
    while yip:
        display_message('WELCOME!', green)
        display_message('press spacebar to play', green, y_dis=200)
        gameCanvas.blit(img, (display_width / 2 - 150, display_height / 2 - 300))

        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                gameexit()
            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_SPACE:
                    yip = False
                    gameLoop()
        pg.display.update()
        cloak.tick(FPS)


def python(block_size, gameList):
    if direc == 'right':
        head = img_head
    if direc == 'left':
        head = pg.transform.rotate(img_head, 180)
    if direc == 'up':
        head = pg.transform.rotate(img_head, 90)
    if direc == 'down':
        head = pg.transform.rotate(img_head, 270)
    gameCanvas.blit(head, (gameList[-1][0], gameList[-1][1]))
    for xny in gameList[:-1]:
        pg.draw.rect(gameCanvas, green, [xny[0], xny[1], block_size, block_size])


def gameLoop():
    global direc
    score = 0
    direc = 'right'
    exit = False
    over = False
    x = display_width / 2
    y = display_height / 2
    x_change = 5
    y_change = 0
    x_apple = rd.randrange(0, display_width - block_size)
    y_apple = rd.randrange(0, display_height - block_size)
    snakeList = []
    snakelen = 1
    f = 0
    while not exit:

        while over == True:
            gameCanvas.fill(white)
            display_message('Score: '+str(score), blue,20,-100, size='large')
            display_message('Game over', red, size='large')
            display_message('y to play again q to quit', green, 0, 50, 'medium')
            # display_message('score is ' + str(score), blue, 0, -100, 'medium')
            pg.display.update()
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        exit = True
                        over = False
                    if event.key == pg.K_y:
                        over = False
                        gameLoop()
                if event.type == pg.QUIT:
                    exit = True
                    over = False

        for event in pg.event.get():
            # print event
            if event.type == pg.QUIT:
                exit = True
            if event.type == pg.KEYDOWN:
                if (event.key == pg.K_UP or event.key == pg.K_w) and direc != 'down':
                    direc = 'up'
                    y_change = -change
                    x_change = 0
                elif (event.key == pg.K_DOWN or event.key == pg.K_s) and direc != 'up':
                    direc = 'down'
                    y_change = change
                    x_change = 0
                elif (event.key == pg.K_LEFT or event.key == pg.K_a) and direc != 'right':
                    direc = 'left'
                    x_change = -change
                    y_change = 0
                elif (event.key == pg.K_RIGHT or event.key == pg.K_d) and direc != 'left':
                    direc = 'right'
                    x_change = change
                    y_change = 0
                elif event.key == pg.K_SPACE:
                    pause()

            """if event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                    x_change = 0
                if event.key == pg.K_UP or event.key == pg.K_DOWN:
                    y_change = 0"""
        x += x_change
        y += y_change
        if x >= display_width or x < 0 or y >= display_height or y < 0:
            over = True

        gameCanvas.fill(black)
        apple_thickness = 30
        # pg.draw.rect(gameCanvas, red, [x_apple, y_apple, apple_thickness, apple_thickness])
        gameCanvas.blit(apple, (x_apple, y_apple))
        snakeHead = [x, y]
        snakeList.append(snakeHead)
        if len(snakeList) > snakelen:
            del snakeList[0]
        for seg in snakeList[:-1]:
            if seg == snakeHead:
                over = True
        python(block_size, snakeList)
        sore(score)
        pg.display.update()
        """if x_apple == x and y_apple == y:
            print 'apple eaten'
            x_apple = round(rd.randrange(0, display_width - block_size) / 10.0) * 10.0
            y_apple = round(rd.randrange(0, display_height - block_size) / 10.0) * 10.0
            snakelen += 1"""
        """if x_apple <= x <= x_apple + apple_thickness and y_apple <= y <= y_apple + apple_thickness:
            print 'apple eaten'
            x_apple = rd.randrange(0, display_width - block_size)
            y_apple = rd.randrange(0, display_height - block_size)
            snakelen += 1"""
        if x_apple <= x <= x_apple + apple_thickness or x_apple <= x + block_size <= x_apple + apple_thickness:
            if y_apple <= y <= y_apple + apple_thickness or y_apple <= y + block_size <= y_apple + apple_thickness:
                print('x and y croosover')
                print('apple eaten')

                x_apple = rd.randrange(0, display_width - block_size)
                y_apple = rd.randrange(0, display_height - block_size)
                snakelen += 1
                global score
                global change
                score += 1
                change = 5 + score / 10
                print(score)
                #display_message('score is ' + str(score), blue, 100, -100)
                pg.display.update()
                cloak.tick(FPS)
        cloak.tick(FPS)
    gameexit()


intro()
# gameLoop()
