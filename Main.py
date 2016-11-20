import data_reader
import a_priori
import time
import argparse

#CLI Stuff
parser = argparse.ArgumentParser(description='Find frequent item sets')
parser.add_argument('fp', type=str, help="Path for data file", default="'./data/T10I4D100K.dat'")
parser.add_argument('s', type=int, help="Minumun support threshold")
parser.add_argument('c', type=float, help="Minumun confindence treshold", default=0.75)

args = parser.parse_args()

path = args.fp
c = args.c
s = args.s

transactions = [[int(n) for n in t.strip().split(" ")] for t in data_reader.read_file_transaction_level(path)]
print("Loaded data")

start = time.time()

counts_map = a_priori.apriori(transactions, s)
rules = a_priori.generate_association_rules(counts_map, c)

end = time.time()

print("==Inferred rules==")

print("Found "+str(len(rules)) +" rules in "+str((end-start))+" seconds")
for rule in rules:
    a, b, confidence = rule
    print(str(a) + " -> " + str(b) + " : c: "+str(confidence))