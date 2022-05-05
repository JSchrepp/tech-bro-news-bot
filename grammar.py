from random import random, choice

import generative
import loader

directive_start = "{$"
directive_end = "}"

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
        result += process_token(token)
    return result

def process_token(token: str) -> str:
    if token.startswith(directive_start) and token.endswith(directive_end):
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
        if c == "!money":
            return generative.get_money()
    
    rules = []
    for file in ruleFiles:
        rules += loader.read_lines(file)
    
    if not rules:
        raise ValueError("No rules to choose from in directive: " + ' '.join(directive))
    
    return process_rule(choice(rules))
