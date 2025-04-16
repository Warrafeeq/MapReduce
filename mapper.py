# mapper.py
import sys

def map_line(line):
    # Split the line into words and emit key-value pairs: word and count 1.
    words = line.strip().split()
    for word in words:
        # Output format: word<TAB>1
        print(f"{word}\t1")

if __name__ == "__main__":
    # Read from standard input (provided by driver.py)
    for line in sys.stdin:
        map_line(line)
