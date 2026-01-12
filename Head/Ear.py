import speech_recognition as sr
import os
import threading
from mtranslate import translate
from colorama import Fore,Style,init

init(autoreset=True)

def print_loop():
    while True:
        print(Fore.LIGHTGREEN_EX + "I am Listening ..... ",end="",flush=True)
        print(Style.RESET_ALL,end="",flush=True)
        print("",end="",flush=True)

def  trans_bengali_to_english(txt):
      english = translate(txt,"en-us")
      return english

def listen():
    rec = sr.Recognizer()
    rec.dynamic_transcription = False
    rec.energy_threshold =35000
    rec.dynamic_energy_adjustment_damping = 0.03
    rec.dynamic_energy_ratio =1.9
    rec.pause_threshold = 0.4
    rec.operation_timeout = None
    rec.pause_threshold =0.2
    rec.non_speaking_duration =0.3

    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source)
        while True:
            print(Fore.LIGHTGREEN_EX + "I am Listening ..... ", end="", flush=True)
            try:
                audio = rec.listen(source,timeout=None)
                print("\r"+Fore.LIGHTYELLOW_EX + "Got it , Recognizing...",end="",flush=True)
                recognized_txt =rec.recognize_google(audio).lower()
                if recognized_txt:
                        translated_txt =trans_bengali_to_english(recognized_txt)
                        print("\r"+Fore.BLUE + "Mr Miskat : "+translated_txt )
                else :
                    return ""
            except sr.UnknownValueError:
                recognized_txt = ""
            finally:
                print("\r",end="",flush=True)
            os.system("cls" if os.name == "nt" else "clear")
            #threding part
            listen_thread = threading.Thread(target=listen)
            print_thread = threading.Thread(target=print_loop())
            listen_thread.start()
            print_thread.start()
            listen_thread.join()
            print_thread.join()




listen()


