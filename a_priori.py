import itertools
from collections import defaultdict


def ck(l, k):
    return list(itertools.combinations(l,k))

def count_items_in_transactions(transactions, candidates, k):
    frequent_items = []
    counts = defaultdict(int)
    items = set()
    for candidate in candidates:
        count = sum([1 for t in transactions if set(candidate) <= set(t)])
        if count >= k:
            counts[tuple(sorted(candidate))] = count
            frequent_items.append(candidate)
            items |= set(candidate)
    print(counts)
    return frequent_items, counts, items



def apriori(items, transactions, t):
    c1 = [(item,) for item in items]
    _,l1c,L1 = count_items_in_transactions(transactions, c1, t)
    stack = [L1]
    frequent_items = []
    counts_map = {1:l1c}
    i = 2
    while(len(stack) > 0):
        print("starting L", i)
        Lk = stack.pop()
        C = ck(Lk, i)
        print(len(C), "combinations")
        pairs, counts, allItems = count_items_in_transactions(transactions, C, t)
        print("L_"+str(i)+" done, " + str(len(allItems)) + " items found")
        if(len(pairs) > 0):
            stack.append(allItems)
            frequent_items.append(pairs)
            counts_map[i] = counts
        i += 1
    generate_association_rules(counts_map, frequent_items, 0.75)

def generate_association_rules(counts, frequent_items, t):
    rules = []
    for i, k_set in enumerate(frequent_items):
        i += 2
        for item in k_set:
            subsets = powerset(item)
            rules += [(subset, set(item) - set(subset)) for subset in subsets if counts[len(item)][tuple(sorted(item))] / counts[len(set(subset))][tuple(sorted(subset))] >= t]


#powerset without the empty set and the set itself
def powerset(iterable):
    "powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3)"
    s = list(iterable)
    return set(itertools.chain.from_iterable(itertools.combinations(s, r+1) for r in range(len(s)-1)))