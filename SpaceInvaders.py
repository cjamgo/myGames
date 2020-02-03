import pygame

pygame.init() #initilizes pygame

#create the screen
# screen = pygame.display.set_mode((800, 600))#need tuple in between parenthesis or it wont work
screen = pygame.display
screen.set_mode((800, 600))
screen.set_caption(('Space Invaders: By yours truly')) #title


#hello


#main loop(creates infinte loop)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
