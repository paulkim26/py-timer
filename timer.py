import pygame
import time

#settings
time_limit = 60 #0-60 minutes
update_frequency = 0.03 #seconds, 0 = uncapped
font_path = "c:/users/<username>/appdata/local/microsoft/windows/fonts/<fontname>.otf" #path to font file
font_size = 300
screen_width = 1920
screen_height = 1080
screen_fullscreen = True

#initialize
pygame.init()
pygame.display.set_caption("Timer")
pygame.mouse.set_visible(False)
if screen_fullscreen:
    screen = pygame.display.set_mode((screen_width,screen_height), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((screen_width,screen_height))

#working variables
start = time.time()
ms_initial_constant = int(1000 * 60 * time_limit)
ms_initial = ms_initial_constant
ms_remaining = ms_initial_constant
run = True
state_play = False

#load font
font = pygame.font.Font(font_path, font_size)

#main
while run:
    #event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        #keyboard input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            run = False

        if keys[pygame.K_SPACE]:
            if state_play:
                #pause
                state_play = False
            else:
                #play
                state_play = True
                start = time.time()
                ms_initial = ms_remaining

        if keys[pygame.K_r]:
            #reset
            ms_remaining = ms_initial_constant
            state_play = False

        minutes_scan = 1
        if keys[pygame.K_LSHIFT]:
            #fast modifier
            minutes_scan = 3

        if keys[pygame.K_LEFT]:
            #rewind
            ms_remaining = ms_remaining + 1000 * 60 * minutes_scan
            if ms_remaining > ms_initial_constant:
                ms_remaining = ms_initial_constant
            state_play = False

        if keys[pygame.K_RIGHT]:
            #fast forward
            ms_remaining = ms_remaining - 1000 * 60 * minutes_scan
            if ms_remaining < 0:
                ms_remaining = 0
            state_play = False

    if state_play:
        #calculate elapsed time since start
        end = time.time()
        ms_remaining = int((end - start) * 1000)
        ms_remaining = ms_initial - ms_remaining
        if ms_remaining <= 0:
            ms_remaining = 0

    s_remaining = int(ms_remaining / 1000)
    m_remaining = int(s_remaining / 60)

    #calculate display time
    ms = ms_remaining % 1000
    s = s_remaining % 60
    m = m_remaining

    #pad digits with leading zeroes
    ms_pad = str(ms).rjust(3,'0')
    s_pad = str(s).rjust(2,'0')
    m_pad = str(m).rjust(2,'0')

    #print text
    text_str = "{}:{}:{}"
    text_str = text_str.format(m_pad,s_pad,ms_pad)
    text = font.render(text_str, True, (255,0,0))
    text_rect = text.get_rect(center=(screen_width/2, screen_height/2))

    #draw
    screen.fill((0,0,0)) #fill with black
    #screen.blit(text, (20,20,0,0))
    screen.blit(text, text_rect)
    pygame.display.flip()

    #exit
    #if ms_remaining <= 0:
    #    run = False

    #delay
    if update_frequency > 0:
        time.sleep(update_frequency) #seconds

pygame.quit()
