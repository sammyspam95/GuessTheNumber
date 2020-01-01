import random
import Bots

minimum = 1
maximum = 10000
r_number = random.randint(minimum, maximum)

found = False
feedback = None

guess_count = 0
guesses = []

bots = []


def get_feedback(guess):
    global feedback
    if guess < r_number:
        feedback = "Higher"
    if guess > r_number:
        feedback = "Lower"
    if guess == r_number:
        set_found()
        return "You found it!"
    return feedback


def record_guess(guess):
    guesses.append(guess)


def set_found():
    global found
    found = True


bot1 = Bots.StupidBot(minimum, maximum, "Stupid")
bots.append(bot1)
bot2 = Bots.StupidBot(minimum, maximum, "Stupid2")
bots.append(bot2)
bot3 = Bots.CleverBot(minimum, maximum, "Clever")
bots.append(bot3)

for bot in bots:
    found = False
    guess_count = 0
    feedback = None
    while not found:
        guess = bot.guess("Y", feedback)
        record_guess(guess)
        guess_count += 1
        get_feedback(guess)
    print(bot.name + " Attempts: " + str(guess_count))

