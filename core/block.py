'''
Author: Karan Sharma

Probleum:
Page 28 at [link]
'''

import hashlib as hasher
import datetime as date
import uuid

class Block:
    def __init__(self, data, next_hash=None, next_block=None):
        if next_block is None: #for the first block
            self.index = 0
            self.timestamp = date.datetime.now()
            self.data = data
            self.next_hash = next_hash
            self.next_block = None
        else:
            self.index = next_block.index + 1
            self.timestamp = date.datetime.now()
            self.data = data
            self.next_hash = next_hash
            self.next_block = next_block

    def hashMe(self):
        salt = uuid.uuid4().hex
        sha = hasher.sha256()
        sha.update(str(salt) +
                   str(self.index) +
                   str(self.timestamp) +
                   str(self.data) +
                   str(self.next_hash) +
                   str(salt))
        return sha.hexdigest()
