def main( n ):
    return (n < 2)   or   ((2 < n) and main(n / 3) and ((n - n/3 * 3) < 2))
