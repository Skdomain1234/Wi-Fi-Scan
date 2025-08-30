🔎 WiFi Scanner Tool (Python)
📌 Overview

This is a simple Python-based WiFi scanning tool that uses the pywifi library.
It scans for nearby WiFi networks, displays their details in a formatted table, and also saves the results into both .txt and .csv files for future use.

⚙️ Features

✅ Scan available WiFi networks.
✅ Display SSID and signal strength in a clean table format.
✅ Save results to wifi_list.txt (plain text).
✅ Save results to wifi_list.csv (spreadsheet compatible).



## 📦 Installation

Clone the repository and install dependencies:

```bash
sudo apt update
git clone https://github.com/Skdomain1234/Wi-Fi-Scan.git
cd Wi-Fi-Scan
pip install pywifi --break-system-packages
python wifiscan.py
