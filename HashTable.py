# TOTAL TIME COMPLEXITY: O(m*n) linear
# O(m*n) is the largest complexity in the class
#
# TOTAL SPACE COMPLEXITY: O(m*n) linear
# O(m*n) is the largest complexity in the class
class HashTable:
    """Constructs a key value data structure for all deliveries"""

    def __init__(self, size=10):
        self.size = size
        self.map = []
        self.mapKeys = []
        for myList in range(size):
            self.map.append([])

    # TIME COMPLEXITY: O(n) linear
    # time complexity of the insert function is linear instead of constant.
    # The reason being that although the hashing function runs in constant time the index which it is hashed to
    # consists of a chained list which then has to be iterated over to find the appropriate item.
    #
    # SPACE COMPLEXITY: O(n*m) multi-linear
    # for each index (m) within the hash table there is a a chained list of values of length (n)
    # add an element to the hashtable
    def insert(self, key, val):
        # generate hashkey to find input index of key
        hash_key = hash(key) % len(self.map)
        my_list = self.map[hash_key]

        key_exists = False
        my_item = None
        # check if key exists so we can append to the list found at key
        for index, value in enumerate(my_list):
            temp_key, temp_val = value

            if key == temp_key:
                key_exists = True
                my_item = index
                break

        if key_exists:
            my_list[my_item] = [key, val]
        else:
            # if key doesnt exists we create a new key , val pair and insert into hashtable
            my_list.append([key, val])
            self.mapKeys.append(key)

    # TIME COMPLEXITY: O(n)
    # hashing a key and looking up an index is constant time, but because this is a chained hash table
    # a list stored at the index must be iterated to find the appropriate key
    #
    # SPACE COMPLEXITY: O(m*n)
    # for each index within the hashtable(m) there is a chained list of values(n)
    # return a specific element from the hashtable
    def get(self, key):
        hash_key = hash(key) % len(self.map)
        my_list = self.map[hash_key]

        key_exists = False
        val = None
        # search our list found at index of hash table for key
        for index, value in enumerate(my_list):
            temp_key, val = value

            if key == temp_key:
                key_exists = True
                break

        if key_exists:
            return val
        else:
            return None

    # TIME COMPLEXITY: O(n)
    # hashing a key and looking up an index is constant time, but because this is a chained hash table
    # a list stored at the index must be iterated to find the appropriate key
    #
    # SPACE COMPLEXITY: O(m*n)
    # for each index within the hashtable(m) there is a chained list of values(n)
    # delete an element from the hashtable
    def delete(self, key):
        hash_key = hash(key) % len(self.map)
        my_list = self.map[hash_key]

        key_exists = False
        my_item = None
        # search list found at hashtable index for key
        for index, value in enumerate(my_list):
            temp_key, temp_val = value

            if key == temp_key:
                key_exists = True
                my_item = index
                break

        if key_exists:
            my_list.remove(my_item)
        else:
            return

    # TIME COMPLEXITY: O(m*n) linear
    # for each index within the hashtable (m) the chained list(n) must be iterated
    #
    # SPACE COMPLEXITY: 0(m*n) linear
    # for each index within the hashtable (m) the chained list (n) is iterated and returns a key value pair
    # space complexity = (n * m * 2) = O(m*n)
    # return an iterable list of hashtable elements
    def items(self):
        index = 0
        while index < len(self.map):
            for el in self.map[index]:
                yield el[0], el[1]
            index += 1

    def keys(self):
        index = 0
        while index < len(self.mapKeys):
            yield self.mapKeys[index]
            index += 1

    # TIME COMPLEXITY: O(m * n) linear
    # for each key stored within the hash table(m) we iterate over the first (n) indexes of the keys value
    # if key is not None which is (m * n). if weight is not None or status is Not none we iterate over each
    # key stored within the hash table and access the value for that key, then at a specific index
    # within that value we compare for equality.
    # this would be a time complexity of (n) because iterating the keys is linear and accessing the value of the key and
    # accessing the index of the value is constant.
    #
    # SPACE COMPLEXITY: O(m) linear
    # for each for loop within the lookup function a list is generated of m length.
    # looks up values based on id, address, deadline, status, etc.
    # if packaged to be looked up by weight it must be specified.
    def lookup(self, key=None, weight=None, status=None):
        matches = []
        # search each index in our hashtable for the specified values in key list
        if key is not None:
            # getting a list of keys within our hashtable
            for keyd in self.keys():
                # for each key get the value stored at that key
                item = self.get(keyd)
                for val in range(5):
                    # for the values contained within the list found at key
                    # search for the key within each index
                    if key == item[val]:
                        matches.append(item)

            return matches
        # search for a specific weight
        elif weight is not None:
            # get available keys of hashtable
            for keyd in self.keys():
                # return specific val from given key
                item = self.get(keyd)
                # check if the weight matches
                if weight == item[5]:
                    matches.append(item)
            return matches

        # search for specific status value
        elif status is not None:
            # get available keys
            for keyd in self.keys():
                # get val from given key
                item = self.get(keyd)
                # check if the item has the specified status
                if status in item[7]:
                    matches.append(item)
            return matches
