# Basic Network Sniffing(Passive Sniffing)

##  Project Overview

This is a basic **Basic Network Sniffing(Passive Sniffing)** written in Python, built as a networking internship task.

The program **listens to network traffic on the local machine's network interface** and captures **40 packets**, displaying basic information about each one (source/destination IP, protocol, ports, and packet size).

The program only **reads and observes** packets that are already passing through the local network interface. It does not send, inject, modify, redirect, or alter any network traffic in any way.

---

##  Why "Passive" and not "Active" Sniffing

These two terms are often confused, so it's worth being precise:

* **Passive sniffing** — capturing and reading packets that are already visible on the network interface, without sending anything onto the network or interfering with traffic in any way. This is what this program does.
* **Active sniffing** — techniques that involve injecting traffic into the network to force otherwise-invisible traffic to become visible (for example, ARP spoofing/poisoning on a switched network). This program does **not** do this — it never sends or crafts any packets.

This project only uses Scapy's `sniff()` function to **listen**. No packets are ever sent, spoofed, or injected. It is correctly classified as **passive sniffing**.

---

##  Objective

* To understand the basic concept of passive network sniffing.
* To learn how network packets can be captured and read using Python.
* To observe real network traffic on a local machine.
* To inspect packet-level information such as source/destination IP, protocol, and ports.
* To understand how a packet-capturing library like Scapy works under the hood.

---

##  Features

* Passively captures **40 packets** from the local network interface.
* Displays source IP, destination IP, protocol, source port, and destination port.
* Identifies TCP, UDP, and ICMP traffic separately.
* Displays packet size in bytes.
* Detects and handles non-IP packets (such as ARP) separately, since they don't carry the same header fields.
* Stops automatically after 40 packets, or can be stopped manually with `Ctrl+C`.
* Does not send, modify, or inject any traffic — read-only observation.

---

##  Technologies Used

* **Python 3**
* **Scapy** — Python library used to capture and read network packets.
* **Npcap** (Windows only) — driver required by Scapy to access raw packets on Windows.

---

##  Requirements

* Python 3.x installed.
* Scapy library installed (`pip install scapy`).
* An active network interface (Wi-Fi or Ethernet) connected to the local network.
* Administrator/root privileges, since reading raw packets is a privileged operation.
* **Windows only:** Npcap installed, with **"Install Npcap in WinPcap API-compatible Mode"** checked during setup — without this, Scapy cannot access packets on Windows.

---

##  Installation & Setup — Full Steps

