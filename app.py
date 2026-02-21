#!/usr/bin/env python3
"""CalculatorPro placeholder application.

This is a minimal entrypoint used to package the project.  It currently
just prints a greeting, but real calculator functionality can be
implemented later.
"""

import argparse
from calculator import basic


def main():
    """Command-line interface for basic operations.

    Usage examples:
      python app.py add 2 3
      python app.py div 5 2
    """
    parser = argparse.ArgumentParser(description="CalculatorPro CLI")
    parser.add_argument("operation", choices=["add", "sub", "mul", "div", "pow"],
                        help="operation to perform")
    parser.add_argument("a", type=float, help="first operand")
    parser.add_argument("b", type=float, help="second operand")
    args = parser.parse_args()

    op = args.operation
    x, y = args.a, args.b

    try:
        if op == "add":
            result = basic.add(x, y)
        elif op == "sub":
            result = basic.subtract(x, y)
        elif op == "mul":
            result = basic.multiply(x, y)
        elif op == "div":
            result = basic.divide(x, y)
        elif op == "pow":
            result = basic.power(x, y)
        else:  # should never happen due to choices
            raise ValueError(f"unknown operation {op}")
    except Exception as exc:
        parser.error(str(exc))

    print(result)


if __name__ == "__main__":
    main()
