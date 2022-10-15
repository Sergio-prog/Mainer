# THIS IS TEST PROGRAM. DON'T USE THIS FOR REALLY MINING!!!
from hashlib import sha256

MAX_NONCE = 100000000000


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            # print(f"Yay! Successfully mined bitcoins with nonce value:{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")


if __name__ == '__main__':
    transactions = '''
    YourWallet1->YourWallet2->20,
    YourWallet3->YourWallet4->45
    '''
    difficulty = 4  # complexity of calculating a new block (Not recommended over 6)
    import time

    start = time.time()
    print("start mining")
    new_hash = mine(5, transactions, '0000000xa031942e59568d8jaf55edbe068g81268fecf9b66be9a2b8221c6ec9', difficulty)
    total_time = str((time.time() - start))
    print(f"End mining. Mining took: {total_time} seconds")
    print(new_hash)
