from os import listdir

import loader
import grammar

def test_rules():
    for file in listdir("assets"):
        for rule in loader.read_lines("assets/" + file):
            try:
                grammar.process_rule(rule)
            except Exception as e:
                print(f"Failed to process rule `{rule}` in file {file}")
                print(f"exception: {e}")

test_rules()