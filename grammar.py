from random import random, choice

import generative
import loader

directive_start = "{$"
directive_end = "}"

def execute():
    result = (process_rule(choice(loader.read_lines("headline")))
        .replace("  ", " ")  # strip extra space generation
        .strip())
    return result[0].upper() + result[1:]

def tokenize(statement: str) -> list[str]:
    tokens = [statement]
    while (i := tokens[-1].find(directive_start)) != -1:
        curr = tokens.pop()
        tokens.append(curr[0:i])
        curr = curr[i:]

        j = curr.find(directive_end) + 1
        tokens.append(curr[0:j])
        tokens.append(curr[j:])
    
    return tokens

def process_rule(rule: str) -> str:
    result = ""
    for token in tokenize(rule):
        if (processed := process_token(token)):
            result += processed
    return result

def process_token(token: str) -> str:
    if token.startswith(directive_start) and token.endswith(directive_end):
        if random() > 0.9999: # "accidental" failure to resolve
            return generative.get_zalgo(token)
        return process_directive(token[len(directive_start):-len(directive_end)].split())
    else:
        return token

def process_directive(directive: list[str]) -> str:
    isTriggerProbability = lambda item: item.startswith("?")
    isCommand = lambda item: item.startswith("!")
    isRuleFile = lambda item: not isTriggerProbability(item) and not isCommand(item)

    triggerProbability = ([x for x in directive if isTriggerProbability(x)][:1] or [None])[0]
    if triggerProbability and float(triggerProbability[1:]) > random():
        return None

    commands = [x for x in directive if isCommand(x)]
    ruleFiles = [x for x in directive if isRuleFile(x)]

    for c in commands:
        if c == "!percent":
            return generative.get_percent()
        if c.startswith("!money"):
            return process_money_command(c)
        if c == "!version":
            return generative.get_version()
    
    rules = []
    for file in ruleFiles:
        rules += loader.read_lines(file)
    
    if not rules:
        raise ValueError("No rules to choose from in directive: " + ' '.join(directive))
    
    return process_rule(choice(rules))

def process_money_command(c):
    if (i := c.find('[')) > 0 and (j := c.find(']')) > 0:
        magBounds = c[i+1:j].split(',')
        return generative.get_random_money(int(magBounds[0]), int(magBounds[1]))
    return generative.get_random_money()