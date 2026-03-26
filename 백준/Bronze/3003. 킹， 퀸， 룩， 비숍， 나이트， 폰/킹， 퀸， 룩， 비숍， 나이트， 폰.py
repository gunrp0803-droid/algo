
correct_pieces = [1, 1, 2, 2, 2, 8]


found_pieces = list(map(int, input().split()))


for i in range(6):
    print(correct_pieces[i] - found_pieces[i], end=' ')