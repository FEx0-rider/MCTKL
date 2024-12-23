# writen by m.e.
# version 1.0

import hashlib
from colorama import Fore, Style, Back
import itertools
import string
import time

start_time = time.time()


class HashCracker:
    def __init__(self, hash_value):
        self.hash_value = hash_value

    def crack_hash(self, max_length):
        chars = string.ascii_letters + string.digits
        for length in range(1, max_length + 1):
            for attempt in itertools.product(chars, repeat=length):
                attempt_str = ''.join(attempt)
                hashed_attempt = hashlib.sha256(attempt_str.encode('utf-8')).hexdigest()
                if hashed_attempt == self.hash_value:
                    return attempt_str
        return None

hash_value = input("[" + Fore.RED + ">" + Style.RESET_ALL + "] Zadejte hash hodnotu: ")
max_length = int(input("[" + Fore.RED + ">" + Style.RESET_ALL + "] Zadejte maximální délku hesla: "))

cracker = HashCracker(hash_value)
result = cracker.crack_hash(max_length)

if result:
    print("[" + Fore.RED + ">" + Style.RESET_ALL + "] Hash hodnota byla rozkódována na: ", result)
else:
    print("[" + Fore.RED + ">" + Style.RESET_ALL + "] Hash hodnota nebyla rozkódována")

end_time = time.time()
print("[" + Fore.RED + ">" + Style.RESET_ALL + "] In time : " + str((end_time - start_time))[:2] + " s")