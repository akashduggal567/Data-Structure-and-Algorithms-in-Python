def check_powerof2(num):
    """num      num-1  """
    """4-->100  3-->011"""

    if (num and (num&num-1==0)):
        print(num,"is a power of 2")
    else:
        print(num,"is not a power of 2")

check_powerof2(32)


