import pygame
import pygame_gui

pygame.init()
screen = pygame.display.set_mode((640, 480))
manager = pygame_gui.UIManager((640, 480))

slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect((250, 250), (250, 50)),
            start_value=50,
            value_range=(0, 100),
            manager=manager
        )

clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        manager.process_events(event)

    manager.update(60)

    screen.fill((255, 255, 255))
    manager.draw_ui(screen)

    pygame.display.flip()
