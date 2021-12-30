from pathlib import Path
import os
from Quiz import Quiz

class QuizMaker():
    def __init__(self):
        pass


    def get_all_capitals(self, states_data):
        all_capitals = []

        for state in states_data:
            all_capitals.append(state['capital'])

        return all_capitals


    def make_quiz_data(self, states_data, num_of_quizes):
        all_capitals = self.get_all_capitals(states_data)

        all_quizes = []

        for i in range(0, num_of_quizes):
            new_quiz = Quiz(states_data, all_capitals)
            all_quizes.append(new_quiz)

        return all_quizes


    def print_question_txt(self, idx, question_data):
        question_text = ''
        question_text += f'{idx}. What is the capital of {question_data.state_name}?\n'

        letters = ['a', 'b', 'c', 'd']

        for idx, choice in enumerate(question_data.choices):
            question_text += f'\t{letters[idx]}. {choice}\n'

        return question_text + '\n'



    def print_quiz_questions(self, quiz_data):
        all_questions = ''

        for idx, question in enumerate(quiz_data.questions):
            question_txt = self.print_question_txt(idx, question)
            all_questions += question_txt

        return all_questions



    def create_quiz_files(self, all_quiz_data):
        if (not Path('quizes').is_dir()):
            os.makedirs('quizes')

        for idx, quiz in enumerate(all_quiz_data):
            quiz_file = open(Path(Path.cwd(), 'quizes', f'quiz{idx}.txt'), 'w')
            quiz_file.write(self.print_quiz_questions(quiz))



    def print_quiz_answers(self, quiz_data):
        all_answers = ''

        for idx, question in enumerate(quiz_data.questions):
            all_answers += f'{idx}. {question.state_name} - {question.state_capital}\n'

        return all_answers



    def create_answer_files(self, quiz_data):
        if (not Path('answers').is_dir()):
            os.makedirs('answers')

        for idx, quiz in enumerate(quiz_data):
            answer_file = open(Path(Path.cwd(), 'answers', f'answer{idx}.txt'), 'w')
            answer_file.write(self.print_quiz_answers(quiz))
