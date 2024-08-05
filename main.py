from keyboard_input import *

class RPS:
    def __init__(self):
        points = int(input("which one do you need best of 3 or best of 5:"))
        user_input = input("Which will be your input method keyboard or mic(Type k for keyboard and m for mic)?:")

        if(user_input == 'k' and points == 3):
            while True:
                kb.call_everything()


rps = RPS()