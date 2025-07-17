import random
import socket
from termcolor import colored  # pip install termcolor

# Render a big ASCII‑art banner using pyfiglet
banner = "PORT SCANNER"
print(colored(banner, "cyan", attrs=["bold"]))

# Create the scan_data dict with keys as (ip, port) tuples
scan_data = {}

for i in range(1, 25):
    # Random IP in private 192.168.x.y
    ip = f"192.168.{random.randint(0, 255)}.{random.randint(1, 254)}"
    # Random TCP port
    port = random.randint(1, 65535)
    
    # Perform the scan
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)
    result = sock.connect_ex((ip, port))
    sock.close()
    state = "open" if result == 0 else "closed"

    # Random date in DD-MM-YYYY
    day   = random.randint(1, 28)
    month = random.randint(1, 12)
    date  = f"{day:02}-{month:02}-2025"

    service = random.choice([
        "ftp", "ssh", "domain", "http", "pop3", "imap",
        "https", "imaps", "pop3s", ""
    ])
    reason = "syn-ack-ack" if state == "open" else "no-response"

    # Store data under the (ip, port) key
    scan_data[(ip, port)] = {
        "Date":    date,
        "State":   state,
        "Service": service or "-",   # display '-' if empty
        "Reason":  reason
    }

# Print header
header = f"{'DATE':<12} {'IP':<17} {'PORT':<7} {'STATE':<7} {'SERVICE':<8} REASON"
print(header)
print("-" * len(header))

# Print each scan result
for (ip, port), entry in scan_data.items():
    print(f"{entry['Date']:<12} {ip:<17} {port:<7} "
          f"{entry['State']:<7} {entry['Service']:<8} {entry['Reason']}")
