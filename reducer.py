# reducer.py
import sys

def reduce_stream():
    current_word = None
    current_count = 0

    for line in sys.stdin:
        word, count = line.strip().split('\t')
        count = int(count)

        # If we are still processing the same word, sum the counts.
        if word == current_word:
            current_count += count
        else:
            # If moving to a new word, output the previous word and its count.
            if current_word is not None:
                print(f"{current_word}\t{current_count}")
            current_word = word
            current_count = count

    # Output the final word and count.
    if current_word is not None:
        print(f"{current_word}\t{current_count}")

if __name__ == "__main__":
    reduce_stream()
