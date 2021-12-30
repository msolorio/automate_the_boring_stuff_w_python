from sys import argv
from QuizMaker import QuizMaker
from states_data import states_data

quiz_maker = QuizMaker()

num_of_quizes = int(argv[1])

quiz_data = quiz_maker.make_quiz_data(states_data, num_of_quizes)

quiz_maker.create_quiz_files(quiz_data)
quiz_maker.create_answer_files(quiz_data)
