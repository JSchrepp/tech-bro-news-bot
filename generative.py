from random import random, randint, choice, choices
from loader import read_lines
from zalgo_text import zalgo

def get_percent() -> str:
    if random() > 0.15:
        return f"{randint(0,100)}%"
    
    return choice(read_lines("special_percentage"))

def get_money() -> str:
    return f"${randint(0,100)}"

def get_version() -> str:
    cases = [
        (0.1, f"{randint(0,12)}.{randint(0,50)}.{randint(0,999)}"),
        (0.4, f"{randint(0,12)}.{randint(0,50)}"),
        (0.5, f"{randint(0,12)}")
    ]
    return choices(
        [x[1] for x in cases],
        [y[0] for y in cases])[0]

def get_zalgo(text: str) -> str:
    return zalgo.zalgo().zalgofy(text)