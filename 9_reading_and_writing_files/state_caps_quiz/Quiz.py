from random import shuffle
from Question import Question

class Quiz():
    def __init__(self, states_data, all_capitals):
        self.questions = self.get_questions(states_data, all_capitals)

    def get_questions(self, states_data, all_capitals):
        states_data_clone = states_data.copy()
        shuffle(states_data_clone)

        questions = []

        for state in states_data_clone:
            questions.append(Question(state, all_capitals))

        return questions