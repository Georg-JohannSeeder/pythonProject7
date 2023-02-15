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
bg = pygame.image.load("imgf/bg_shop.jpg")
screen.blit(bg,[0,0])
sel = pygame.image.load("imgf/seller.png")
sel = pygame.transform.scale(sel,[250,300])
screen.blit(sel,[60,150])
cht = pygame.image.load("imgf/chat.png")
cht = pygame.trasnform.scale(cht,[250,200])
screen.blit(cht,[200,75])
font = pygame.font.Font(pygame.font.match_font('Arial'), 25)
text = font.render("Georg-Johann Seeder", True, [255, 255, 255])
text_width = text.get_rect().width
text_height = text.get_rect().height
screen.blit(text, [225, 150])
pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()
