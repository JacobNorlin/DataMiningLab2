import data_reader
import a_priori
path = './data/T10I4D100K.dat'

items = set([int(n) for n in data_reader.read_file_item_level(path)])
transactions = [[int(n) for n in t.strip().split(" ")] for t in data_reader.read_file_transaction_level(path)]

print(transactions)

frequent_items, counts_map = a_priori.apriori(items, transactions, 10)
rules = a_priori.generate_association_rules(counts_map, frequent_items, 0.75)

for rule in rules:
    a, b, confidence = rule
    print(str(a) + " -> " + str(b) + " : c: "+str(confidence))