import argparse
import sys
import random
import matplotlib.pyplot as plt

import algorithm
import analytics


def do_io(args):
    for line in sys.stdin:
        if line == '\n':
            break
        n = int(line)
        result = algorithm.find_first_greater_prime_palindrome(n)
        print(result)
        if args.verify:
            analytics.compare_with_brute(n, result)


def do_random(args):
    samples = random.sample(range(0, 10**9), args.k_samples)
    for n in samples:
        result = algorithm.find_first_greater_prime_palindrome(n)
        print(str(n) + " " + str(result))
        if args.verify:
            analytics.compare_with_brute(n, result)


def do_analytics(args):
    analytics_results = analytics.measure_time(
        initial_number=args.initial_number,
        k_samples=args.k_samples,
        step=args.step,
        repeats=args.repeats)

    if args.table is not None:
        analytics.table(n_list=analytics_results["n_list"],
                        measured_times=analytics_results["measured_times"],
                        filename=args.table)

    if args.graph is not None:
        analytics.graph(analytics_results=analytics_results, args=args)

    if args.verify:
        analytics.compare_range_with_brute(
            n_list=analytics_results["n_list"],
            results=analytics_results["results"])


def main():
    parser = argparse.ArgumentParser(
        description=
        'Find first prime palindrome greater than a number from the range [0, 10^9].'
    )

    parser.add_argument(
        '-v',
        '--verify',
        action="store_true",
        default=False,
        help=
        'verify algorithm results with brute version, if verification fails, message will be printed to stdout'
    )

    subparsers = parser.add_subparsers(title="modes",
                                       dest="mode",
                                       help="select one of (required):")
    subparsers.required = True

    io = subparsers.add_parser(
        'stdio',
        help=
        'read new-line-separated numbers from stdio and write results to stdout',
        description=
        'read new-line-separated numbers from stdio and write results to stdout'
    )

    random = subparsers.add_parser(
        'random',
        help=
        'generate random numbers and solve problem for them, random -h for more details',
        description=
        'generate random numbers and solve problem for them, print tuples (number result) to stdout'
    )

    random.add_argument('-k',
                        '--k-samples',
                        type=int,
                        default=1,
                        help='number of samples to be generated')

    analytics = subparsers.add_parser(
        'analytics',
        help='algorytihm analytics mode, analytics -h for more details',
        description='generate multiple problem instances and do analytics')

    analytics.add_argument('-n',
                           '--initial-number',
                           type=int,
                           default=1,
                           help='number from which the analysis will start')

    analytics.add_argument('-k',
                           '--k-samples',
                           type=int,
                           default=1,
                           help='number of samples to be generated')

    analytics.add_argument('-s',
                           '--step',
                           type=int,
                           default=1,
                           help='difference between two next samples value')

    analytics.add_argument(
        '-r',
        '--repeats',
        type=int,
        default=1,
        help='number of times to repeat the time measurement for a given sample'
    )

    analytics.add_argument(
        '-t',
        '--table',
        help='filename where to save the time measurement results')

    analytics.add_argument(
        '-g',
        '--graph',
        help='filename where to save the time measurement graph')

    args = parser.parse_args()

    if args.mode == 'stdio':
        do_io(args)
    elif args.mode == 'random':
        do_random(args)
    elif args.mode == 'analytics':
        do_analytics(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
