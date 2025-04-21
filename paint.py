import pygame

pygame.init() # Initialize pygame

painting = []
timer = pygame.time.Clock()
fps = 60 # Set Frames per second
activeColor = (0, 0, 0)
activeShape = 0
w = 800 # Set Window width
h = 600 # Set Window height

screen = pygame.display.set_mode([w, h]) # Set Screen
pygame.display.set_caption("Paint") # Set Window Title

def drawDisplay():
    pygame.draw.rect(screen, (229,255,204), [0, 0, w, 86]) #Display
    pygame.draw.line(screen, 'gray', [0, 85], [w, 85]) #Line separator
    rect = [pygame.draw.rect(screen, (96, 96, 96), [10, 10, 70, 70]), 0]
    pygame.draw.rect(screen, 'white', [20, 20, 50, 50])
    circ = [pygame.draw.rect(screen, (96, 96, 96), [100, 10, 70, 70]), 1]
    pygame.draw.circle(screen, 'white', [135, 45], 30)
    triangle = [pygame.draw.rect(screen, (96, 96, 96), [200, 10, 70, 70]), 2]
    pygame.draw.polygon(screen, 'white', ((235,20),(260,70),(210,70)))
    rhomb = [pygame.draw.rect(screen, (96, 96, 96), [300, 10, 70, 70]), 3]
    pygame.draw.polygon(screen, 'white', ((335,15),(360,45),(335,75),(310,45)))
    right_triangle = [pygame.draw.rect(screen, (96, 96, 96), [400, 10, 70, 70]), 4]
    pygame.draw.polygon(screen, 'white', ((410,20),(410,70),(460,70)))
    #Colors
    blue = [pygame.draw.rect(screen, (0, 0, 255), [w - 35, 10, 25, 25]), (0, 0, 255)]
    red = [pygame.draw.rect(screen, (255, 0, 0), [w - 35, 35, 25, 25]), (255, 0, 0)]
    green = [pygame.draw.rect(screen, (0, 255, 0), [w - 60, 10, 25, 25]), (0, 255, 0)]
    yellow = [pygame.draw.rect(screen, (255, 255, 0), [w - 60, 35, 25, 25]), (255, 255, 0)]
    black = [pygame.draw.rect(screen, (0, 0, 0), [w - 85, 10, 25, 25]), (0, 0, 0)]
    purple = [pygame.draw.rect(screen, (255, 0, 255), [w - 85, 35, 25, 25]), (255, 0, 255)]

    eraser = [pygame.draw.rect(screen, (253, 166, 215), [w - 300, 20, 50, 50]), (255, 255, 255)] #Eraser

    return [blue, red, green, yellow, black, purple, eraser], [rect, circ, triangle, rhomb, right_triangle]
def drawPaint(paints):
    for paint in paints:
        if paint[2] == 1:
            pygame.draw.circle(screen, paint[0], paint[1], 15)
        elif paint[2] == 0:
            pygame.draw.rect(screen, paint[0], [paint[1][0]-15, paint[1][1]-15, 30, 30])
        elif paint[2] == 2:
            pygame.draw.polygon(screen, paint[0], ((paint[1][0]-15, paint[1][1]+15), (paint[1][0], paint[1][1]-15), (paint[1][0]+15, paint[1][1]+15)))
        elif paint[2] == 3:
            pygame.draw.polygon(screen, paint[0], ((paint[1][0], paint[1][1]-20), (paint[1][0]+15, paint[1][1]), (paint[1][0], paint[1][1]+20),(paint[1][0]-15, paint[1][1])))
        elif paint[2] == 4:
            pygame.draw.polygon(screen, paint[0], ((paint[1][0]-10, paint[1][1]-20), (paint[1][0]+20, paint[1][1]+10), (paint[1][0]-10, paint[1][1]+10)))
def draw():
    global activeColor, activeShape, mouse
    if mouse[1] > 100:
        if activeShape == 0:
            pygame.draw.rect(screen, activeColor, [mouse[0]-15, mouse[1]-15, 30, 30])
        if activeShape == 1:
            pygame.draw.circle(screen, activeColor, mouse, 15)
        if activeShape == 2:
            pygame.draw.polygon(screen, activeColor, ((mouse[0]-15, mouse[1]+15), (mouse[0], mouse[1]-15), (mouse[0]+15, mouse[1]+15)))
        if activeShape == 3:
            pygame.draw.polygon(screen, activeColor, ((mouse[0], mouse[1]-20), (mouse[0]+15, mouse[1]), (mouse[0], mouse[1]+20),(mouse[0]-15, mouse[1])))
        if activeShape == 4:
            pygame.draw.polygon(screen, activeColor, ((mouse[0]-10, mouse[1]-20), (mouse[0]+20, mouse[1]+10), (mouse[0]-10, mouse[1]+10)))
run = True
while run:
    timer.tick(fps) #FPS
    screen.fill('white') # Fill Screen
    colors, shape = drawDisplay() # Draw Display

    mouse = pygame.mouse.get_pos() # Get Mouse Position
    draw()
    click = pygame.mouse.get_pressed()[0] # Get Mouse Button Pressed
    if click and mouse[1] > 100:
        painting.append((activeColor, mouse, activeShape)) # Add Mouse Position to List
    drawPaint(painting)

    for event in pygame.event.get(): # Set quit event
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                painting = []
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in colors:
                if i[0].collidepoint(event.pos):
                    activeColor = i[1]
            for i in shape:
                if i[0].collidepoint(event.pos):
                    activeShape = i[1]
    pygame.display.flip() # Update Screen
pygame.quit()