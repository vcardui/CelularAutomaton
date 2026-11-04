# +----------------------------------------------------------------------------+
# | CARDUI TECH v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2026 - 2026, CARDUITECH.COM (www.carduitech.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.carduitech.com/license/
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: October 29th, 2026
# | Last update..: October 30th, 2026
# | WhatIs.......: Celular Automaton - Class
# +-----------------------------------------------------------------------------+
from idlelib import rpc

# ------------ Resources / Documentation involved -------------

# --------------------------- Code ----------------------------
transition_functions = []
for i in range(0, 8):
    if i == 0:
        a = 0
    else:
        a = 1

    transition_functions.append([f"{i:03b}", a])

print(f"transition_functions {transition_functions}")

# rule = 254
# rule = 8


rule = 'abcde'
print(f"rule: {rule}")

next_generation = f"{rule}"

"""
for i in range(0, 6):
    print(f"transition_functions[i][0][1]: {transition_functions[i][0][1]}")
    for x in next_generation:
        print(x)

    print(f"---- {i}")
"""


# print(f"transition_functions[i][0][1]: {transition_functions[i][0][1]}")
# for x in range(len(next_generation)):
x = 0
print(f"previous: {next_generation[int(x):-1]}")
print(f"current: {next_generation[int(x)]}")
print(f"next: {next_generation[int(x):1]}")