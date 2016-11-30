def gen():
    yield 3
    yield 'wow'
    yield -1
    yield 1.2


for i in gen():
    print(i)
