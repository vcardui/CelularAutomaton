# +----------------------------------------------------------------------------+
# | CARDUI TECH v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2026 - 2026, CARDUITECH.COM (www.carduitech.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.carduitech.com/license/
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: November 4th, 2026
# | Last update..: November 5th, 2026
# | WhatIs.......: Celular Automaton 1D - Class
# +-----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# Sólo cosas vistas en clase y mi linda mentecita

# --------------------------- Code ----------------------------
rule = 254
current_generation = f"0001000"

rule_num = f"{rule:03b}"
print(f"rule: {rule} = {rule_num}")

transition_functions = {}
for i in range(len(rule_num)):
    transition_functions[f"{i:03b}"] = rule_num[-i]

print(f"transition_functions {transition_functions}")

print(f"current_generation: {current_generation}\n")

for i in range(0, 6):
    print(f"------------ {i+1} ------------")
    print(current_generation)
    next_generation = [""] * len(current_generation)

    for x in range(len(current_generation)):
        previous = current_generation[int(x)-1]
        current = current_generation[int(x)]

        if len(current_generation) <= int(x)+1:
            next = current_generation[len(current_generation) - (int(x)+1)]
        else:
            next = current_generation[int(x) + 1]

        transition = f"{previous}{current}{next}"
        try:
            new_element = transition_functions[transition]
            print(f"transition: {transition} => transition function: {new_element}")
        except KeyError:
            # print(f"No transition for {transition}")
            new_element = current_generation[int(x)]

        next_generation[x] = new_element

    next_generation = "".join(next_generation)
    current_generation = next_generation