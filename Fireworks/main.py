import pygame, random
import firework
import settings as st

pygame.init()

# Setting Window
window = pygame.display.set_mode((st.WIDTH, st.HEIGHT), 0, 32)
pygame.display.set_caption("Fireworks")
isExit = False

# Setting FPS
fpsClock = pygame.time.Clock()
fireworks = []

while not isExit:
    window.fill((0, 0, 0, 255))

    # Event Controler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isExit = True

    # Apply Fireworks
    if random.random() < 0.2:
        fireworks.append(firework.Firework())
    for fw in range(fireworks.__len__() - 1, -1, -1):
        fireworks[fw].update()
        fireworks[fw].show(window)
        if fireworks[fw].done():
            del fireworks[fw:fw+1]
    print(fireworks.__len__())

    # FPS
    fpsClock.tick(st.FPS)
    pygame.display.update()

pygame.quit()
quit()