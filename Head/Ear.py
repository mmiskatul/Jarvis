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




