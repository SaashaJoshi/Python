# The function capitalizes first letter of each word of the string

def upperCase(string):
    str=string.split()
    nstr=[]
    for word in str:
        word=word.capitalize()
        nstr.append(word)
    return ' '.join(nstr)
