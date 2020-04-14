def if_smaller_than_0_exist(seq):
    for el in seq:
        if el < 0:
            return True
    else:
        return False

def is_graphic_seq(seq):
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
            print(seq)


        seq[0] = 0
        seq.sort(reverse=True)