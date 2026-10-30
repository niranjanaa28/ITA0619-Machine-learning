from itertools import product

data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Weak', 'No'],
    ['Sunny', 'Warm', 'High', 'Weak', 'Yes']
]

domains = [
    ['Sunny', 'Rainy'], ['Warm', 'Cold'],
    ['Normal', 'High'], ['Strong', 'Weak']
]

values = [d + ['?', 'Ø'] for d in domains]
all_h = list(product(*values))

def matches(h, x):
    return all(a == '?' or a == b for a, b in zip(h, x))

consistent = [
    h for h in all_h
    if all(matches(h, r[:-1]) == (r[-1] == 'Yes') for r in data)
]

def more_general(h1, h2):
    return all(a == '?' or a == b or b == 'Ø'
               for a, b in zip(h1, h2))

G = [h for h in consistent if not any(
    h != other and more_general(other, h)
    for other in consistent)]

S = [h for h in consistent if not any(
    h != other and more_general(h, other)
    for other in consistent)]

print("Specific Boundary S:", S)
print("General Boundary G:", G)
