# The function takes in an integer, converts it to a list and returns a reversed list.

def digitize(n):
    listnum=map(int, str(n))
    
    return listnum[: :-1]
