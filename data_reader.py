import itertools

def read_file_transaction_level(path):
    return [line.rstrip("\n") for line in open(path)]
