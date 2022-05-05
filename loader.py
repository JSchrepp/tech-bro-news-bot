def read_lines(optionFileName: str) -> list[str]:
    with open(f"assets/{optionFileName}.txt", mode='r', encoding="utf-8") as file:
        options = [line.rstrip('\n') for line in file.readlines()]
        file.close()
        return options
