def expand_non_ter(non_ter, grammar, terminals, non_terminals):
    results = []
    for rule in grammar:
        if rule[0] == non_ter:
            tmp_res = expand(rule, grammar, terminals, non_terminals)
            if len(results) == 0:
                for itm in tmp_res:
                    results += itm
            else:
                for i, itm in enumerate(results):
                    for itm2 in tmp_res:
                        results += itm2
    return results

def expand(rule, grammar, terminals, non_terminals):
    results = []
    
    for itm in rule[1]:
        tmp_res = []
        if itm in terminals:
            tmp_res.append([itm])
        else:
            tmp_res.append(expand_non_ter(itm, grammar, terminals, non_terminals))
        
        tmp_res2 = []
        for itm2 in tmp_res:
            if len(tmp_res2) == 0:
                tmp_res2 += itm2
            else:
                for i, itm3 in enumerate(tmp_res2):
                    for itm4 in itm2:
                        tmp_res2[i] += itm4
        
        if len(results) == 0:
            results += tmp_res2
        else:
            for i, itm in enumerate(results):
                for itm2 in tmp_res2:
                    results[i] += itm2
    
    return results

def isambiguous(grammar, non_ter, ter, start, inp_string):
    results = []
    for rule in grammar:
        if rule[0] == start:
            results += expand(rule, grammar, terminals, non_terminals)
    return len([token for token in results if token == inp_string]) > 1


n = int(input("No of rules = "))

start = None
grammar = []
non_terminals = []
terminals = []

for i in range(n):
    print("Rule " + str(i + 1))
    non_ter = input("Non-Terminal Symbol = ")
    ter = input("Terminal symbols seperated by space = ").split(" ")
    grammar.append((non_ter, ter))
    if non_ter not in non_terminals:
        non_terminals.append(non_ter)
    if not start:
        start = non_ter

for rule in grammar:
    for ter in rule[1]:
        if ter not in non_terminals and ter not in terminals:
            terminals.append(ter)

inp_string = input("String to check = ")

print(isambiguous(grammar, terminals, non_terminals, start, inp_string))
