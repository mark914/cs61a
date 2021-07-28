def countdown(k):
    if k > 0:
        print(k)
        return countdown(k-1)

def countdown_gen(k):
    if k > 0:
        yield k
        yield from countdown_gen(k-1)
    else:
        yield 'Blast off'