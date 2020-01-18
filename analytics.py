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
    # return np.log10(n) + 1
    return (np.sqrt(n)) / n + np.log10(n)
    # return np.log10(n) + np.sqrt(n)

    # return 0.001 * np.sqrt(n)
    # return n
    # return np.log10(n) * (np.log10(n) + np.sqrt(n))


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
    plt.plot(n_list, q)
    plt.title('q')
    plt.ylabel('q')
    plt.xlabel('n')
    plt.show()


def graph(analytics_results, args):
    _, ax1 = plt.subplots()

    color = 'tab:blue'
    ax1.set_xlabel('n')
    ax1.set_ylabel('time(n)', color=color)
    ax1.plot(analytics_results["n_list"],
             analytics_results["measured_times"],
             color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()

    color = 'tab:red'
    ax2.set_ylabel('prime palindrome (n)', color=color)
    ax2.plot(analytics_results["n_list"],
             analytics_results["results"],
             color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title("initial_number={} k_samples={} \n repeats={} step={}".format(
        args.initial_number, args.k_samples, args.repeats, args.step))
    plt.savefig(args.graph)
    # plt.show()
