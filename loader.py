from os import listdir

def read_lines(filePrefix: str) -> list[str]:
    fileNames = [f for f in listdir("assets") if f.startswith(filePrefix)]
    lines = []
    for fileName in fileNames:
        with open(f"assets/{fileName}", mode='r', encoding="utf-8") as file:
            lines += [line.rstrip('\n') for line in file.readlines()]
            file.close()
    return lines
