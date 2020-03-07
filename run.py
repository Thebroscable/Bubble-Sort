import pygame, sys, random

pygame.init()
pygame.display.set_caption("Bubble sort")

clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))
tab = [[x, 60+(x-1)*30] for x in range(1, 24)]
font = {"16":pygame.font.Font("freesansbold.ttf", 16), "24":pygame.font.Font("freesansbold.ttf", 24)}
color = {"start":(100, 100, 100), "stop":(100, 100, 100)}
start_b = [False, 0, 0, 0]

def bubble(tab, start_b):

    xd = 5
    if start_b[1] <= len(tab) - 1 - start_b[3]:
        k = start_b[1]
        if tab[k] > tab[k + 1]:
            for n in range(30):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit(0)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        xd = button(color, screen, tab, 0, start_b)
                if xd == 5:
                    update(tab, start_b)
                    pygame.display.flip()
                    tab[k][1] += 1
                    tab[k+1][1] -= 1
            if xd == 5:
                tab[k], tab[k + 1] = tab[k + 1], tab[k]
        start_b[1] += 1

def draw(tab, font, start_b):

    if start_b[1] >= len(tab) - 1 - start_b[3]:
        start_b[1] = 0
        start_b[3] += 1
    if start_b[3] >= 22:
        color["stop"] = (255, 0, 0)
        color["start"] = (100, 100, 100)
        start_b[0] = False
        start_b[2] = 1

    for n in range(len(tab)):
        if (start_b[1] == n or start_b[1]+1 == n) and start_b[2] > 1 :
            pygame.draw.rect(screen, (255, 0, 0), (tab[n][1], 500, 20, -(tab[n][0]*20)))
            rend = font["16"].render("".join(str(tab[n][0])), True, (255, 0, 0))
        elif 23-start_b[3] <= n:
            pygame.draw.rect(screen, (100, 100, 100), (tab[n][1], 500, 20, -(tab[n][0] * 20)))
            rend = font["16"].render("".join(str(tab[n][0])), True, (0, 255, 0))
        else:
            pygame.draw.rect(screen, (0, 0, 0), (tab[n][1], 500, 20, -(tab[n][0]*20)))
            rend = font["16"].render("".join(str(tab[n][0])), True, (0, 0, 0))
        if tab[n][0] > 9:
            screen.blit(rend, (tab[n][1], 510))
        else:
            screen.blit(rend, (tab[n][1]+5, 510))

def menu(font):

    pygame.draw.line(screen, (0, 0, 0), (0, 1), (800, 1))
    pygame.draw.line(screen, (0, 0, 0), (0, 535), (800, 535))

    pygame.draw.rect(screen, color["start"], (100, 550, 100, 30))
    start = font["24"].render("START", True, (0, 0, 0))
    screen.blit(start, (110, 554))

    pygame.draw.rect(screen, color["stop"], (350, 550, 100, 30))
    stop = font["24"].render("STOP", True, (0, 0, 0))
    screen.blit(stop, (367, 554))

    pygame.draw.rect(screen, (100, 100, 100), (600, 550, 100, 30))
    reset = font["24"].render("RESET", True, (0, 0, 0))
    screen.blit(reset, (610, 554))

def stop(color, screen, tab, start_b):

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                temp = button(color, screen, tab, 1, start_b)
                if temp == 1:
                    run = False
        update(tab, start_b)
        pygame.display.flip()

def button(color, screen, tab, ifstop, start_b):

    mouse = pygame.mouse.get_pos()
    if mouse[0] >= 100 and mouse[0] <= 200 and start_b[2] >= 1:
        if mouse[1] >= 550 and mouse[1] <= 580:
            color["start"] = (0, 255, 0)
            color["stop"] = (100, 100, 100)
            start_b[0] = True
            start_b[2] = 2
            return 1
    elif mouse[0] >= 350 and mouse[0] <= 450 and ifstop == 0 and start_b[2] > 1:
        if mouse[1] >= 550 and mouse[1] <= 580:
            color["stop"] = (255, 0, 0)
            color["start"] = (100, 100, 100)
            start_b[0] = False
            stop(color, screen, tab, start_b)
            return 0
    elif mouse[0] >= 600 and mouse[0] <= 700:
        if mouse[1] >= 550 and mouse[1] <= 580:
            color["start"] = (100, 100, 100)
            color["stop"] = (255, 0, 0)
            for n in range(0, 430, 5):
                clock.tick(100)
                update(tab, start_b)
                pygame.draw.rect(screen, (0, 0, 0), (0, 0, n, 535))
                pygame.draw.rect(screen, (0, 0, 0), (800, 0, -n, 535))
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit(0)
            start_b[0] = False
            start_b[1] = 0
            start_b[2] = 1
            start_b[3] = 0
            temp = [tab[x][0] for x in range(23)]
            random.shuffle(temp)
            for n in range(23):
                tab[n][0] = temp[n]
                tab[n][1] = 60+n*30
            update(tab, start_b)
            return 0

def events(tab, start_b):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            button(color, screen, tab, 0, start_b)

def update(tab, start_b):

    screen.fill((255, 255, 255))
    draw(tab, font, start_b)
    menu(font)

while True:

    clock.tick(5)
    events(tab, start_b)

    update(tab, start_b)
    if start_b[0]:
        bubble(tab, start_b)
    pygame.display.flip()
