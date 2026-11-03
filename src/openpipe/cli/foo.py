# src/openpipe/cli/foo.py
import sys
from openpipe.core import say_hello

def main():
    print(say_hello())
    print("This is the foo command!")
    return 0

if __name__ == "__main__":
    sys.exit(main())