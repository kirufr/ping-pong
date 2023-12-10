from pygame import *

width = 600
height = 500

window = display.set_mode((width, height))

background_color = (50, 50, 100)
clock  = time.Clock()

game_over = False
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, s):
        super().__init__()
        self.image = transform.scale(image.load(img), (w, h))
        self.speed = s

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
player_1 = GameSprite("racket.png", 30, 200, 50, 150, 4)
player_2 = GameSprite("racket.png", 520, 200, 50, 150, 4)


while game_over == False:
    for e in event.get():
        if e.type == QUIT:
            game_over = True

    window.fill(background_color)
    player_1.draw()
    player_2.draw()

    display.update()
    clock.tick(60)