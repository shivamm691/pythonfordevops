#!/bin/bash

# Define the path to the log file and the output files
log_file_path="path/to/your/apache_log_file.log"
ip_file="ip_addresses.txt"
compressed_file="ip_addresses.txt.gz"

# Check if the log file exists
if [[ ! -f "$log_file_path" ]]; then
  echo "Log file does not exist: $log_file_path"
  exit 1
fi

# Extract IP addresses from the log file
grep -oP '\d+\.\d+\.\d+\.\d+' "$log_file_path" | sort | uniq > "$ip_file"

# Check if extraction and sorting were successful
if [[ $? -ne 0 ]]; then
  echo "Failed to extract and sort IP addresses."
  exit 1
fi

# Compress the IP addresses file
gzip "$ip_file"

# Check if compression was successful
if [[ $? -ne 0 ]]; then
  echo "Failed to compress the IP addresses file."
  exit 1
fi

echo "IP addresses have been extracted and compressed into $compressed_file"
