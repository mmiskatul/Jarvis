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


