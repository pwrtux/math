# Calculate Stirling numbers of the second kind

def stirling(n, k):
    k_tmp = k
    n_tmp = n

    if n <= 0:
        return 1

    if k == 0:
        return 0

    if k == 1:
        return 1
    
    if n != 0 and n == k:
        return 1

    if k == 2:
        tmp_calc = (2 ** (n - 1)) - 1
        return tmp_calc
    else:
        recursion = stirling(n_tmp -1, k_tmp)
        recursion = k_tmp * recursion
        return (k_tmp * (stirling(n_tmp - 1, k_tmp))) + stirling(n_tmp -1, k_tmp -1)

    

#print(stirling(6, 4))