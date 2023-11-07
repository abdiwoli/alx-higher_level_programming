#!/usr/bin/python3

import sys
import signal
from collections import defaultdict

total_file_size = 0
status_code_counts = defaultdict(int)

# Define a function to print metrics
def print_metrics():
    print("File size:", total_file_size)
    for status_code in sorted(status_code_counts.keys()):
        count = status_code_counts[status_code]
        if count != 0:
            print(f"{status_code}: {count}")
        # Reset the count to 0
        status_code_counts[status_code] = 0

# Function to handle keyboard interruption (CTRL + C)
def handle_interrupt(signal, frame):
    print_metrics()
    sys.exit(0)

# Set up the interrupt signal handler
signal.signal(signal.SIGINT, handle_interrupt)

line_count = 0

# Process lines from stdin
for line in sys.stdin:
    line_count += 1
    parts = line.split()
    if len(parts) >= 8:
        status_code = parts[-2]
        file_size = int(parts[-1])

        # Update metrics
        total_file_size += file_size
        status_code_counts[status_code] += 1

    if line_count % 10 == 0:
        print_metrics()
        line_count = 0

# Print the final metrics
print_metrics()
