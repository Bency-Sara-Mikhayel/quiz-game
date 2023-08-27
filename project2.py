#quiz game
import time
class Quiz:
    def __init__(self):
        self.score=0
    def question(self,qstn,option,crct_ans):
        print(qstn)
        for option in option:
            print(option)
        start_time=time.time()
        answer=input("enter your answer:")
        end_time=time.time()
        if end_time - start_time <=10:
            if answer==crct_ans:
                print('correct answer')
                self.score+=1
            else:
                print('wrong answer')
        else:
            print("Time's Up")
def play_quiz():
    name = input('Enter your name: ')
    print(f'HELLO! {name}, Welcome to the computer quiz!')

    play = input('Are you ready to play the game? (Type yes to continue / no to exit): ')

    if play.lower() == 'no':
        print('Thank you for your time')
    else:
        print("Let's start")
        quiz=Quiz()
        questions=[("Q1: Who is known as the father of the computer?",["a) Bill Gates", "b) Charles Babbage", "c) James Gosling"], "b"),
                ("Q2: What is the brain of the computer?", ["a) RAM", "b) GPU", "c) CPU"], "c"),
                ("Q3: What does CPU stand for?", ["a) Central Processing Unit", "b) Control Processing Unit","c) Computer Programming Unit"], "a"),
                ("Q4: What does RAM stand for?", ["a) Random Access Memory", "b) Read-Only Memory", "c) Readable "], "a")]
        for qstn,option,crct_ans in questions:
            quiz.question(qstn,option,crct_ans)
            print()
        print(f'You scored {quiz.score} out of {len(questions)}')

play_quiz()


          


