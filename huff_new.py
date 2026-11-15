def huffman():

    n = int(input("Enter number of characters: "))

    char = []
    freq = []

    for i in range(n):
        c = input("Enter character: ")
        f = int(input("Enter frequency: "))

        char.append(c)
        freq.append(f)

    # Create Huffman Tree
    tree = char.copy()

    while len(freq) > 1:

        # Find two smallest frequencies
        first = freq.index(min(freq))
        f1 = freq.pop(first)
        c1 = tree.pop(first)

        second = freq.index(min(freq))
        f2 = freq.pop(second)
        c2 = tree.pop(second)

        # Combine two nodes
        freq.append(f1 + f2)
        tree.append([c1, c2])

    # Generate codes
    def print_codes(node, code):

        if isinstance(node, str):
            print(node, ":", code if code else "0")
            return

        print_codes(node[0], code + "0")
        print_codes(node[1], code + "1")

    print("\nHuffman Codes:")
    print_codes(tree[0], "")


huffman()
