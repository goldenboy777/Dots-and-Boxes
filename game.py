import pygame	
from grid import Grid	



surface = pygame.display.set_mode((600,600))
pygame.display.set_caption('Dots-and-Boxes')

grid=Grid()
running=True
surface.fill((0,0,0))
flag=True
while running:
	for event in pygame.event.get():
		if event.type ==pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if pygame.mouse.get_pressed()[0] and flag:
			 	pos=pygame.mouse.get_pos()
			 	grid.selected(pos[0],pos[1],surface)

			 		
	grid.draw(surface)
	pygame.display.flip()
	