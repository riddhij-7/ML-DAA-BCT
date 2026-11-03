import heapq

text = input("Enter text: ")
if text == "":
    raise SystemExit("Nothing to encode")

# 1. count how often each character appears
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

# 2. put every character in a min-heap: (frequency, tie-breaker, node)
#    a node is either a single character or a (left, right) pair
heap = [(f, i, ch) for i, (ch, f) in enumerate(freq.items())]
heapq.heapify(heap)
count = len(heap)                                  # tie-breaker for new nodes

# 3. greedy step: always join the two least frequent nodes
while len(heap) > 1:
    f1, _, left = heapq.heappop(heap)
    f2, _, right = heapq.heappop(heap)
    heapq.heappush(heap, (f1 + f2, count, (left, right)))
    count += 1

# 4. walk the tree: left edge = 0, right edge = 1
codes = {}
def assign(node, code):
    if isinstance(node, str):                      # leaf = a character
        codes[node] = code or "0"                  # "or" handles a single-character text
        return
    assign(node[0], code + "0")
    assign(node[1], code + "1")

assign(heap[0][2], "")

# 5. encode the text
encoded = "".join(codes[ch] for ch in text)

print("\nChar  Freq  Code")
for ch in sorted(codes, key=lambda c: (len(codes[c]), c)):
    print(f"{ch!r:5} {freq[ch]:4}  {codes[ch]}")

print("\nEncoded text:", encoded)
print("Original size:", len(text) * 8, "bits")
print("Encoded size :", len(encoded), "bits")

# 6. decode back to check the result
rev = {c: ch for ch, c in codes.items()}
decoded, cur = "", ""
for bit in encoded:
    cur += bit
    if cur in rev:
        decoded += rev[cur]
        cur = ""
print("Decoded text :", decoded)

#Input - abracadabra