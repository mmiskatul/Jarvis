import asyncio
import os
import edge_tts
import pygame
import time

VOICE = "en-AU-WilliamNeural"


def remove_file(filename):
    for _ in range(3):
        try:
            if os.path.exists(filename):
                os.remove(filename)
            break
        except Exception as e:
            print(f"File remove error: {e}")
            time.sleep(0.2)


def play_audio(file_path):
    try:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.stop()
        pygame.mixer.quit()
        pygame.quit()

    except Exception as e:
        print(f"Audio play error: {e}")

