from keyboard_input import *

class RPS:
    def __init__(self):
        print("WELCOME TO Rock,Paper,Scissors game made by HexHavoc!\n")
        print("FIRST TO REACH 5 POINTS WINS!\n")
        user_input = input("Which will be your input method keyboard or mic(Type k for keyboard and m for mic)?:")
        print()

        
        if(user_input == 'k'):
                while True:
                    kb.call_everything()
                


rps = RPS()