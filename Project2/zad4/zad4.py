import euler_cycle
import functions
import graph
import zestaw1


if __name__ == "__main__":
    # seq = [3, 5, 7, 1, 5, 9, 1] # ciąg nie graficzny

    # seq = [2, 2, 2, 2, 2, 2, 2] # ten najczęściej wymaga randomizacji
    # seq = [4, 1, 1, 3, 2, 3, 4, 1, 1] # ten też


    # seq = [2, 2, 2, 4, 4, 2, 2] # Eulerowski
    # seq = [4, 2, 2, 4, 2, 2, 4] # Eulerowski

    if_euleryan = True
    # if_euleryan = False
    seq = functions.generate_seq(11, if_euleryan)

    g = functions.create_graph(seq)

    if g:
        if if_euleryan:
            print("Wylosowana sekwancja - graf eulerowski", seq)
        else:
            print("Wylosowana sekwancja - graf randomowy", seq)

        g.print_adj_list()
        g.print_adj_matrix()
        g.print_i_matrix()
        g.print_conected_comps()


        if len(g.connected_comp()) != 1:
            print("\n\n\n---- RANDOMIZCJA ----")
            g = g.randomize_graph()
            

            print("\n\n\n Graf po randomizacji")
            g.print_adj_list()
            g.print_adj_matrix()
            g.print_i_matrix()
            g.print_conected_comps()

        if if_euleryan:
            print("\n\n\n---- WYZNACZAM CYKL EULERA ----")
            cycle = euler_cycle.euler_form_any_vertex(g, 5) # <- podajemy indeks wierzchołka startowego
            euler_cycle.print_euleryan_cycle(cycle)













# if __name__ == "__main__":
#     # i_matrix = [
#     #         [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#     #         [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
#     #         [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
#     #         [0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0],
#     #         [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
#     #         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
#     #         [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1]
#     #     ]
#     i_matrix = [
#             [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#             [1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
#             [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
#             [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
#             [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
#             [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
#             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
#         ]
#     adj_list = zestaw1.i_matrix_to_list(i_matrix)
#     g = graph.Graph(adj_list, i_matrix)
#     print("---- WYZNACZAM CYKL EULERA ----")
#     cycle = euler_cycle.euler_form_any_vertex(g, 5) # <- podajemy indeks wierzchołka startowego
#     euler_cycle.print_euleryan_cycle(cycle)
