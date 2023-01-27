import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Ülesanne 2")
screen.fill([204, 255, 204])
#lisame teksti
font = pygame.font.Font(None, 30)
text = font.render("Hello PyGame", True, [0,0,0])
screen.blit(text, [200,200])
#Lisame pildid
bg = pygame.image.load("bg_shop.png")
bg = pygame.image.load("seller.png")
bg = pygame.image.load("chat.png")
screen.blit(bg,[0,0])   
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()