# TODO 1: Create a question class
class Question:  # So you actually shouldn't put "()" when defining a class

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def __repr__(self):
        return f"Question(text='{self.text}', answer='{self.answer}')"