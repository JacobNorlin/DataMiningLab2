from data_reader import read_file_item_level
from a_priori import first_pass
path = './data/T10I4D100K.dat'

items = read_file_item_level(path)
counts = first_pass(items, 2)