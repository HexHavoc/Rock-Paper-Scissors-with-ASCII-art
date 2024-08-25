import random
import time
import sys
from ascii_art import *

class Keyboard:

    def __init__(self):
        self.computer_point = 0
        self.user_point = 0
        self.pick_list = ['r','p','s','r','p','s','r','p','s']
    
    def computer_selection(self):
        self.computer_choice = random.choice(self.pick_list)


    def user_selection(self):
        self.user_choice = input("Typer r for rock, s for scissors, p for paper:")



    def countdown(self):
        sys.stdout.write("Rock ")
        sys.stdout.flush()
        time.sleep(0.5)

        sys.stdout.write("Paper ")
        sys.stdout.flush()
        time.sleep(0.5)

        sys.stdout.write("Scissor ")
        sys.stdout.flush()
        time.sleep(0.5)

        sys.stdout.write("Shoot!! ")
        sys.stdout.flush()
        time.sleep(0.5)

        print()

    def point_checking(self):
        if(self.computer_point == 5):
            print("COMPUTER WON THE MATCH!!!\n")
            quit_choice = input("IF YOU WANT TO CONTINUE PRESS c or PRESS e TO EXIT")

            if(quit_choice == 'c'):
                pass

            else:
                print("THANKS FOR PLAYING SEE YA NEXT TIME :) \n")
                sys.exit()

        if(self.user_point == 5):
            print("USER WON THE MATCH!!!\n")
            if(quit_choice == 'c'):
                pass


            else:
                print("THANKS FOR PLAYING SEE YA NEXT TIME :) \n")
                sys.exit() 



    def logic_and_printing(self):
        if(self.computer_choice == self.user_choice):
            print()
            print("DRAW!\n")


                            

        elif(self.computer_choice == 'r' and self.user_choice == 's'):
            print("Computer chose ROCK")
            print(rock_ascii)
            print()

            print("User chose SCISSORS")
            print(scissor_ascii)
            print()

            print("COMPUTER WINS!!!")
            self.computer_point += 1
            print()
            print(f"COMPUTER-{self.computer_point}:USER-{self.user_point}")
            print()

        elif(self.computer_choice == 's' and self.user_choice == 'r'):
            print("Computer chose SCISSORS")
            print(scissor_ascii)
            print()

            print("User chose ROCK")
            print(rock_ascii)
            print()

            print("USER WINS!!!")
            self.user_point += 1
            print()
            print(f"COMPUTER-{self.computer_point}:USER-{self.user_point}")
            print()


        elif(self.computer_choice == 'p' and self.user_choice == 'r'):
            print("Computer chose PAPER")
            print(paper_ascii)
            print()

            print("User chose ROCK")
            print(rock_ascii)
            print()

            print("COMPUTER WINS!!!")
            self.computer_point += 1
            print()
            print(f"COMPUTER-{self.computer_point}:USER-{self.user_point}")
            print()

        
        elif(self.computer_choice == 'r' and self.user_choice == 'p'):
            print("Computer chose ROCK")
            print(rock_ascii)
            print()

            print("User chose PAPER")
            print(paper_ascii)
            print()

            print("USER WINS!!!")
            self.user_point += 1
            print()
            print(f"COMPUTER-{self.computer_point}:USER-{self.user_point}")
            print()

        elif(self.computer_choice == 's' and self.user_choice == 'p'):
            print("Computer chose SCISSORS")
            print(scissor_ascii)
            print()

            print("User chose PAPER")
            print(paper_ascii)
            print()

            print("COMPUTER WINS!!!")
            self.computer_point += 1
            print()
            print(f"COMPUTER-{self.computer_point}:USER-{self.user_point}")
            print()

        elif(self.computer_choice == 'p' and self.user_choice == 's'):
            print("Computer chose PAPER")
            print(paper_ascii)
            print()

            print("User chose SCISSORS")
            print(scissor_ascii)
            print()

            print("USER WINS!!!")
            self.user_point += 1
            print()
            print(f"COMPUTER-{self.computer_point}:USER-{self.user_point}")
            print()




    def call_everything(self):
        self.point_checking()
        self.computer_selection()
        self.user_selection()
        self.countdown()
        self.logic_and_printing()


kb = Keyboard()