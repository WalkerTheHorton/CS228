import pygame

class PYGAME_WINDOW:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((300,100))

	def Prepare():
		self.screen.fill((255,255,255))
	def Reveal():
		pygame.display.update()
