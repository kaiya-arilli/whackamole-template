import pygame
import random


def main():
   try:
       pygame.init()
       # You can draw the mole with this snippet:
       # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
       mole_image = pygame.image.load("mole.png")
       screen = pygame.display.set_mode((640, 512))
       mole_x, mole_y = 0,0
       clock = pygame.time.Clock()
       running = True


       while running:
           screen.blit(mole_image, mole_image.get_rect(topleft=(0,0)))
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   running = False
               elif event.type == pygame.MOUSEBUTTONDOWN:
                   mouse_x, mouse_y = event.pos
                   mole_rect = pygame.Rect(mole_x, mole_y, 32, 32)
                   if mole_rect.collidepoint(mouse_x, mouse_y):
                       mole_x = random.randrange(0, 640, 32)
                       mole_y = random.randrange(0, 512, 32)
           screen.fill("pink")


           # draw grid lines
           for x in range(0, 640, 32):
               pygame.draw.line(screen, "hot pink", (x, 0), (x, 512))
           for y in range(0, 512, 32):
               pygame.draw.line(screen, "hot pink", (0, y), (640, y))
           screen.blit(mole_image, (mole_x, mole_y))
           pygame.display.flip()
           clock.tick(60)
   finally:
       pygame.quit()


if __name__ == "__main__":
   main()

