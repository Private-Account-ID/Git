from pywhatkit import playonyt, text_to_handwriting, search, image_to_ascii_art
from random import random

def HandWrite(txt,  N = f"C:\\Users\\abc\Pictures\Handwritten\\{random()}.png"): # Syntax: Handwrite ********
    text_to_handwriting(txt[txt.index('write')+6:],N, (0,0,138))
    return N

def ImgToArt():                                         
    image_to_ascii_art(input('Enter Image Location:')) 
    return 'read pywhatkit_asciiart.txt file'

Play = lambda txt: playonyt(txt) 

Search = lambda txt: search(txt) 