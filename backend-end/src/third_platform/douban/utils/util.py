import random
import time
import string


def generate_random_string():
    current_time = int(time.time())
    random.seed(current_time)
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choices(characters, k=11))
    return random_string
