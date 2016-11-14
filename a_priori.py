import itertools
from collections import defaultdict

def count_and_filter(items, t):
    counts = [item for item in set(items) if items.count(item) > t]
    return counts

def ck(l, k):
    return list(itertools.combinations(l,k))

def count_in_transactions(transactions, items, k):
    counts = defaultdict(int)
    pairs = set()
    allItems = set()
    for transaction in transactions:
        for tuple in items:
            if all([i in transaction for i in tuple]) == True:
                counts[tuple] += 1
                if(counts[tuple] > k):
                    pairs.add(tuple)
                    for v in tuple:
                        allItems.add(v)
    return pairs, allItems, counts

def apriori(items, transactions, t):
    L1 = count_and_filter(items, t)
    stack = [L1]
    frequent_items = []
    counts_map = {}
    i = 2
    while(len(stack) > 0):
        Lk = stack.pop()
        C = ck(Lk, i)
        pairs, allItems, counts = count_in_transactions(transactions, C, i)
        print("L_"+str(i)+" done")
        if(len(pairs) > 0):
            stack.append(allItems)
            frequent_items.append(pairs)
            counts_map[i] = counts
        i += 1

    


    print(frequent_items)