import itertools

data = {'1':['a','b'], '2':['c','d']}

values = list(data.values())

combainations = list(itertools.product(*values))

result = ' '.join([''.join(combination) for combination in combainations])

print(result)