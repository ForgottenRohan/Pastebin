import string 
import random

def create_hash():
    alphabet = string.ascii_lowercase + string.digits + string.ascii_uppercase
    return ''.join(random.choices(alphabet, k=8))

