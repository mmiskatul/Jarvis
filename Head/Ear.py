import threading
import speech_recognition as sr
from mtranslate import translate
from colorama import Fore, init

init(autoreset=True)

listening_event = threading.Event()


def print_loop():
    while True:
        listening_event.wait()
        print(Fore.LIGHTGREEN_EX + "🎧 Listening...")
        listening_event.clear()


def trans_bengali_to_english(text):
    return translate(text, "en-us")


def recognize_with_timeout(recognizer, audio, result_holder):
    try:
        text = recognizer.recognize_google(audio, language="bn-BD").lower()
        result_holder["text"] = text
    except:
        result_holder["text"] = None


def listen():
    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 3000
    recognizer.dynamic_energy_threshold = True
    recognizer.pause_threshold = 1.0
    recognizer.non_speaking_duration = 0.6

    with sr.Microphone() as source:
        print(Fore.CYAN + "🎤 Calibrating microphone...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print(Fore.GREEN + "✅ Ready to listen\n")

        while True:
            listening_event.set()

            try:
                audio = recognizer.listen(
                    source,
                    phrase_time_limit=3
                )

                print(Fore.LIGHTYELLOW_EX + "🧠 Recognizing...")

                result_holder = {"text": None}
                recog_thread = threading.Thread(
                    target=recognize_with_timeout,
                    args=(recognizer, audio, result_holder)
                )

                recog_thread.start()
                recog_thread.join(timeout=15.0)  # ⏱️ MAX WAIT TIME

                if recog_thread.is_alive():
                    print(Fore.RED + "⚠ Recognition took too long, skipped\n")
                    continue

                if result_holder["text"]:
                    translated = trans_bengali_to_english(result_holder["text"])
                    print(Fore.BLUE + "Mr Miskat:", translated, "\n")
                else:
                    print(Fore.RED + "❌ Could not understand\n")

            except Exception as e:
                print(Fore.RED + f"⚠ Error: {e}\n")


# Threads
listen_thread = threading.Thread(target=listen, daemon=True)
print_thread = threading.Thread(target=print_loop, daemon=True)

listen_thread.start()
print_thread.start()

listen_thread.join()
print_thread.join()
