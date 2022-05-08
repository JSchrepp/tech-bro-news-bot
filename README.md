# Tech Bro News Bot

Your one and only totally legit #technews source!

Twitter bot using a context-free grammar to generate headlines.

## Contributing

### Content

`assets` contains the .txt files of generative content, where each line in a file is a rule. Rules consist of directives (contained within `{$ }`) and plaintext. Ensure rules are sorted alphabetically.

Grammar is evaluated by selecting a random value from an unweighted list of rules, recursively processing any directives, until a final plaintext string is returned.

Directives can contain 0 or more rule file identifiers. A rule list is created by reading in each .txt file that *starts with* that identifier for each file identifier. The grammar then selects a rule to evaluate uniformly from that combined list.

Directives can also contain a trigger probability, notated `?<float>` where float is in range [0,1). If present, the rest of the directive will only be executed if the trigger probability succeeds, otherwise the directive will evaluate empty.

Finally, directives can contain commands, notated `!<command>`. Currently supported commands are:

| Command  | Description |
| ------------- | ------------- |
| `!int`     | Generates a random integer value. Defaults to a non-zero single digit value, but range can be specified by appending `[min,max]` to the command. |
| `!money`   | Generates a random monetary value of 2 significant figures. Defaults to an order of magnitude range of [2,11], but can be specified by appending `[min,max]` to the command. |
| `!percent` | Generates a random integer [0,100] and attaches a `%` character to the end. 15% chance to instead select a rule from `special_percentage.txt` |
| `!version` | Generates a random version string with 50% chance of only major version number, 40% chance of major.minor string, and 10% chance of major.minor.patch string. Possible values include [0,12].[0,50].[0,999]. |
