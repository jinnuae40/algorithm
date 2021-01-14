from multiprocessing import Pool
import os


def f(x):
    print(os.getpid())
    return x*x


if __name__ == '__main__':
    with Pool(5) as p:
        p.map(f, [i for i in range(9000)])
