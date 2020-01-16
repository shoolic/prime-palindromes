# import math
import time
import matplotlib.pyplot as plt
import numpy as np
# import pandas as pd

import algorithm
import csv


def measure_time(initial_number, k_samples, step, repeats):
    n_range = range(initial_number, initial_number + k_samples * step, step)
    measured_times = []
    results = []

    for n in n_range:
        avg_time = 0
        result = 0
        for _ in range(0, repeats):
            start = time.process_time()
            result = algorithm.find_first_greater_prime_palindrome(n)
            avg_time += time.process_time() - start

        avg_time /= repeats

        measured_times.append(avg_time)
        results.append(result)

    return {
        "n_list": list(n_range),
        "results": results,
        "measured_times": measured_times
    }


def compare_with_brute(n, result):
    brute_result = algorithm.find_first_greater_prime_palindrome_brute(n)
    if result != brute_result:
        print("Unexpected algorithm result for " + str(n) + ": " +
              str(result) + ", should be " + str(brute_result))


def compare_range_with_brute(n_list, results):
    for idx, n in enumerate(n_list):
        compare_with_brute(n, results[idx])


def theoretical_complexity(n):
    # return np.log10(n)
    return np.sqrt(n)
    # return np.log10(n) + np.sqrt(n)


def calc_q(n_list, measured_times):
    median_idx = int(len(n_list) / 2)

    c = measured_times[median_idx] / theoretical_complexity(n_list[median_idx])

    q = []

    idx = 0
    while idx < len(n_list):
        q.append(measured_times[idx] /
                 (c * theoretical_complexity(n_list[idx])))
        idx += 1

    print(sum(q[3:median_idx]) / len(q[3:median_idx]))
    print(sum(q[median_idx:]) / len(q[median_idx:]))

    return q


def table(n_list, measured_times, filename):
    q = calc_q(n_list, measured_times)
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(zip(n_list, measured_times, q))
    # plt.yscale('log')
    # plt.xscale('log')
    # plt.plot(n_list, q)
    # plt.title('q')
    # plt.ylabel('q')
    # plt.xlabel('n')
    # plt.show()


def graph(n_list, measured_times, args):
    # plt.yscale('log')
    # plt.xscale('log')
    plt.plot(n_list, measured_times)
    # plt.plot(x2, y2, 'r', label = "aproks")
    plt.legend()
    plt.title('t(n)')

    plt.suptitle("initial_number={} k_samples={} repeats={} step={}".format(
        args.initial_number, args.k_samples, args.repeats, args.step))
    plt.ylabel('time')
    plt.xlabel('n')
    plt.savefig(args.graph)


# def do_analytics(initial_number, k_samples, step, repeats):
#      # N = int(input())
#     # print(find_first_greater_prime_palindrome(N))

#     #),
#     # *range(10 ** 3, 10 ** 6, 10 ** 3),
#     # *range(10 ** 6, 10 ** 9, 10 ** 6),
#     # *range(10 ** 9, 10 ** 12, 10 ** 9),
#     # ]
#     # x = [10 ** i for i in range(0, 19)]
#     # y = [1962.0, 1331.0, 23983.666666666668, 26955.333333333332, 28242.333333333332,  92946.0,  89794.0,  859859.0,  841767.3333333334,  14355312.666666666,  14802340.666666666,  125257132.33333333,  124933231.66666667,  1760593980.0,  1524281532.6666667,  12684118707.666666,  12860319183.333334,  137141924650.33333,  132122571410.33333]
#     # y = measure_time(x, 1000)
#     # y_b = measure_time_brute(x, 3)
#     # x2 = np.linspace(1, 10 ** 18, 100)
#     # y2 = np.sqrt(x2) * np.log10(x2)
#     # x2 = [10 ** i for i in range(0, 19)]
#     # y2 = [10 ** 3 + ((10 ** i) ** 0. * (math.log10(10 ** i) * 1)) for i in range(0, 19)]
#     # y2 = [ (10 ** i) ** 0.8 for i in range(0, 19)]
#     # y2 = [ 10 ** ( i + 1 ) for i in range(0, 19)]
