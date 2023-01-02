import pygame

display_width = 1200
display_height = 800
cubeSize = 30
field_height = cubeSize*20
field_width = cubeSize*10
button_width = 180
button_height = 70
endMenu_width = 400
endMenu_height = 400
margin_width = 5
frame_width = field_width + margin_width*2
frame_height = field_height + margin_width*2
fieldStartX = (display_width - field_width)//2
fieldStartY = display_height- field_height - margin_width
field1StartX = (display_width//2 - field_width)//2 + 60
field2StartX = (display_width//2 - field_width)//2 + display_width//2 - 60
Auto_drop_event = pygame.USEREVENT + 1
Game_End = pygame.USEREVENT + 2
autoDropPeriod = 1000 # in milliseconds
