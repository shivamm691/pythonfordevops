import re
import zipfile

# Regex pattern to extract IP addresses
rexp_ip = r".*\s(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*"

# Function to extract IP addresses from a log file
def extract_ips(log_file_path, output_file_path):
    ip_addresses = set()
    
    # Compile the regex pattern
    pattern = re.compile(rexp_ip)
    
    # Open the log file and extract IP addresses
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            match = pattern.match(line)
            if match:
                ip = match.group('ip')
                ip_addresses.add(ip)
    
    # Write the IP addresses to the output file
    with open(output_file_path, 'w') as output_file:
        for ip in sorted(ip_addresses):
            output_file.write(ip + '\n')

# Function to zip the output file
def zip_file(file_to_zip, zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        zipf.write(file_to_zip)

# Define file paths
log_file_path = 'tst.log'         # Input log file path
output_file_path = 'extracted_ips.txt' # Output file path for IP addresses
zip_file_path = 'extracted_ips.zip'    # Output zip file path

# Extract IP addresses and write to file
extract_ips(log_file_path, output_file_path)

# Zip the output file
zip_file(output_file_path, zip_file_path)

print(f"IP addresses extracted to {output_file_path} and zipped into {zip_file_path}.")
