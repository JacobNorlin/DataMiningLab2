import itertools

def read_file_transaction_level(path):
    return [line.rstrip("\n") for line in open(path)][1:100]

def read_file_item_level(path):
    transactions = read_file_transaction_level(path)
    items = [[item for item in transaction.split(" ")] for transaction in transactions]
    return list(itertools.chain(*items))