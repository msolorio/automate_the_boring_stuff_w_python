from random import shuffle

class Question():
    def __init__(self, state_info, all_capitals):
        self.state_name = state_info['name']
        self.state_capital = state_info['capital']
        self.choices = self.get_choices(state_info['capital'], all_capitals)


    def get_choices(self, state_cap, all_capitals):
        all_caps_clone = all_capitals.copy()
        shuffle(all_caps_clone)
        choices = all_caps_clone[0:4]

        if (not state_cap in choices):
            choices[0] = state_cap
        
        shuffle(choices)

        return choices
