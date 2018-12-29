def print_table():
    word_len = []
    for row in range(len(tableData)):
        word_len.append(max([len(x) for x in tableData[row]]))
    for col in range(len(tableData[0])):
        for row in range(len(tableData)):
            print(tableData[row][col].rjust(word_len[row]), end=' ')
        print('\n')


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table()