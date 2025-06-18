def frequency(l, n):
    freq_dict = {}
    for x in l:
        freq_dict[x] = freq_dict.get(x, 0) + 1
    for i in freq_dict.keys():
        if i==n:
            return(freq_dict[i])
l = (list(map(int, input("Enter the list: ").split())))
x = int(input("Enter the number: "))
print(frequency(l, x))

