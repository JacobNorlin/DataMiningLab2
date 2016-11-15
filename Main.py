import data_reader
import a_priori
path = './data/T10I4D100K.dat'
#path = './data/test.dat'

transactions = [[n for n in t.strip().split(" ")] for t in data_reader.read_file_transaction_level(path)]

print("Loaded data")

counts_map = a_priori.apriori(transactions, 1000)
rules = a_priori.generate_association_rules(counts_map, 0.75)

print("==Inferred rules==")
for rule in rules:
    a, b, confidence = rule
    print(str(a) + " -> " + str(b) + " : c: "+str(confidence))