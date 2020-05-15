# -*- coding: utf-8 -*-
"""
Created on Fri May 15 22:53:45 2020

@author: P.LohithViswa
"""

import speech_recognition as sr

r = sr.Recognizer()
print("1.Convert speech to text")
print("2.Convert audio file to text")
option=int(input("Choose option : "))

def speak():
 with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source,timeout=1,phrase_time_limit=10)
    print('Done, Please wait while we are processing what you said...')
    try:
        text = r.recognize_google(audio)
        print("Speaker said : {}".format(text))
    except:
        print("Sorry we could not recognize what you said. You can try again.")

def recording(audio_file):
 with sr.AudioFile(audio_file) as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source,timeout=1,phrase_time_limit=10)
    print('Done, Please wait while we are processing what you said...')
    try:
        text = r.recognize_google(audio)
        print("Audio in Recording is : {}".format(text))
    except:
        print("Sorry we could not recognize what you said. You can try again.")
        


if option==1 :
 speak()
elif option==2:
 print("File must be in any of the following format PCM WAV, AIFF/AIFF-C, or Native FLAC")
 audio_file=input("Location of Audio file:")
 recording(audio_file)
else:
 print("choose valid option")
 
