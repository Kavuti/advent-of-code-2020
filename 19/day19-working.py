import sys
import regex

def expand(value):
    if not value.isdigit(): 
        print(value)
        return value 
    return "(?:" + "".join(map(expand, rules[value].split())) + ")"


def solve(rules, messages):
   
    r = regex.compile(expand("0"))
    return sum(r.fullmatch(m) is not None for m in messages)


raw_rules, messages = sys.stdin.read().split("\n\n")
messages = messages.splitlines()
rules = dict(
    raw_rule.replace('"', "").split(": ", 1)
    for raw_rule in raw_rules.splitlines()
)

print(expand("1"))

print(solve(rules, messages))
rules["8"] = "42 +"  # repeat pattern
rules["11"] = "(?P<R> 42 (?&R)? 31 )"  # recursive pattern
print(solve(rules, messages))