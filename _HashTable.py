#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:48:05 2022

@author: dharmendrakhakhar
"""

class HashTable:

    def __init__(self):
        self.size = 360
        self.hashmap = [[] for _ in range(0, self.size)]
        # print(self.hashmap)

    def hash_func(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key
    
    
    
    def checkKey(self, key):
        hash_key = self.hash_func(key)
        key_exists = False
        slot = self.hashmap[hash_key]
        for _, kv in enumerate(slot):
            k, v = kv
            if key == k:
                key_exists = True
                break
        
        return key_exists

    def set(self, key, value):
        hash_key = self.hash_func(key)
        # key_exists = False
        slot = self.hashmap[hash_key]
        slot.append((key, value))

    def get(self, key):
        hash_key = self.hash_func(key)
        slot = self.hashmap[hash_key]
        for kv in slot:
            k, v = kv
            if key == k:
                return v
            else:
                raise KeyError('Key does not exist.')

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)



# H = HashTable()
# H.set('key1','value1')
# H.set('key2','value2')
# H.set('key3','value3')

# H.set(10,'value10')
# H.set(20, 'value20')

# H['NEWWWWWWWWW'] = 'newwwwwwwww'

# print(H['key1'])
# print(H[10])
# print(H[20])

# print(H.hashmap)


# H2 = HashTable()
# H2.set('key1','value1')
# H2.set('key2','value2')
# H2.set('key3','value3')

# H2.set(10,'value10')
# H2.set(20, 'value20')