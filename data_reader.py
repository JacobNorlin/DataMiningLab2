import itertools

def read_file_transaction_level(path):
    return [line.rstrip("\n") for line in open(path)]

def read_file_item_level(path):
    transactions = read_file_transaction_level(path)
    items = [[item for item in transaction.split(" ") if item != ''] for transaction in transactions]
    return list(itertools.chain(*items))