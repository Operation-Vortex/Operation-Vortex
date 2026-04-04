

import sys

collection_size = 5
list_collection = []
tuple_collection = ()
set_collection =  set()

for collection_item in range(collection_size):
    list_collection.append(collection_item)
    tuple_collection += (collection_item,)
    set_collection.add(collection_item)

print("List collection:", list_collection)
print("List collection size:", sys.getsizeof(list_collection))

print("Tuple collection:", tuple_collection)
print("Tuple collection size:", sys.getsizeof(tuple_collection))

print("Set collection:", set_collection)    
print("Set collection size:", sys.getsizeof(set_collection))