dic = {}

letters = ["a", "b", "c"]
numbers = [1, 2, 3]

for i, j in zip(letters, numbers):
    dic[i] = j

print(dic["a"])
