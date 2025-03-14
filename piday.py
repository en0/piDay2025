import math
from argparse import ArgumentParser
from time import sleep


def get_opts():

    description=(
        "PiDay 2025 using a modified version of gosphers spigot "
        "algorithm. This algorithm is unproven but still fun to code."
    )
    ap = ArgumentParser(description=description)

    ap.add_argument(
        '-d', '--digits',
        help="Limit the output to n digits of pi. Default = infinity",
        default=math.inf,
        type=float
    )
    ap.add_argument(
        '-s', '--sleep',
        help="The amount of time to sleep between printinig digit of "
             "pi, because it looks cool. Default=0.25",
        default=0.25,
        type=float
    )

    return ap.parse_args()


def gibbons_conjector_for_gosphers_pi_spigot():
    """
    A spigot algorithm to compute pi based on Gosphers algorithm.

    This algorithm is a modified  versoin of Gosphers algorithm depending
    on a unproven conjection from Jeremy Gibbons. Read the full paper here:
    https://www.cs.ox.ac.uk/jeremy.gibbons/publications/spigot.pdf
    """
    q = 1
    r = 180
    t = 60
    i = 2

    while True:

        u = 3 * (3 * i + 1) * (3 * i + 2)
        y = (q * (27 * i - 12) + 5 * r) // (5 * t)

        r = 10 * u * (q * (5 * i - 2) + r - y * t)
        q = 10 * q * i * (2 * i - 1)
        t = t * u

        yield y

        i = i + 1


def main():

    opts = get_opts()

    pi = gibbons_conjector_for_gosphers_pi_spigot()

    n = 0
    while n < opts.digits:
        print(next(pi), end="", flush=True)
        sleep(opts.sleep)
        if n == 0:
            print('.', end="", flush=True)
            sleep(opts.sleep)
        n += 1

if __name__ == "__main__":
    main()
