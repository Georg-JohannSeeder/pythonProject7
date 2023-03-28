import pygame
pygame.init()
#ekraani seaded
screen=pygame.display.set_mode([640,480])
pygame.display.set_caption("Lisaülesanne 2")
screen.fill([204, 255, 204])
#lisame teksti
font = pygame.font.Font(None, 30)
text = font.render("Hello PyGame", True, [0,0,0])
screen.blit(text, [200,200])
#Lisame pildid
bg = pygame.image.load("bg_shop.jpg")
screen.blit(bg,[0,0])
sel = pygame.image.load("seller.jpg")
sel = pygame.transform.scale(sel,[250,300])
screen.blit(sel,[60,150])
cht = pygame.image.load("chat.jpg")
cht = pygame.transform.scale(cht,[250,200])
screen.blit(cht,[200,75])
font = pygame.font.Font(pygame.font.match_font('Arial'), 25)
text = font.render("Georg-Johann Seeder", True, [255, 255, 255])
text_width = text.get_rect().width
text_height = text.get_rect().height
screen.blit(text, [225, 150])
tort = pygame.image.load('tort.jpg')
tort = pygame.transform.scale(tort, [120, 70])
screen.blit(tort,[330,220])

logo = pygame.image.load('VIKK logo.png')
logo = pygame.transform.scale(logo, [200, 75])
screen.blit(logo, [10, 10])

mook = pygame.image.load('Mõõk.png')
mook = pygame.transform.scale(mook, [90,100])
screen.blit(mook, [540,150])

pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if running == False:
      pygame.quit()
