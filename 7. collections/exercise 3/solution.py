from collections import Counter


poll_1 = {'yes': 140, 'no': 120, None: 12}
poll_2 = {'yes': 113, 'no': 132, None: 9}
poll_3 = {'yes': 16, 'no': 14}

counter_1 = Counter(poll_1)
counter_2 = Counter(poll_2)
counter_3 = Counter(poll_3)

total = counter_1 + counter_2 + counter_3

print(total['yes'])
