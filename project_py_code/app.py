from Q import *

question_list=[ 
    "What colour are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What colour are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What colour are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

questions_object = [
    Question(question_list[0], "a"),
    Question(question_list[1], "c"),
    Question(question_list[2], "b"),
]


def run_test(questions_object):
    score = 0
    for x in questions_object:
        answer = input(f" {x.prompt} \n Enter answer : ")
        if answer == x.answer:
            score += 1

    print(f" You have corrected  {str(score)}/{str(len(questions_object))}")

run_test(questions_object)


