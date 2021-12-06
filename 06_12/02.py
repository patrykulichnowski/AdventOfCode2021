initial_state = [5, 1, 5, 3, 2, 2, 3, 1, 1, 4, 2, 4, 1, 2, 1, 4, 1, 1, 5, 3, 5, 1, 5, 3, 1, 2, 4, 4, 1, 1, 3, 1, 1, 3, 1, 1, 5, 1, 5, 4, 5, 4, 5, 1, 3, 2, 4, 3, 5, 3, 5, 4, 3, 1, 4, 3, 1, 1, 1, 4, 5, 1, 1, 1, 2, 1, 2, 1, 1, 4, 1, 4, 1, 1, 3, 3, 2, 2, 4, 2, 1, 1, 5, 3, 1, 3, 1, 1, 4, 3, 3, 3, 1, 5, 2, 3, 1, 3, 1, 5, 2, 2, 1, 2, 1, 1, 1, 3, 4, 1, 1, 1, 5, 4, 1, 1, 1, 4, 4, 2, 1, 5, 4, 3, 1, 2, 5, 1, 1, 1, 1, 2, 1, 5, 5, 1, 1, 1, 1, 3, 1, 4, 1, 3, 1, 5, 1,
                 1, 1, 5, 5, 1, 4, 5, 4, 5, 4, 3, 3, 1, 3, 1, 1, 5, 5, 5, 5, 1, 2, 5, 4, 1, 1, 1, 2, 2, 1, 3, 1, 1, 2, 4, 2, 2, 2, 1, 1, 2, 2, 1, 5, 2, 1, 1, 2, 1, 3, 1, 3, 2, 2, 4, 3, 1, 2, 4, 5, 2, 1, 4, 5, 4, 2, 1, 1, 1, 5, 4, 1, 1, 4, 1, 4, 3, 1, 2, 5, 2, 4, 1, 1, 5, 1, 5, 4, 1, 1, 4, 1, 1, 5, 5, 1, 5, 4, 2, 5, 2, 5, 4, 1, 1, 4, 1, 2, 4, 1, 2, 2, 2, 1, 1, 1, 5, 5, 1, 2, 5, 1, 3, 4, 1, 1, 1, 1, 5, 3, 4, 1, 1, 2, 1, 1, 3, 5, 5, 2, 3, 5, 1, 1, 1, 5, 4, 3, 4, 2, 2, 1, 3]
countList = []
for i in range(0, 9):
    counter = 0
    for j in range(0, len(initial_state)):
        if initial_state[j] == i:
            counter += 1
    countList.append(counter)

for day in range(0, 256):
    memorized = countList[0]
    for i in range(0, len(countList)):
        if i == 0:
            memorized = countList[0]
            countList[7] += memorized
        else:
            countList[i-1] = countList[i]
    countList[8] = memorized

summary = 0
for i in countList:
    summary += i
print("result", summary)
