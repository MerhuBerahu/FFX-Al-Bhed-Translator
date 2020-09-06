
#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module's deals Combat. Reading in the character, checking 
their stats and that of the enemy, then doing the combat math
"""

primer = {" ":" ","A":"E","B":"P","C":"S","D":"T","E":"I","F":"W","G":"K","H":"N","I":"U","J":"V","K":"G","L":"C","M":"L","N":"R","O":"Y","P":"B","Q":"X","R":"H","S":"M","T":"D","U":"O","V":"F","W":"Z","X":"Q","Y":"A","Z":"J"}


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
        

print("".join(str(x) for x in translation)) # Formatting to get rid of ' and ,

