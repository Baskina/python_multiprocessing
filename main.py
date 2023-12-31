import logging
import time
from multiprocessing import Pool, cpu_count


def number_calculation(number):
    list_of_factors = []
    for n in range(1, number + 1):
        if number % n == 0:
            list_of_factors.append(n)
    return list_of_factors


def factorize_sync(*numbers):
    result = []
    for number in numbers:
        result.append(number_calculation(number))
    return result


def factorize_with_process(*numbers):
    with Pool(cpu_count()) as pool:
        result = pool.map(number_calculation, numbers)
    return result


def test():
    a, b, c, d = factorize_sync(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]

    a, b, c, d = factorize_with_process(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106,
                 1521580, 2130212, 2662765, 5325530, 10651060]


def main():
    start = time.perf_counter()
    factorize_sync(128, 255, 99999, 10651060)
    end = time.perf_counter()
    logging.info(f"Time synchronized code: {end - start}")

    start = time.perf_counter()
    factorize_with_process(128, 255, 99999, 10651060)
    end = time.perf_counter()
    logging.info(f"Time with multiprocessing code: {end - start}")
    test()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    main()
