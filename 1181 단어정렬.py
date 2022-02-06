n=int(input())
word=[input() for i in range(n)]
print("\n".join(sorted(list(set(word)),key=lambda x: (len(x),x))))