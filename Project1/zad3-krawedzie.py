import zestaw1
import random
random.seed()

n_matrix = []

def gen_G_l(n, l):
    for i in range(l):
        row = []
        duplicate = True
        temp1 = int(random.random() * n)
        temp2 = int(random.random() * n)
        while temp1 == temp2:
            temp1 = int(random.random() * n)
            temp2 = int(random.random() * n)
        #srawdza czy dana para krawedzi juz nie została wylosowana
        while duplicate:
            for tmp in n_matrix:
                while (tmp[0] == temp1 and tmp[1] == temp2) or (tmp[0] == temp2 and tmp[1] == temp1) or temp2 == temp1:
                    temp1 = int(random.random() * n)
                    temp2 = int(random.random() * n)
            duplicate = False
        row.append(temp1)
        row.append(temp2)
        n_matrix.append(row)
    i_matrix = []

    for i in range(l):
        row = []
        i_matrix.append(row)
        for j in range(n):
            i_matrix[i].append(0)

    #uzupelnianie macierzy incydencji
    for i in range(0, l):
        i_matrix[i][n_matrix[i][0]] = 1
        i_matrix[i][n_matrix[i][1]] = 1
    i_matrix = zestaw1.transpose(i_matrix)

    with open("random_graph.txt", 'w') as file:
        file.writelines(' '.join(str(j) for j in i) + '\n' for i in i_matrix)
    file.close()
    return i_matrix

if __name__ == "__main__":
    im_m = gen_G_l(8, 8)
    adj_matrix = zestaw1.i_matrix_to_adj_matrix(im_m)
    adj_list = zestaw1.adj_matrix_to_list(adj_matrix)
    zestaw1.print_list(adj_list)
    zestaw1.print_adj_matrix(adj_matrix)
    zestaw1.print_i_matrix(im_m)