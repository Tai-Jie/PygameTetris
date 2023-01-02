import pygame
from pygame.locals import*
from Constant import*
from Color import*

def main():
    
    # initialize the pygame module
    Zpic = pygame.image.load('pic/Z.png')
    pygame.init()
    # load and set the logo
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    pygame.display.set_caption("Tetris")
    screen = pygame.display.set_mode((1200, 800))

    def drawBackground():
        # draw frame
        pygame.draw.rect(screen, pink, [fieldStartX - margin_width, fieldStartY - margin_width, frame_width, frame_height]) # frame
        pygame.draw.rect(screen, black, [fieldStartX+1, fieldStartY+1, field_width-2, field_height-2])
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
    drawTwoBackground()
    

    running = True
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pass
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                screen.fill(black)
                pygame.draw.rect(screen, white, [pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 150, 150], 5, 5)
                drawTwoBackground()
                print(pygame.mouse.get_pos())
                pygame.display.update()

        

if __name__=="__main__":
    # call the main function
    main()