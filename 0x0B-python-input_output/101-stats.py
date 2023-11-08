#!/usr/bin/python3
import time
import sys
import signal
import random
from collections import defaultdict

total_file_size = 0
status_code_counts = defaultdict(int)


# Define a function to print metrics
def print_metrics():
    print("File size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        if count != 0 and status_code.isdigit():
            print(f"{status_code}: {count}")
        # Reset the count to 0


# Function to handle keyboard interruption (CTRL + C)
# Function to handle keyboard interruption (CTRL + C)
def handle_interrupt(signal, frame):
    # Ensure line_count is a multiple of 10
    remainder = line_count % 10
    if remainder != 0:
        for _ in range(10 - remainder):
            print_metrics()
    sys.exit(0)


# Set up the interrupt signal handler
signal.signal(signal.SIGINT, handle_interrupt)

line_count = 0

# Process lines from stdin
for line in sys.stdin:
    line_count += 1
    parts = line.split()
    if len(parts) < 7:
        continue
    if len(parts) >= 8:
        status_code = parts[-2]
        file_size = int(parts[-1])

        # Update metrics
        total_file_size += file_size
        status_code_counts[status_code] += 1

    if line_count % 10 == 0:
        print_metrics()

    random_sleep = random.random()
    time.sleep(random_sleep)

# Print the final metrics
print_metrics()
