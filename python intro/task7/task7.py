find_modified_max_argmax = lambda L,f: max(zip(L:=[f(x) for x in L if type(x) is int], range(len(L))),default=())

