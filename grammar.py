from random import random, choice, randint

import generative
import loader

directive_start = "{$"
directive_end = "}"

def execute():
    result = (process_rule(choice(loader.search_rules("headline")))
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
            return process_rule(generative.get_percent())
        if c.startswith("!money"):
            return process_rule(process_money_command(c))
        if c.startswith("!int"):
            return process_rule(process_int_command(c))
        if c == "!version":
            return process_rule(generative.get_version())
    
    rules = []
    for file in ruleFiles:
        rules += loader.search_rules(file)
    
    if not rules:
        raise ValueError("No rules to choose from in directive: " + ' '.join(directive))
    
    return process_rule(choice(rules))

def process_money_command(c):
    if (optionalMagRange := parse_optional_bracket_range(c)):
        return generative.get_random_money(int(optionalMagRange[0]), int(optionalMagRange[1]))
    return generative.get_random_money()

def process_int_command(c):
    if (optionalRange := parse_optional_bracket_range(c)):
        return str(randint(int(optionalRange[0]), int(optionalRange[1])))
    return str(randint(1,9))

def parse_optional_bracket_range(c):
    if (i := c.find('[')) > 0 and (j := c.find(']')) > 0:
        magBounds = c[i+1:j].split(',')
        return (magBounds[0], magBounds[1])
    return None