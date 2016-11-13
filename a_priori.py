import itertools
#wrong
def first_pass(items, t):
    counts = {item:items.count(item) for item in items if items.count(item) > t}
    print(counts)