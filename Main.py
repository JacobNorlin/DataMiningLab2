import data_reader
import a_priori
path = './data/T10I4D100K.dat'

items = set(data_reader.read_file_item_level(path))
transactions = [t.strip().split(" ") for t in data_reader.read_file_transaction_level(path)]
a_priori.apriori(items, transactions, 3)