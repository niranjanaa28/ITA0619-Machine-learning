S = ['Sunny', 'Warm']
G = [['?', '?']]

data = [
    (['Sunny', 'Warm'], 'Yes'),
    (['Sunny', 'Cold'], 'Yes'),
    (['Rainy', 'Warm'], 'No')
]

for x, label in data:
    if label == 'Yes':
        for i in range(len(S)):
            if S[i] != x[i]:
                S[i] = '?'
    else:
        G = [
            ['Sunny', '?'],
            ['?', 'Warm']
        ]

print("Specific boundary:", S)
print("General boundary:", G)
