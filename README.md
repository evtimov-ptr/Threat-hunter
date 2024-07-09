# ThreatHunter

ThreatHunter is a Python tool designed to gather network connection information and check it against a threat intelligence platform to identify potential threats.

## Preview

- Windows Preview ![Windows Preview](https://github.com/evtimov-ptr/Threat-hunter/blob/master/images/image1.png)
- Linux Preview ![Windows Preview](https://github.com/evtimov-ptr/Threat-hunter/blob/master/images/image2.png)
- macOS Preview ![Windows Preview](https://github.com/evtimov-ptr/Threat-hunter/blob/master/images/image3.png)

## Installation

1. **First you need to clone the repository**
   ```sh
    git clone https://github.com/yourusername/ThreatHunter.git
    cd ThreatHunter
    ```
   
2. **Make the setup.sh as an executable and run the script**
   ```sh
    sudo chmod +x setup.sh
    ./setup.sh
    ```
3. **In the script folder type the following. By doing this you activate the virtual environment**
   ```sh
   Linux, macOS: source venv/bin/activate
   Windows: venv\Scripts\activate
   ```
4. **Create .env file in the root and paste the following, where the empty string is your API Key**
   ```sh 
   ABUSEIPDB_API_KEY=""
   ```
   
5. **Finally, you can now execute the script using threat_hunter.py <list_of_ip_addresses>.txt**

# Compatibility

ThreatHunter has been tested and confirmed working on the following systems:

* Windows 11 Build 22631
* macOS Sonoma 14.5
* Debian 12
