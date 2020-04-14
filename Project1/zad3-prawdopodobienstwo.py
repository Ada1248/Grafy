import zestaw1

if __name__ == "__main__":    
    adj_list = zestaw1.gen_G_p(6, 0.7)
    adj_matrix = zestaw1.adj_list_to_adj_matrix(adj_list)
    i_matrix = zestaw1.adj_list_to_i_matrix(adj_list)
    zestaw1.print_list(adj_list)
    zestaw1.print_adj_matrix(adj_matrix)
    zestaw1.print_i_matrix(i_matrix)