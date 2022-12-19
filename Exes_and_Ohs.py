
def xo(s):
    s = s.lower()
    ohs = 0
    exes = 0
    for item in s:
        if item == 'o':
            ohs = ohs + 1
        if item == 'x':
            exes = exes + 1
    if ohs == exes:
        return True
    else: 
        return False
    





if __name__ == "__main__":
    assert(xo('xo'), True)
    assert(xo('xo0'), 'True expected')
    assert(not xo('xxxoo'), 'False expected')