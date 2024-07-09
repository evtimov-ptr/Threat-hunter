# ThreatHunter

ThreatHunter is a Python tool designed to gather network connection information and check it against a threat intelligence platform to identify potential threats.

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

4. **Finally, you can now execute the script using threat_hunter.py <list_of_ip_addresses>.txt**