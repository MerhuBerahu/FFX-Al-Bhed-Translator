
#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This program will translate Final Fantasy X 'Al Bhed' into english
"""


from colorama import Fore, Back, Style, init
init()

#TODO
# Add in errors, if letters no translatable
# print out translated in pink
# and errors print original input letters
# as purple

# Font Colors
WHITE = Fore.WHITE
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
MAGENTA = Fore.MAGENTA
LIGHT_RED = Fore.LIGHTRED_EX
CYAN = Fore.CYAN

primer = {",":",","!":"!","'":"'","?":"?",".":"."," ":" ","A":"E","B":"P","C":"S","D":"T","E":"I","F":"W","G":"K","H":"N","I":"U","J":"V","K":"G","L":"C","M":"L","N":"R","O":"Y","P":"B","Q":"X","R":"H","S":"M","T":"D","U":"O","V":"F","W":"Z","X":"Q","Y":"A","Z":"J"}


phrase = input("Type the al bhed phrase that you want to translate and hit 'Enter':-> ")

translation = []
"""
for all letters in 'phrase' check if theres a key in 'primer' and 
if so append 'translation' with the value
"""
try:
    for i in phrase.upper():
        for item,value in primer.items():
            if i == item:
                translation.append(value + " ")
except:
    print("error")
        

print(MAGENTA,"".join(str(x) for x in translation)) # Formatting to get rid of ' and ,

