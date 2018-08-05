# The function arranges the given string with proper casing.
# The function also lower cases all the words mentioned in the second argument as exceptions

def title_case(title, minor_words=''):
    ans = []
    title = title.title()
    title=title.split()
    minor_words=minor_words.title()
    minor_words=minor_words.split()
    for index, item in enumerate(title):
        if index==0:
            ans.append(item)
        else:
            if item not in minor_words:
                ans.append(item)
            else:
                item=item.lower()
                ans.append(item)
    return ' '.join(ans)
