import numpy

GREETINGS = ["Hello, World!",
             "Hola, Amigo!",
             "You've got to ask yourself one question: 'Do I feel lucky?'"]

def get_random_greeting():
    return numpy.random.choice(GREETINGS)

