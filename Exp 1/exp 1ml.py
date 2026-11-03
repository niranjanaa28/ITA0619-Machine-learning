data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

h = None

for row in data:
    if row[-1] == 'Yes':
        if h is None:
            h = row[:-1].copy()
        else:
            for i in range(len(h)):
                if h[i] != row[i]:
                    h[i] = '?'

print("Final hypothesis:", h)
