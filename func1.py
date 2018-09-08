def get_summ(one, two, delimeter = '&'):
    a =str(one) + str(delimeter) + str(two)
    return a.upper()
print(get_summ('art', 'tru'))