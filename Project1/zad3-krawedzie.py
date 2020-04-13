import zestaw1

if __name__ == "__main__":
    adj_matrix = zestaw1.gen_G_l(8, 8)
    i_matrix = zestaw1.adj_matrix_to_i_matrix(adj_matrix)
    adj_list = zestaw1.adj_matrix_to_list(adj_matrix)
    zestaw1.print_list(adj_list)
    zestaw1.print_adj_matrix(adj_matrix)
    zestaw1.print_i_matrix(i_matrix)