def check_kbit(num,k):
    """step-1 : find a number whose kth bit is set"""
    n = 1<<(k-1)
    """step-2 : AND the number found with the given num"""
    num&n

    if (num&n != 0):
        print(k,"bit is set")
    else:
        print(k,"bit is not set")



check_kbit(5,1)