def permute_with_size(input, size):
    if size == 0:
        yield []  # Yield an empty list for permutations of size == 0
    elif size == 1:
        for elem in input:
            yield [elem]  # Yield individual elements as permutations of size == 1
    else:
        for elem in input:
            rlist = input[:]
            rlist.remove(elem)
            for retlist in permute_with_size(rlist, size - 1):
                retlist.insert(0, elem)
                yield retlist

if __name__ == '__main__':
    input_list = ["a", "b", "c"]
    permutation_size = 2

    for permutation in permute_with_size(input_list, permutation_size):
        print(permutation)