import pygame
print ('Setup Start')
pygame.init()

window = pygame.display.set_mode(size = (600, 480))
print ('Setup End')
while  True:
    # check for all events
    for event in pygame.event.get():
        if event.type == QUIT:
            10
        pygame.quit()
        sys.exit()




