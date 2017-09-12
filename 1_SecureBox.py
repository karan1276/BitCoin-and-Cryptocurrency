'''
Author: Karan Sharma

Probleum:
Page 28 at [link]
'''

import hashlib as hasher

class Block:
    def __init__(self, index, timpestamp, data, previous_hash):
        self.index = index
        self.timpestamp = timpestamp
        self.data = data
        self.previous_hash = previous_hash

    def hashMe(self):
        sha = hasher.sha256()
        sha.update(str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hash))
        return sha.hexdisgest()
