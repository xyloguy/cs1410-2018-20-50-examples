line = input()
time = 0
correct = []
incorrect = {}

while line != "-1":
    m, problem, answer = line.split()
    m = int(m)
    if answer == 'right' and problem not in correct:
        time += m
        correct.append(problem)
        if problem in incorrect:
            time += (20 * incorrect[problem])
    if answer == 'wrong':
        if problem in incorrect:
            incorrect[problem] += 1
        else:
            incorrect[problem] = 1
    line = input()

print(len(correct), time)