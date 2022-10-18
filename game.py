##this is the number guessing game
import random

ai_num = random.randint(-100,100)

def game():
    print(ai_num)
    p1 = input("Your Guessing Number: ")
    p2 = int(p1) 
    if ai_num < 0: ##finding negative int
        if p2 > ai_num: ##player num bigger than ai num
            if p2 == ai_num:
                print("You got it right!!")
            elif (p2 - ai_num <= 5):
                print("SO FUCKING CLOSE!!!")
                return game()
            elif (p2 - ai_num <= 10):
                print("Very Close!!")
                return game()
            elif (p2 - ai_num <= 15):
                print("Close!")
                return game() 
            elif (p2 - ai_num <= 20):
                print("no!")
                return game()
            elif (p2 - ai_num <= 25):
                print("Further AWAY!!!")
                return game()
            else:
                print("SHIT!!!!!!")
                return game()
        else: ##player num less than ai num
            if p2 == ai_num:
                print("You got it right!!")
            elif (ai_num - p2 <= 5):
                print("SO FUCKING CLOSE!!!")
                return game()
            elif (ai_num - p2 <= 10):
                print("Very Close!!")
                return game()
            elif (ai_num - p2 <= 15):
                print("Close!")
                return game()
            elif (ai_num - p2 <= 20):
                print("no!")
                return game()
            elif (ai_num - p2 <= 25):
                print("Further AWAY!!!")
                return game()
            else:
                print("shit")
                return game()
    else: ##finding positive int
        if p2 > ai_num: ##player num bigger than ai num
            if p2 == ai_num:
                print("You got it right!!")
            elif (p2 - ai_num <= 5):
                print("SO FUCKING CLOSE!!!")
                return game()
            elif (p2 - ai_num <= 10):
                print("Very Close!!")
                return game()
            else:
                print("shit")
                return game()
        else: ##player num less than ai num
            if p2 == ai_num:
                print("You got it right!!")
            elif (ai_num - p2 <= 5):
                print("SO FUCKING CLOSE!!!")
                return game()
            elif (ai_num - p2 <= 10 or p2 - ai_num <= 10):
                print("Very Close!!")
                return game()
            else:
                print("shit")
                return game()                          

game()

