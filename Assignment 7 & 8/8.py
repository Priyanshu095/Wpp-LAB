def decode_ways(s, index=0, current_decoding="", results=None):
    if results is None:
        results = []
    
    # If we have reached the end, store the current decoding
    if index == len(s):
        results.append(current_decoding)
        return results  # Ensure results are returned here
    
    # Single digit mapping (1-9)
    if s[index] != '0':  # '0' cannot be mapped
        num1 = int(s[index])
        decode_ways(s, index + 1, current_decoding + chr(num1 + ord('A') - 1), results)

    # Double digit mapping (10-26)
    if index + 1 < len(s):
        num2 = int(s[index:index + 2])
        if 10 <= num2 <= 26:
            decode_ways(s, index + 2, current_decoding + chr(num2 + ord('A') - 1), results)
    
    return results  # Ensure results are returned here

# Taking input
encoded_message = input("Enter the encoded message: ")

# Get all possible decodings
decoded_messages = decode_ways(encoded_message)

# Display results
print("\nPossible Decoded Messages:")
for msg in decoded_messages:
    print(msg)
