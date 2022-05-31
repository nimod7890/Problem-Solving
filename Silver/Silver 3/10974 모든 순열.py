from itertools import permutations
for i in permutations(range(1, int(input())+1)):
    print(" ".join(map(str, i)))
