def even_gen():
    for i in range(2, 21, 2):
      yield i

for i in even_gen():
    print(i)
