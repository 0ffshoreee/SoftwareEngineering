print("y x z w")
for y in 0, 1:
    for x in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if ((not (y)) or x or ((not (z)) and w)) == 0:
                    print(y, x, z, w)
