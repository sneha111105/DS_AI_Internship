import random
val_int = random.randint(1, 10)
val_float = random.random()

val_range = random.uniform(1.5, 9.5)
item = random.choice(["A", "B", "C"])
print("Random Integer:", val_int)
print("Random Float:", val_float)
print("Random Float in Range (1.5 to 9.5):", val_range)
print("Random Item from List:", item)


my_list = [10, 20, 30]
random.shuffle(my_list)