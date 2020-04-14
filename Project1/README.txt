zestaw1.py - program



FileIn - plik z danymi wejściowymi
Musi mieć strukture:

W pierwszej lini musimy podać co podajemy:
A - macierz sąsiedztwa
I - macierz incydencji
L - listę sąsiedztwa
macierz lub lista ma być bezpośrednio pod literką
nie może być nigdzie pustych linii, ani przed ani po danych
przykładowe pliki:

L
1: 2 5
2: 1 3 4 5
3: 2 4
4: 2 3 5
5: 1 2 4

A 
0 1 0 0 1
1 0 1 1 1
0 1 0 1 0
0 1 1 0 1
1 1 0 1 0

I
1 0 0 0 1 0 0
1 1 1 0 0 1 0
0 1 0 1 0 0 0
0 0 1 1 0 0 1
0 0 0 0 1 1 1

Przykladowe - przykładowe dane wejściowe



Adj.txt - plik potrzebny do rysowania grafów
Z niego odczytywane są dane do narysowania grafu