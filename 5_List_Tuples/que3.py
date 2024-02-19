sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# Calculate the length of each chunk
chunk_size = len(sample_list) // 3
# Slice the list into 3 equal chunks and reverse each chunk
result = [chunk[::1] for chunk in [sample_list[i:i+chunk_size] for i in range(0, len(sample_list), chunk_size)]]
print(result)