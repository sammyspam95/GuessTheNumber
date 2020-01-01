import random


class StupidBot:

    def __init__(self, minimum, maximum, name):
        self.minimum = minimum
        self.maximum = maximum
        self.name = name

    def guess(self, silent="N", feedback=None):
        guess = random.randint(self.minimum, self.maximum)
        if silent == "N":
            print(self.name + ": guesses " + str(guess) + "!")
        return guess


class CleverBot(StupidBot):

    last_guess = 1
    feedback = None

    def get_feedback(self, feedback):
        if feedback in ['Higher', 'Lower']:
            self.feedback = feedback

    def guess(self, silent="N", feedback=None):
        self.get_feedback(feedback)
        if self.feedback is None:
            guess = super().guess("Y")
        if self.feedback == "Higher":
            self.minimum = self.last_guess
            guess = random.randint(self.last_guess, self.maximum)
        if self.feedback == "Lower":
            self.maximum = self.last_guess
            guess = random.randint(self.minimum, self.last_guess)
        self.last_guess = guess
        if silent == "N":
            print(self.name + ": guesses " + str(guess) + "!")
        return guess