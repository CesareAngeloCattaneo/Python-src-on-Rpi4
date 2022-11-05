def sum_all_num(*args):
    total = 0
    for num in args:
        total += num
    return total
        
print(sum_all_num(1, 4 ,5, 8))
