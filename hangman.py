from hangmanArt import logo
from hangmanArt import stages
from hangmanList import wordList
import random
def main():
    print(logo)
    chosen=random.choice(wordList)
    print(chosen)
    word_len=len(chosen)
    display=[]
    for i in range(word_len):
        display+='_'
    print(display)
    lives=6
    end_of_game=False
    while not end_of_game:
        letter=input()
        print(end_of_game)
        for i in range(word_len):
            if letter==chosen[i]:
                display[i]=letter
        print(display)
        if letter not in chosen:
            lives=lives-1
        if lives==0:
            end_of_game=True
        if '_' not in display:
            end_of_game=True
        print(stages[lives])
    print(display)
main()