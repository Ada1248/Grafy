import copy
import graph
import operator
import random
import zestaw1

#flag:
#   True - Eulerowski
#   False - randomowy
def generate_seq(number, flag):
    for i in range(100):
        seq = random_even_seq(number) if flag else random_seq(number)
        if is_graphic_seq(seq):
            return seq

def random_even_seq(number):
    seq = []
    while len(seq) != number:
        el = random.randint(1, number)
        if el % 2 == 0:
            seq.append(el)
    return seq  

def random_seq(number):
    seq = []
    while len(seq) != number:
        seq.append(random.randint(1, number))
    return seq  

def if_smaller_than_0_exist(seq):
    for el in seq:
        if el < 0:
            return True
    else:
        return False

def is_graphic_seq(my_seq):
    seq = copy.deepcopy(my_seq)
    if len(seq) == 0 or sum(seq) == 0:
        return False

    number_of_odd = 0
    bigger = False
    for el in seq:
        if not el % 2 == 0:
            number_of_odd += 1
        if el >= len(seq):
            bigger = True 

    if not number_of_odd % 2 == 0 or bigger:
        return False

    seq.sort(reverse=True)
    while True:
        if all([el == 0 for el in seq]):
            return True

        if if_smaller_than_0_exist(seq) or seq[0] > len(seq):
            return False

        for i in range(1, seq[0] + 1):
            seq[i] -= 1
            # print(seq)


        seq[0] = 0
        seq.sort(reverse=True)


def create_graph(seq):
    seq_try = copy.deepcopy(seq)
    if is_graphic_seq(seq_try):
        seq_temp = [[index, value] for index, value in enumerate(seq)]

        adj_list = [[] for _ in range(len(seq_temp))]
        for _ in range(len(seq_temp)):
            seq_temp.sort(reverse=True, key=operator.itemgetter(1))
            i = 0
            j = i + 1
            while seq_temp[i][1] > 0 and j < len(seq_temp):
                adj_list[seq_temp[i][0]].append(seq_temp[j][0])
                adj_list[seq_temp[j][0]].append(seq_temp[i][0])
                seq_temp[i][1] -= 1
                seq_temp[j][1] -= 1
                j += 1

        for i in range(len(adj_list)):
            adj_list[i].sort()

        i_matrix = zestaw1.adj_list_to_i_matrix(adj_list)
        g = graph.Graph(adj_list, i_matrix)

        return g
    else:
        print("Nie da się wygenerować grafu z takiego ciągu")