'''
Author: Karan Sharma

Probleum:
Page 28 at [link]
'''

import hashlib as hasher
from core import create_genesis_block, Block
import datetime as date

class BlockChain:
    def __init__(self):
        self.headBlock = Block("Genesis Block")
        self.headHash = self.headBlock.hashMe()

    def add_block(self,data):
        new_block = Block(data, self.headHash,self.headBlock)
        self.headBlock = new_block
        self.headHash = self.headBlock.hashMe()
        print("Block added!")
        print("Index: "+str(self.headBlock.index))
        print("Timestamp: "+str(self.headBlock.timestamp))
        print("Hash: "+str(self.headHash))

    def demonstrate(self):
        num_of_blocks_to_add = 5
        for i in range(0, num_of_blocks_to_add):
            self.add_block("Sample data")

newChain = BlockChain()
newChain.demonstrate()
