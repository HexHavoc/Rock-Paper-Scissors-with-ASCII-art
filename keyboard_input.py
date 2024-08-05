import random
import time
import sys
from ascii_art import *

class Keyboard:

    def __init__(self):
        self.computer_point = 0
        self.user_point = 0
        self.pick_list = ['r','p','s','r','p','s']
    
    def computer_selection(self):
        self.computer_choice = random.choice(self.pick_list)


    def user_selection(self):
        self.user_choice = input("Typer r for rock, s for scissors, p for paper:")



    def countdown(self):
        sys.stdout.write("Rock ")
        sys.stdout.flush()
        time.sleep(1)

        sys.stdout.write("Paper ")
        sys.stdout.flush()
        time.sleep(1)

        sys.stdout.write("Scissor ")
        sys.stdout.flush()
        time.sleep(1)

        sys.stdout.write("Shoot!! ")
        sys.stdout.flush()
        time.sleep(1)


    def logic_and_printing(self):

        if(self.computer_choice == self.user_choice):
            print("DRAW!\n")

        elif(self.computer_choice == 'r' and self.user_choice == 's'):
            print("Computer chose ROCK")
            print(rock_ascii)
            print()

            print("User chose SCISSORS")
            print(scissor_ascii)
            print()

            print("COMPUTER WINS!!!")
            print()

        elif(self.computer_choice == 's' and self.user_choice == 'r'):
            print("Computer chose SCISSORS")
            print(scissor_ascii)
            print()

            print("User chose ROCK")
            print(rock_ascii)
            print()

            print("USER WINS!!!")
            print()


        elif(self.computer_choice == 'p' and self.user_choice == 'r'):
            print("Computer chose PAPER")
            print(paper_ascii)
            print()

            print("User chose ROCK")
            print(rock_ascii)
            print()

            print("COMPUTER WINS!!!")
            print()

        
        elif(self.computer_choice == 'r' and self.user_choice == 'p'):
            print("Computer chose ROCK")
            print(rock_ascii)
            print()

            print("User chose PAPER")
            print(rock_ascii)
            print()

            print("USER WINS!!!")
            print()

        elif(self.computer_choice == 's' and self.user_choice == 'p'):
            print("Computer chose SCISSORS")
            print(scissor_ascii)
            print()

            print("User chose PAPER")
            print(paper_ascii)
            print()

            print("COMPUTER WINS!!!")
            print()

        elif(self.computer_choice == 'p' and self.user_choice == 's'):
            print("Computer chose PAPER")
            print(paper_ascii)
            print()

            print("User chose SCISSORS")
            print(scissor_ascii)
            print()

            print("USER WINS!!!")
            print()


    def call_everything(self):
        self.computer_selection()
        self.user_selection()
        self.countdown()
        self.logic_and_printing()


kb = Keyboard()