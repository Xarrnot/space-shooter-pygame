import pygame
import sys
import socket
import math
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True           


class button():
    def __init__(self, image,x,y):
        self.testimage = pygame.image.load("button.png")
        self.image = pygame.transform.scale(self.testimage,(500,500))
        self.rect = self.image.get_rect()
        self.rect.move_ip(350,150)
    def draw(self):
        screen.blit(self.image, self.rect)

class player():
    def __init__(self):
        self.rect = pygame.Rect(50,50,50,50)
        self.image = pygame.image.load("ship.png").convert_alpha()
        self.rotateimage = pygame.image.load("ship.png").convert_alpha()
        self.speed = 500
        self.jumping = False
        self.jumpheight = 70
        self.vel = self.jumpheight
        self.gravity = 5
        self.mouse_x,self.mouse_y = pygame.mouse.get_pos()
        self.x = self.rect.y
        self.y = self.rect.x
        self.MY_CUSTOM_EVENT = pygame.USEREVENT + 1
        self.MY_time_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.MY_CUSTOM_EVENT, 7000)
        pygame.time.set_timer(self.MY_time_EVENT, 7000)
        self.time = pygame.time.get_ticks()
        self.shoot = False
    def draw(self):
        pass    
    def move(self):
        keys = pygame.key.get_pressed()
        dt = clock.tick(60) / 1000
        if keys[pygame.K_SPACE]:
            self.shoot = True
        if keys[pygame.K_LSHIFT]:
            for event in pygame.event.get():
                if event.type == self.MY_CUSTOM_EVENT:
                    if event.type == self.MY_time_EVENT:
                        
                        print("Work")
                        self.speed = 800 
                else:
                    self.speed = 100
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    pass            
        if keys[pygame.K_a]:
            self.rect.x -= self.speed * dt
        if keys[pygame.K_d]:
            self.rect.x += self.speed * dt
            
        if keys[pygame.K_w]:
            self.rect.y -= self.speed * dt
        if keys[pygame.K_s]:
            self.rect.y += self.speed * dt
    def jump(self):
        pass
    
class bullets():
    def __init__(self,x,y):
        self.image = pygame.image.load("laserBullet.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        self.y = self.rect.y
        self.rect.topleft = 100,50
        self.speed = 1
        
    def shoot(self):
        screen.blit(self.image,self.rect)
        self.rect.center = player1.rect.center
    def move(self):
        pass
    
    def draw(self):
        pass
        
    bullet_group = pygame.sprite.Group()
playbutton1 = button("button.png",4000,4000)
quitbutton = button("button.png",4000,4000)
image1  = pygame.image.load("button.png")
rect1 = image1.get_rect()
red = 255,0,0
mouse_pos = pygame.mouse.get_pos()
mouse_rect_size = 20
mouse_rect = pygame.Rect(0, 0, mouse_rect_size, mouse_rect_size)
player1 = player()
player1.rect.topleft = 0,500
ground_rect = pygame.Rect(1000,1000,1000,1000)
ground_rect.topleft = 0,550


def main_menu():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        mouse_pos = pygame.mouse.get_pos()
        mouse_rect.topleft = mouse_pos
        mouseaction = pygame.mouse.get_pressed()[0]
        if playbutton1.rect.colliderect(mouse_rect):
            if mouseaction == True:
                game_loop()
                mouseaction == False
        playbutton1.draw()
        quitbutton.draw()
        quitbutton.rect.topleft = 350,300
        
        if quitbutton.rect.colliderect(mouse_rect):
            if mouseaction == True:
                print("hello")
        pygame.display.flip()

        clock.tick(60)
        
        
        
def game_loop():
    import pygame


    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill("black")
        pygame.draw.rect(screen,(153,0,153),ground_rect)
        player1.draw()
        player1.move()
        if ground_rect.colliderect(player1.rect):
            player1.rect.y -= player1.gravity
            player1.jump()
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mousepos = pygame.mouse.get_pos()
        dx = mouse_x - player1.rect.centerx
        dy = mouse_y - player1.rect.centery
        angle = math.degrees(math.atan2(-dy, dx)) 
        rotated_image = pygame.transform.rotate(player1.image, angle)
        rotated_rect = rotated_image.get_rect(center=player1.rect.center)
    
        
        screen.blit(rotated_image, (rotated_rect.topleft))
        pygame.display.flip()

main_menu()
pygame.quit()