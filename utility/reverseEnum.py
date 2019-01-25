def reverseEnumerate(thing):
    l=len(thing)
    for i,item in enumerate(reversed(thing)):
        yield l-i-1, item