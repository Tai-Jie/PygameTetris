import pygame
from pygame.locals import*
from tetromino import*
from Playfield import Playfield
from Color import*
from Constant import*

# define a main function
def main():
    
    # initialize the pygame module
    picFolder = 'pic/'
    pygame.init()
    # load and set the logo
    logo = pygame.image.load(picFolder + 'logo.png')
    pygame.display.set_icon(logo)

    Zpic = pygame.image.load(picFolder + 'Z.png')
    Lpic = pygame.image.load(picFolder + 'L.png')
    Spic = pygame.image.load(picFolder + 'S.png')
    Jpic = pygame.image.load(picFolder + 'J.png')
    Opic = pygame.image.load(picFolder + 'O.png')
    Tpic = pygame.image.load(picFolder + 'T.png')
    Ipic = pygame.image.load(picFolder + 'I.png')

    pygame.display.set_caption("Tetris")
    screen = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock()
    playfield1 = Playfield()
    playfield2 = Playfield()

    def drawCube(posX, posY, size, color):
        pygame.draw.rect(screen, color, [posX+1, posY+1, size-2, size-2] )
        
    def drawPlayfield(playfield:Playfield, fieldX, fieldY):
        for col in range(len(playfield.field)):
            for row in range(len(playfield.field[col])):
                drawCube(fieldX + col*cubeSize, fieldY + row*cubeSize, cubeSize, playfield.getFieldcolor(col, row))

        for block in playfield.tetromino.blocks:
            x = (playfield.tetromino.centerX + block[0])*cubeSize + fieldX
            y = (playfield.tetromino.centerY + block[1])*cubeSize + fieldY
            drawCube(x, y, cubeSize, playfield.tetromino.color)

    def drawBackground():       
        # draw frame
        pygame.draw.rect(screen, pink, [fieldStartX - margin_width, fieldStartY - margin_width, frame_width, frame_height], 5, 5) # frame
        # draw grid
        for col in range(fieldStartX + cubeSize, fieldStartX + field_width, cubeSize):
            pygame.draw.line(screen, gray, (col-1, fieldStartY + 1), (col-1, fieldStartY + field_height -2), width=2)
        for row in range(fieldStartY + cubeSize, fieldStartY + field_height, cubeSize):
            pygame.draw.line(screen, gray, (fieldStartX + 1, row-1), (fieldStartX + field_width - 2, row-1), width=2)

    def drawTwoBackground():       
        # draw frame1
        pygame.draw.rect(screen, pink, [field1StartX - margin_width, fieldStartY - margin_width, frame_width, frame_height], 5, 5) # frame
        # draw grid1
        for col in range(field1StartX + cubeSize, field1StartX + field_width, cubeSize):
            pygame.draw.line(screen, gray, (col-1, fieldStartY + 1), (col-1, fieldStartY + field_height -2), width=2)
        for row in range(fieldStartY + cubeSize, fieldStartY + field_height, cubeSize):
            pygame.draw.line(screen, gray, (field1StartX + 1, row-1), (field1StartX + field_width - 2, row-1), width=2)

        # draw frame2
        pygame.draw.rect(screen, pink, [field2StartX - margin_width, fieldStartY - margin_width, frame_width, frame_height], 5, 5) # frame
        # draw grid2
        for col in range(field2StartX + cubeSize, field2StartX + field_width, cubeSize):
            pygame.draw.line(screen, gray, (col-1, fieldStartY + 1), (col-1, fieldStartY + field_height -2), width=2)
        for row in range(fieldStartY + cubeSize, fieldStartY + field_height, cubeSize):
            pygame.draw.line(screen, gray, (field2StartX + 1, row-1), (field2StartX + field_width - 2, row-1), width=2)

    def drawPreview(shape, x, y):
        pygame.draw.rect(screen, white, [x, y, 150, 150], 5, 5)
        match shape:
            case Shape.I:
                screen.blit(Ipic, (x + 5, y + 5))
            
            case Shape.J:
                screen.blit(Jpic, (x + 5, y + 5))
            
            case Shape.O:
                screen.blit(Opic, (x + 5, y + 5))
            
            case Shape.T:
                screen.blit(Tpic, (x + 5, y + 5))

            case Shape.L:
                screen.blit(Lpic, (x + 5, y + 5))
            
            case Shape.S:
                screen.blit(Spic, (x + 5, y + 5))

            case Shape.Z:
                screen.blit(Zpic, (x + 5, y + 5))

    def display(text, x, y, s:int=24, center:bool=False):  
        scoreText = pygame.font.Font('Font/FreeSans.ttf', s)
        scoreSurf = scoreText.render(text, True, white)
        scoreRect = scoreSurf.get_rect()
        if center:
            scoreRect.center = (x, y)           
        else:
            scoreRect.topleft = (x, y)
            pygame.draw.rect(screen, black, [scoreRect.topleft[0], scoreRect.topleft[1], scoreRect.width, scoreRect.height]) 
        screen.blit(scoreSurf, scoreRect)

    def drawMenu():
        pygame.draw.rect(screen, white, [(display_width - endMenu_width)/2 - margin_width, 145, 410, 410], 5, border_radius=5) # menu
        pygame.draw.rect(screen, black, [(display_width - endMenu_width)/2, 150, endMenu_width, endMenu_height])

    def pauseLoop():
        drawMenu()
        display('Pause', display_width/2, 250, s=48, center=True)
        pygame.draw.rect(screen, white, [(display_width - button_width)/2, 375, button_width, button_height], 5, 5) # single player
        pygame.draw.rect(screen, white, [(display_width - button_width)/2, 465, button_width, button_height], 5, 5) # two player
        display('Continue', display_width/2, 410, center=True)
        display('Restart  ', display_width/2, 500, center=True)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    if (display_width - button_width)/2 <= mousePos[0] <= (display_width + button_width)/2 and 375 <= mousePos[1] <= 375+70:
                        return
                    
                    elif (display_width - button_width)/2 <= mousePos[0] <= (display_width + button_width)/2 and 465 <= mousePos[1] <= 465+70: 
                        modeChoiceLoop()

    def modeChoiceLoop():
        start_level = 0
        drawMenu()
        display('Choose Mode', display_width/2, 250, s=48, center=True)
        pygame.draw.rect(screen, white, [(display_width - button_width)/2, 375, button_width, button_height], 5, 5) # single player
        pygame.draw.rect(screen, white, [(display_width - button_width)/2, 465, button_width, button_height], 5, 5) # two player
        display('start level: ' + str(start_level), display_width/2, 325, center=True)
        display('Single player', display_width/2, 410, center=True)
        display('Two player', display_width/2, 500, center=True)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    if (display_width - button_width)/2 <= mousePos[0] <= (display_width + button_width)/2 and 375 <= mousePos[1] <= 375+70:
                        playfield1.resetField()
                        playfield1.level = start_level
                        return singleGameLoop()
                    
                    elif (display_width - button_width)/2 <= mousePos[0] <= (display_width + button_width)/2 and 465 <= mousePos[1] <= 465+70: 
                        playfield1.resetField()
                        playfield2.resetField()
                        playfield1.level = start_level
                        playfield2.level = start_level
                        return doubleGameLoop()

    def singleGameLoop():
        # define a variable to control the main loop
        screen.fill(black)
        drawBackground()
        # main loop
        running = True
        frame = 1
        while running:
            if frame%playfield1.getFrame_to_Drop() == 0:
                # print(Playfield.Frame_to_Drop[playfield1.level])
                playfield1.shiftDown()
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        playfield1.shiftLeft()
                        
                    if event.key == pygame.K_RIGHT:
                        playfield1.shiftRight()
                        
                    if event.key == pygame.K_UP:
                        playfield1.rotate()
                        
                    if event.key == pygame.K_DOWN:
                        playfield1.shiftDown()

                    if event.key == pygame.K_SPACE:
                        playfield1.drop()

                    
                    if event.key == pygame.K_ESCAPE:
                        pauseLoop()
                        screen.fill(black)
                        drawBackground()
                        
                if event.type == pygame.KEYUP:
                    pass
                
                if event.type == Game_End:
                    running = False

                display('Score:' + playfield1.getScore(), 10, 75, s=48)        
                display('Lines:' + playfield1.getLines(), 10, 175, s=48)
                display('Level:' + playfield1.getLevel(), 10, 275, s=48)
                # print(event)
            drawPreview(playfield1.tetromino.next_Shape, 900, 60)
            drawPlayfield(playfield1, fieldStartX, fieldStartY)   
            pygame.display.update()
            clock.tick(60)
            frame += 1
        return endLoop(1)

    def doubleGameLoop():
        # define a variable to control the main loop
        screen.fill(black)
        drawTwoBackground()
        # main loop
        running = True
        frame = 1
        while running:
            if frame%playfield1.getFrame_to_Drop() == 0:
                playfield1.shiftDown()
            
            if frame%playfield2.getFrame_to_Drop() == 0:
                playfield2.shiftDown()

            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        playfield1.shiftLeft()
                    
                    if event.key == pygame.K_d:
                        playfield1.shiftRight()
                        
                    if event.key == pygame.K_w:
                        playfield1.rotate()
                        
                    if event.key == pygame.K_s:
                        playfield1.shiftDown()
                    
                    if event.key == pygame.K_SPACE:
                        playfield1.drop()
                        

                    if event.key == pygame.K_LEFT:
                        playfield2.shiftLeft()

                    if event.key == pygame.K_RIGHT:
                        playfield2.shiftRight()
                        
                    if event.key == pygame.K_UP:
                        playfield2.rotate()

                    if event.key == pygame.K_DOWN:
                        playfield2.shiftDown()

                    if event.key == pygame.K_RCTRL:
                        playfield2.drop()


                    if event.key == pygame.K_ESCAPE:
                        pauseLoop()
                        screen.fill(black)
                        drawTwoBackground()
                        
                if event.type == pygame.KEYUP:
                    pass

                if event.type == Auto_drop_event:
                    playfield1.shiftDown()
                    playfield2.shiftDown()
                
                if event.type == Game_End:
                    running = False

                # print score of player 1       
                display('Score:' + playfield1.getScore(), 10, 75) 
                display('Lines:' + playfield1.getLines(), 10, 175)
                display('Level:' + playfield1.getLevel(), 10, 275)

                # print score of playe 2
                display('Score:' + playfield2.getScore(), field2StartX + field_width + 20, 75)
                display('Lines:' + playfield2.getLines(), field2StartX + field_width + 20, 175)
                display('Level:' + playfield2.getLevel(), field2StartX + field_width + 20, 275)
            
                # print(event)
            drawPreview(playfield1.tetromino.next_Shape, 30, 630)
            drawPreview(playfield2.tetromino.next_Shape, 1020, 630)
            drawPlayfield(playfield1, field1StartX, fieldStartY)
            drawPlayfield(playfield2, field2StartX, fieldStartY)
            pygame.display.update()
            clock.tick(60)
            frame += 1
        return endLoop(2)

    def endLoop(mode:int):
        drawMenu()
        display('Game over!', display_width/2, 200, s=48, center=True)
        pygame.draw.rect(screen, white, [(display_width - button_width)/2, 375, button_width, button_height], 5, 5) # restart
        pygame.draw.rect(screen, white, [(display_width - button_width)/2, 465, button_width, button_height], 5, 5) # exit
        display('Restart', display_width/2, 410, center=True)
        display('Exit', display_width/2, 500, center=True)
        if mode == 1:
            display('Score: ' + playfield1.getScore(), display_width/2, 275, s=36, center=True)
        elif mode == 2:
            display('P1 score: ' + playfield1.getScore(), display_width/2, 275, s=36, center=True)
            display('P2 score: ' + playfield2.getScore(), display_width/2, 325, s=36, center=True)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mousePos = pygame.mouse.get_pos()
                    if (display_width - button_width)/2 <= mousePos[0] <= (display_width + button_width)/2 and 375 <= mousePos[1] <= 375+70:
                        playfield1.resetField()
                        return modeChoiceLoop()
                    elif (display_width - button_width)/2 <= mousePos[0] <= (display_width + button_width)/2 and 465 <= mousePos[1] <= 465+70: 
                        pygame.quit()
                        quit()

    modeChoiceLoop()

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()