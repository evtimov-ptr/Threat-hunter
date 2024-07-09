import os
import re
import subprocess
import sys
from dotenv import load_dotenv

import requests

load_dotenv()
def get_network_connections():
    if os.name == 'nt':
        command = "netstat -ano"
    else:
        command = "netstat -tunapl"

    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

def extract_ip_addresses(netstat_output):
    ip_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+)')
    return set(ip_pattern.findall(netstat_output))

def check_ip_against_threat_intel(ips):
    api_key = os.getenv('ABUSEIPDB_API_KEY')
    api_url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        "Accept": "application/json",
        "Key": api_key,
    }

    results = {}

    for ip in ips:
        response = requests.get(api_url, headers=headers, params={"ipAddress": ip})
        if response.status_code == 200:
            data = response.json()
            results[ip] = data
        else:
            results[ip] = {
                "error": "Failed to retrieve data"
            }
    return results

def read_ips_from_file(file_path):
    with open(file_path, 'r') as file:
        ips = file.read().splitlines()
        ips = [ip.strip().strip(',') for ip in ips]
    return ips

def main():
    if len(sys.argv) != 2:
        print("Usage of ThreatHunter: threat_hunter.py <list_of_ips>.txt")
        sys.exit(1)

    ip_list_file = sys.argv[1]

    if os.path.getsize(ip_list_file) == 0:
        print("Error: File is empty. Please try again!")
        sys.exit(1)

    if not  os.path.isfile(ip_list_file):
        print(f"File {ip_list_file} does not exist. Try again!")
        sys.exit(1)


    ip_addresses = read_ips_from_file(ip_list_file)
    results = check_ip_against_threat_intel(ip_addresses)

    for ip, data in results.items():
        print(f"IP: {ip}, Data: {data}")

if __name__ == "__main__":
    main()