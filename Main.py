import data_reader
import a_priori
path = './data/T10I4D100K.dat'

items = data_reader.read_file_item_level(path)
transactions = data_reader.read_file_transaction_level(path)
a_priori.apriori(items, transactions, 5000)