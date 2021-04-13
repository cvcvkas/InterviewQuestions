def cutrope(ropelength: int):
    rope_threes = ropelength // 3
    rope_remainder = ropelength % 3
    rope_twos = 0

    if (rope_remainder == 1):
        rope_threes -= 1
        rope_twos = 2
    elif (rope_remainder == 2):
        rope_twos = 1
            
    return (3 ** rope_threes) * (2 ** rope_twos)

print(cutrope(8));
print(cutrope(9));
print(cutrope(10));