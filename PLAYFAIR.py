def generate_playfair_matrix(keyword):
    keyword = ''.join(filter(str.isalpha, keyword.upper()))
    keyword = ''.join(sorted(set(keyword), key=keyword.index))
    matrix = [['' for _ in range(5)] for _ in range(5)]
    row = 0
    col = 0
    for char in keyword:
        matrix[row][col] = char
        col += 1
        if col == 5:
            col = 0
            row += 1
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    for char in alphabet:
        if char not in keyword:
            matrix[row][col] = char
            col += 1
            if col == 5:
                col = 0
                row += 1
    return matrix
pt=input("Enter plain text : ")
keyword = input("Enter keyword : ")
playfair_matrix = generate_playfair_matrix(keyword)
print("The playfair matrix : ")
for row in playfair_matrix:
    print(row)