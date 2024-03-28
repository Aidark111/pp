import pygame

pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((960, 600))
done = False
songs = ['/Users/sansyzbaidarkhan/Desktop/pp2/music/Like That [TubeRipper.com].mp3',
         '/Users/sansyzbaidarkhan/Desktop/pp2/music/Tyler The Creator - She (Feat. Frank Ocean) - Goblin (HQ) [TubeRipper.com].mp3',
         '/Users/sansyzbaidarkhan/Desktop/pp2/music/Billie Eilish - What Was I Made For (Official Lyric Video) [TubeRipper.com].mp3',
         '/Users/sansyzbaidarkhan/Desktop/pp2/music/Everything In Its Right Place.mp3']
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
i = 0
a = True
background_image = pygame.image.load("/Users/sansyzbaidarkhan/Desktop/pp2/music/d3ZXHLsxqw.jpg.webp")
background_rect = background_image.get_rect()

while not done:
    screen.blit(background_image, background_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                i = (i + 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
            elif event.key == pygame.K_LEFT:
                i = (i - 1) % len(songs)
                pygame.mixer.music.load(songs[i])
                pygame.mixer.music.play()
            elif event.key == pygame.K_SPACE:
                if a:
                    pygame.mixer.music.pause()
                    a = False
                else:
                    pygame.mixer.music.unpause()
                    a = True

    pygame.display.flip()
