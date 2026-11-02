import heapq

def huffman_encoding(characters, frequencies):
    heap = []

    for i in range(len(characters)):
        heap.append((frequencies[i], i, characters[i]))

    heapq.heapify(heap)
    counter = len(characters)

    while len(heap) > 1:
        freq1, _, left = heapq.heappop(heap)
        freq2, _, right = heapq.heappop(heap)

        merged = (freq1 + freq2, counter, (left, right))
        heapq.heappush(heap, merged)
        counter += 1

    root = heap[0]
    codes = {}

    def generate_codes(node, code=""):
        if isinstance(node, str):
            codes[node] = code or "0"
            return

        generate_codes(node[0], code + "0")
        generate_codes(node[1], code + "1")

    generate_codes(root[2])
    return codes


# User input
n = int(input("Enter the number of characters: "))

characters = []
frequencies = []

for i in range(n):
    char = input("Enter character: ")
    freq = int(input("Enter frequency: "))

    characters.append(char)
    frequencies.append(freq)

codes = huffman_encoding(characters, frequencies)

print("\nHuffman Codes:")
for char in characters:
    print(char, ":", codes[char])
