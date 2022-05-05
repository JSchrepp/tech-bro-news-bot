from random import random, randint, choice
from loader import read_lines

def get_percent() -> str:
    if random() > 0.15:
        return f"{randint(0,100)}%"
    
    return choice(read_lines("special_percentages"))

def get_money() -> str:
    return f"${randint(0,100)}"