sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

length = len(sample_list)
chunk_size = int(length/3)
start = 0
end = chunk_size

for i in range(3):
    indexes = slice(start, end)
    list_chunk = sample_list[indexes]
    print(("Chunk", i, list_chunk))
    print("After reversing it ", list(reversed(list_chunk)))
    start = end
    end += chunk_size
