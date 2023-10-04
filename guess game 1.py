#!/usr/bin/env python

import random

def main():
    """Start a music genre guessing game."""
    print("Guess music genre!")
    
    music=[
        "pop",
        "country",
        "hip hop",
        "rock",
        "classic",
        "popular"
        ]
    x = random.choice(music)
    guess = None
    
    for trials in range(5):      
        guess = str(input("\nWhat music genre am I thinking right now?"))
        
        if x == guess:
            print(f"Congratulations! you guessed the number ({x}) in {trials} trials.")
            break
        else:
            print("Oops! That's not correct. Try again")
            
    else:
        print("Sorry, you've run out of trials. The secret number was ",x)                  
    
main()