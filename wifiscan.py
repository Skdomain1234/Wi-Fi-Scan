import pywifi
from pywifi import const
import time
import csv

def wifi_scan():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # Select first network interface
    iface.scan()  # Start scanning
    time.sleep(3)  # Wait for scan to complete
    results = iface.scan_results()

    # Save to TXT file
    with open("wifi_list.txt", "w") as txt_file:
        for network in results:
            txt_file.write(f"SSID: {network.ssid}, Signal: {network.signal} dBm\n")

    # Save to CSV file
    with open("wifi_list.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["SSID", "Signal (dBm)"])
        for network in results:
            writer.writerow([network.ssid, network.signal])

    print("---------------------------------------------")
    print(f"| {'SSID':25} | {'Signal (dBm)':12} |")
    print("---------------------------------------------")
    for network in results:
       print(f"| {network.ssid:25} | {network.signal:12} |")
       print("---------------------------------------------")



if __name__ == "__main__":
    wifi_scan()
    
