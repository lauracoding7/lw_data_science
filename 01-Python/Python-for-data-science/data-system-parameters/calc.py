# pylint: disable=missing-module-docstring,missing-function-docstring,eval-used
import sys


def main():
    """Implement the calculator"""
    # YOUR CODE HERE
    return eval(f'{sys.argv[1]} {sys.argv[2]} {sys.argv[3]}')

if __name__ == "__main__":
    print(main())
