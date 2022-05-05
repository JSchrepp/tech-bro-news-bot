from random import random, randint, choice, choices
from loader import read_lines
from zalgo_text import zalgo

def get_percent() -> str:
    if random() > 0.15:
        return f"{randint(0,100)}%"
    
    return choice(read_lines("special_percentage"))

def get_random_money(startMag = 2, endMag = 11) -> str:
    d1 = randint(1,9)
    d2 = randint(0,9)
    sciNotationDigitString = str(d1)
    if d2 > 0:
        sciNotationDigitString += str(d2)
    mag = randint(startMag,endMag)
    return get_money(sciNotationDigitString, mag)

def get_money(digits: str, mag: int) -> str:
    miniMag = ((mag - 1) % 3) + 1
    group = ((mag - 1) // 3)

    i = 0
    result = ""
    while i < miniMag:
        result += digits[i] if i < len(digits) else "0"
        i += 1
    if (i < len(digits)):
        result += "."
        while i < len(digits):
            result += digits[i]
            i += 1
    
    suffixes = [
        "",
        "K",
        "M",
        "B",
        "T",
        "qd",
        "Qn",
        "sx",
        "Sp",
        "O",
         "N",
    ]
    result += suffixes[group] if group < len(suffixes) else f"e{mag}"
    return "$" + result

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
