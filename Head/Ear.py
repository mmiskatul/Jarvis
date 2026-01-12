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




