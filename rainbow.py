color = int(input('input color 1 - 6 '))
col = {
    1: 'white',
    2: 'blue',
    3: 'green',
    4: 'red',
    5: 'yellow',
    6: 'orange'
}

if color >= 1 or color <=6:
    print(col[color], col[color - 1], col[color + 1])
else:
    print("input color 1 to 6!!!")







