init = 1
init_cached = 0
while 1 == 1:
    print(init)
    init = init + init_cached
    init_cached = init - init_cached
    if init > 1000:
        break
