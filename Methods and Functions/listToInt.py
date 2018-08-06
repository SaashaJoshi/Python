# This function squares every digit of a number.

def square_digits(num):
    final=[]
    x=map(int, str(num))
    for y in x:
        y=y**2
        final.append(y)
    final=map(str, final)
    return int(''.join(final))
