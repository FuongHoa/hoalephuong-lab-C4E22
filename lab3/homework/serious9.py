def get_even_list(l):
    new_list = []
    for i in l:
        if i % 2 == 0:
            new_list.append(i)
    print(new_list)
    return new_list