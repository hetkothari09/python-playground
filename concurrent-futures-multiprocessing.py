from concurrent.futures import ProcessPoolExecutor
from time import sleep

values = [2, 3, 4, 5, 6, 7]

def cube(x):
    return x**3


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=3) as exe:
        response = exe.submit(cube, 10)
        print(response)
        sleep(10)
        result = exe.map(cube, values)

    for i in result:
        print(i)


