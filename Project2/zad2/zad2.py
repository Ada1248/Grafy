import random

random.seed()

i_matrix = []

print("Podaj liczbe randomizacji: ")
randomize_num = int(input())

#funkcja czyta plik wejsciowy, w finalnej wersji trzeba dołączyć do zad2 zadanie 1
#z podanego ciagu graficznego wygenerować graf, ustalić jego macierz incydencji i ją dalej losować

def read_file():
    with open('input.txt', 'r+') as file:
        for line in file:
            row = []
            for element in line.strip().split(" "):
                row.append(int(element))
            i_matrix.append(row)

#funkcja przelesowująga graf, arg.wesjciowe: liczba krawedzi, liczba zamian
def randomize_graph(edge_num, randomize_num):
    succesfull_swaps = 0
    while True:
        line1 = line2 = int(random.random() * edge_num - 1)
        while line1 == line2:  # losuje krawedzie ktore maja zostac zamienione
            line2 = int(random.random() * edge_num - 1)

        first_edge = [] # indeksy a b
        second_edge = [] # ideksy c d

        for i in range(len(i_matrix)):
            if i_matrix[i][line1] == 1:
                first_edge.append(i)
            if i_matrix[i][line2] == 1:
                second_edge.append(i)

        may_be_swapped = True
        for i in range(0, len(i_matrix[0])):
            if (i_matrix[first_edge[0]][i] == 1 and i_matrix[second_edge[1]][i] == 1) or (
                    i_matrix[first_edge[1]][i] == 1 and i_matrix[second_edge[0]][i] == 1):
                may_be_swapped = False

        if may_be_swapped:
            i_matrix[first_edge[1]][line1] = 0
            i_matrix[second_edge[1]][line1] = 1
            i_matrix[second_edge[1]][line2] = 0
            i_matrix[first_edge[1]][line2] = 1
            succesfull_swaps += 1

        with open("output.txt", 'w') as file:
            file.writelines(' '.join(str(j) for j in i) + '\n' for i in i_matrix)

        if succesfull_swaps == randomize_num:
            break



read_file()
randomize_graph(len(i_matrix[0]), randomize_num)
