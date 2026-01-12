import os
import threading
import speech_recognition as sr
from mtranslate import translate
from colorama import Fore, Style, init

init(autoreset=True)

listening_event = threading.Event()


def print_loop():
    """Print listening status only when actively listening."""
    while True:
        listening_event.wait()
        print(Fore.LIGHTGREEN_EX + "🎧 Listening...", flush=True)
        listening_event.clear()


def trans_bengali_to_english(text):
    return translate(text, "en-us")


def listen():
    recognizer = sr.Recognizer()

    recognizer.dynamic_transcription = False
    recognizer.energy_threshold = 35000
    recognizer.dynamic_energy_adjustment_damping = 0.03
    recognizer.dynamic_energy_ratio = 1.9
    recognizer.operation_timeout = None
    recognizer.pause_threshold = 0.3
    recognizer.non_speaking_duration = 0.2

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)

        while True:
            listening_event.set()

            try:
                audio = recognizer.listen(source)
                print(Fore.LIGHTYELLOW_EX + "🧠 Recognizing...")

                recognized_text = recognizer.recognize_google(audio).lower()

                if recognized_text:
                    translated_text = trans_bengali_to_english(recognized_text)
                    print(Fore.BLUE + "Mr Miskat: " + translated_text)

            except sr.UnknownValueError:
                print(Fore.RED + "❌ Could not understand")

            os.system("cls" if os.name == "nt" else "clear")


# Threads
listen_thread = threading.Thread(target=listen, daemon=True)
print_thread = threading.Thread(target=print_loop, daemon=True)

listen_thread.start()
print_thread.start()

listen_thread.join()
print_thread.join()
