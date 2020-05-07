import functions

seq = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
seq = [2, 4, 4, 4, 4, 4, 2]
seq = [4, 2, 3, 2, 1]
seq = [7, 5, 3, 4, 1, 7, 5, 4, 4, 4]
# seq = [4, 4, 3, 1, 2] # nie da sie

g = functions.create_graph(seq)
if g:
    print("Wprowadzony ciąg:", seq)
    g.print_adj_list()
    g.print_adj_matrix()
    g.print_i_matrix()