1. **Install Python 3** from [python.org](https://www.python.org/) if not already installed. Verify with:
   ```bash
   python --version
   ```

2. **Install Scapy:**
   ```bash
   pip install scapy
   ```

3. **(Windows only) Install Npcap:**
   - Download from [npcap.com/#download](https://npcap.com/#download)
   - Run the installer **as Administrator**
   - During setup, check the box **"Install Npcap in WinPcap API-compatible Mode"**
   - Restart the PC after installation

4. **Save the script** as `cloud-sniff.py` in your project folder.

---

##  How to Run

Packet sniffing requires elevated/administrator privileges, since it reads raw traffic directly from the network interface.

**Windows:**
- Open your code editor or terminal **as Administrator**
- Run:
  ```bash
  python network-sniffing.py
  ```

**Linux / Mac:**
```bash
sudo python3 network-sniffing.py
```

The program will start listening immediately and stop automatically once 40 packets are captured. Press `Ctrl+C` to stop earlier if needed.

---

##  How the Program Works

1. The program starts listening on the local network interface.
2. Every time a packet passes through the interface, Scapy calls a function (`process_packet`) to handle it — this is a **callback function**, given to `sniff()` through its `prn` parameter.
3. For each packet, the program checks if it has an IP layer. If it does, it identifies whether it's TCP, UDP, or ICMP, and prints the relevant source/destination IP and ports.
4. If the packet doesn't have an IP layer (e.g., ARP), it's handled separately and shown with Scapy's built-in summary.
5. A separate function (`stop_filter`) checks after every packet whether 40 packets have been reached — once true, sniffing stops automatically.

### Basic Flow

```text
Start Program
      ↓
Listen on Local Network Interface (passive — read only)
      ↓
Packet Arrives → process_packet() runs automatically
      ↓
Check Protocol (TCP / UDP / ICMP / Other / Non-IP)
      ↓
Display Packet Information
      ↓
Check if 40 Packets Reached (stop_filter)
      ↓
Stop Sniffing
      ↓
End Program
```

---

##  Packet Information Displayed

* Source IP address
* Destination IP address
* Protocol (TCP / UDP / ICMP / Other)
* Source port (TCP/UDP only)
* Destination port (TCP/UDP only)
* Packet size (in bytes)

Non-IP packets (such as ARP) don't have these fields, so they are shown using Scapy's built-in packet summary instead.

---

##  Example Output

```text
Starting Packet Sniffer...
Capturing 40 packets
Press CTRL+C to stop

============================================================
Packet #1  |  Time: 12:16:52
============================================================
Source IP       : 192.168.0.123
Destination IP  : 57.144.43.32
Protocol        : TCP
Source Port     : 64620
Destination Port: 443
Packet Size     : 128 bytes

============================================================
Packet #2  |  Time: 12:16:52
============================================================
Source IP       : 57.144.43.32
Destination IP  : 192.168.0.123
Protocol        : TCP
Source Port     : 443
Destination Port: 64620
Packet Size     : 280 bytes

...

Done. Total packets captured: 40
```

Actual output will vary depending on the real traffic present on the network while the program runs.

---

##  Ethical and Legal Considerations

Passive sniffing on your own local network — capturing packets sent to/from your own devices — is what this program does, and is generally safe for personal learning.

* Only run this on a network you **own or are explicitly authorized to monitor** (e.g., your own home network, or a lab network provided for this purpose).
* Do not use this on a network you don't own or don't have permission to monitor (e.g., public Wi-Fi, a neighbour's network, an employer's network without authorization) — this can be illegal.
* This program does not decrypt encrypted traffic (like HTTPS content) — it only reads packet headers (IPs, ports, protocol, size), not private message content.
* No data is transmitted anywhere outside the local machine; nothing is saved to disk unless explicitly added.

---

##  Limitations

* Captures a fixed number of packets: **40**.
* Passive only — it cannot see traffic that a switch doesn't deliver to this machine's interface (unlike active techniques such as ARP spoofing).
* Does not decrypt encrypted traffic (e.g., HTTPS payloads) — only header-level metadata is visible.
* Visibility depends on OS permissions, network interface, and driver support (Npcap on Windows).
* Not a full-featured network monitoring/analysis tool — built for learning fundamentals.

---


##  Learning Outcomes

Beginners going through this project will learn:

* The actaul concept behind **passive sniffing** (reading existing traffic).
* How to use Scapy's `sniff()` function and its `prn` (callback) and `stop_filter` parameters.
* How to identify a packet's protocol layer (IP, TCP, UDP, ICMP) programmatically.
* Why raw packet capture requires administrator/root privileges.
* Why Windows specifically needs Npcap installed for Scapy to work.
* Basic Python concepts used along the way: f-strings, `global` variables, callback functions, and conditional layer checks.

---

##  Possible Future Improvements

* Filter packets by a specific protocol (e.g., only TCP or only DNS).
* Save captured packet data to a `.pcap` file for later analysis in Wireshark.
* Add packet statistics (e.g., count per protocol).
* Build a simple GUI for live display.

---

##  Project Summary

**Project Name:** Basic Network Sniffing Program
**Language:** Python
**Library:** Scapy
**Sniffing Type:** Passive (read-only, no packet injection or traffic alteration)
**Packet Capture Limit:** 40 packets
**Environment:** Local machine / authorized network only 

---

##  Disclaimer

This project was built for educational purposes as part of a networking internship task. It performs passive, read-only packet observation on the local network and does not send, inject, or alter any network traffic. It should only be run on networks and devices the user owns or is explicitly authorized to monitor.
