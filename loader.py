from os import listdir
from pathlib import Path

_assetsDir = Path(__file__).parent / 'assets'

def search_rules(filePrefix: str) -> list[str]:
    fileNames = [f for f in listdir(_assetsDir) if f.startswith(filePrefix)]
    rules = []
    for fileName in fileNames:
        rules += read_lines(_assetsDir / fileName)
    return rules

def read_lines(filePath: str) -> list[str]:
    with open(filePath, mode='r', encoding="utf-8") as file:
        lines = [line.rstrip('\n') for line in file.readlines()]
        file.close()
    return lines
