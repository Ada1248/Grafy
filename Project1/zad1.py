import zestaw1

adj_matrix = []
i_matrix = []
adj_list = []

if __name__ == "__main__":
    with open('FileIn.txt') as file:
        mode = str(file.readline().split()[0])
        for line in file:
            if mode == 'A':
                row = []
                for element in line.strip().split():
                    row.append(int(element))
                adj_matrix.append(row)

            elif mode == 'I':
                row = []
                for element in line.strip().split():
                    row.append(int(element))
                i_matrix.append(row)


            elif mode == 'L':
                row = []
                it = 0
                for element in line.strip().split(' '):
                    if it == 0:
                        it += 1
                    else:
                        row.append(int(element) - 1)
                adj_list.append(row)

    if mode == 'A':
        i_matrix = zestaw1.adj_matrix_to_i_matrix(adj_matrix)
        adj_list = zestaw1.adj_matrix_to_list(adj_matrix)

    elif mode == 'I':
        adj_matrix = zestaw1.i_matrix_to_adj_matrix(i_matrix)
        adj_list = zestaw1.i_matrix_to_list(i_matrix)

    elif mode == 'L':
        adj_matrix = zestaw1.adj_list_to_adj_matrix(adj_list)
        i_matrix = zestaw1.adj_list_to_i_matrix(adj_list)

    zestaw1.print_list(adj_list)
    zestaw1.print_adj_matrix(adj_matrix)
    zestaw1.print_i_matrix(i_matrix)


# W FileIn w pierwszej lini musimy podać co podajemy:
# A - macierz sąsiedztwa
# I - macierz incydencji
# L - listę sąsiedztwa
# macierze itd mają być bezpośrednio pod literką
# nie może być nigdzie pustych linii
# przykładowe pliki:
# L
# 1: 2 5
# 2: 1 3 4 5
# 3: 2 4
# 4: 2 3 5
# 5: 1 2 4

# N
# 0 1 0 0 1
# 1 0 1 1 1
# 0 1 0 1 0
# 0 1 1 0 1
# 1 1 0 1 0

# I
# 1 0 0 0 1 0 0
# 1 1 1 0 0 1 0
# 0 1 0 1 0 0 0
# 0 0 1 1 0 0 1
# 0 0 0 0 1 1 1