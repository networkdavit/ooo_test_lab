def serialize_set(int_set):
    serialized = ""
    for num in sorted(int_set):
        serialized += str(len(str(num))) + str(num)
    return serialized

def deserialize_set(serialized_str):
    int_set = set()
    i = 0
    while i < len(serialized_str):
        num_len = int(serialized_str[i])
        i += 1
        int_set.add(int(serialized_str[i:i + num_len]))
        i += num_len
    return int_set

def compression_ratio(original, compressed):
    return len(compressed) / len(original)

tests = [
    {1},  
    {3, 1, 4, 1, 5, 9, 2, 6},  
    set(range(1, 51)),  
    set(range(1, 101)),  
    set(range(1, 501)),  
    set(range(1, 1001)),  
    set(range(1, 10)), 
    set(range(10, 100)),  
    set(range(100, 300)), 
    set([i % 300 + 1 for i in range(900)])  
]

for test_set in tests:
    original_str = serialize_set(test_set)
    deserialized_set = deserialize_set(original_str)
    compression_ratio_val = compression_ratio(original_str, original_str)
    
    print("Original Set:", test_set)
    print("Original String:", original_str)
    print("Deserialized Set:", deserialized_set)
    print("Compression Ratio:", compression_ratio_val)
    print("\n")

