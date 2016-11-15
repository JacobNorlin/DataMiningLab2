import itertools
from collections import defaultdict


def count_items_in_transactions(transactions, prev_frequent_items, k, s):
    counts = defaultdict(int)
    frequent_items = set()
    for t in transactions:
        fi = t if len(prev_frequent_items) == 0 else [item for item in t if item in prev_frequent_items]
        candidates = set(itertools.combinations(fi, k))
        for candidate in candidates:
            candidate = tuple(sorted(candidate))
            counts[candidate] += 1
            if counts[candidate] >= s:
                frequent_items |= set(candidate)
    return counts, frequent_items

def count_individual_items(items, t):
    return {item:items.count(item) for item in items if items.count(item) >= t}

def apriori(transactions, t):
    #counts = count_individual_items(items, t)
    counts, fi = count_items_in_transactions(transactions, [], 1, t)
    print("First pass count done")
    stack = [fi]
    frequent_items = []
    counts_map = {1:counts}
    i = 2
    while(len(stack) > 0):
        print("starting L", i)

        prev_all_items = stack.pop()

        n_counts, n_frequent_items = count_items_in_transactions(transactions, prev_all_items, i, t)
        if(len(n_frequent_items) > 0):
            stack.append(n_frequent_items)
            frequent_items.append(n_frequent_items)
            counts_map[i] = n_counts
        i += 1
    return counts_map

def generate_association_rules(count_map, t):
    rules = []
    for k, k_sets in count_map.items():
        if k == 1: continue
        for item in k_sets:
            subsets = [(value, len(value)) for value in powerset(item)]
            all_rules = [(subset, set(item) - set({subset} if i == 1 else set(subset)), count_map[k][item] / count_map[i][subset]) for subset, i in subsets]
            rules += [(a, b, c) for a, b, c in all_rules if c >= t]

    return rules

#powerset without the empty set and the set itself
def powerset(iterable):
    "powerset([1,2,3]) --> (1,) (2,) (3,) (1,2) (1,3) (2,3)"
    s = list(iterable)
    return set(itertools.chain.from_iterable(itertools.combinations(s, r+1) for r in range(len(s)-1)))