init = 1
init_cached = 0
while init <= 1597:
    print(init)
    init += init_cached
    init_cached = init - init_cached

