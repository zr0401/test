from reply import reply
from response import response
name = input("What is your name? ")
question = input("Hi " + name + ", do you want to feel healthy and do some exercise? ")

while True:
    if "yes" in question.lower() or "yeah" in question.lower() or "sure" in question.lower():
        print(reply())
        break
    elif "no" in question.lower() or "nah" in question.lower():
        print(response())
        break
    else:
        print("I do not understand your answer. (Answer with yes or no)")
        question = input("Do you want to feel healthy and do some exercise? ")