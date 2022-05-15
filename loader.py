from os import listdir

def search_rules(filePrefix: str) -> list[str]:
    fileNames = [f for f in listdir("assets") if f.startswith(filePrefix)]
    rules = []
    for fileName in fileNames:
        rules += read_lines(f"assets/{fileName}")
    return rules

def read_lines(filePath: str) -> list[str]:
    with open(filePath, mode='r', encoding="utf-8") as file:
        lines = [line.rstrip('\n') for line in file.readlines()]
        file.close()
    return lines