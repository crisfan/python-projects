a = [1, 2, 3]
try:
    raise IndexError, IndexError('ssss')
except IndexError, e:
    print type(e)

