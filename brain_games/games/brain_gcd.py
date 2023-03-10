from random import randint
import math


GAME_RULE = 'Find the greatest common divisor of given numbers.'


num1 = randint(0, 50)
num2 = randint(0, 50)


def get_question_and_answer():
    correct_answer = math.gcd(num1, num2)
    question = f'{num1} {num2}'
    return str(correct_answer), question
