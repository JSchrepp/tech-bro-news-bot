from random import random, randint, choice, choices
from loader import read_lines
from zalgo_text import zalgo

def get_percent() -> str:
    if random() > 0.15:
        return f"{randint(0,100)}%"
    
    return choice(read_lines("special_percentage"))

def get_money(startMag = 2, endMag = 11) -> str:
    val = str(randint(1,99))
    mag = randint(startMag,endMag)
    miniMag = (mag % 3) + 1
    group = mag // 3

    i = 0
    result = ""
    while i < miniMag:
        result += val[i] if i < len(val) else "0"
        i += 1
    if (i < len(val)):
        result += "."
        while i < len(val):
            result += val[i]
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
    return result

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
