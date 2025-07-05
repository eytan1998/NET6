
# Final Project – Communication Networks

## 📋 Project Overview

This is a final project for a Communication Networks course. The system simulates an end-to-end network environment with implementations of DHCP, DNS, and a custom RUDP (Reliable UDP) protocol, alongside a user-facing GUI application that manages and queries a synagogue database. The system includes:

- 🖧 **DHCP Server & Client**
- 🌐 **DNS Server & Client**
- 📡 **Reliable UDP (RUDP) Protocol**
- 💻 **Graphical Interface (GUI) Application**
- 🔧 **TCP Alternative Communication**
- 🗃️ **Data Storage, Packet Handling, Logging**

---

## 🚀 Installation

To install and run the project, follow these steps on a Linux-based system:

```bash
sudo apt-get install git
git clone https://github.com/eytan1998/NET6.git
cd NET6

# Install Python and required packages
sudo apt install python3-pip
pip install --pre scapy[complete]
sudo pip install jsonpickle
```

---

## 📁 Project Structure

```
NET6/
├── Backend/
│   ├── Data/                # Server data storage
│   ├── Help/                # Helper utilities and packet logic
│   ├── RUDP/                # RUDP protocol implementation
│   ├── TCP/                 # TCP connection handling
│   ├── DHCP/                # DHCP client and server
│   └── DNS/                 # DNS client and server
├── Frontend/                # GUI application
├── server.py                # Server runner (TCP or RUDP)
├── App.py                   # Main application runner
└── Test/                    # Testing scripts
```

---

## 🧪 How to Run

### DHCP Server
```bash
sudo python3 DHCP/DHCPserver.py -H 127.0.0.1
```

### DNS Server
```bash
sudo python3 DNS/DNSserver.py -i lo -H 127.0.0.1
```

> For help:
```bash
sudo python3 DNS/DNSserver.py -h
```

### Reset Server Data
```bash
python3 Backend/Data/reserServer.py
```

### Main Server
- **RUDP**:
  ```bash
  sudo python3 server.py
  ```
- **TCP**:
  ```bash
  sudo python3 server.py --tcp
  ```

### GUI Application
- **RUDP**:
  ```bash
  sudo python3 App.py
  ```
- **TCP**:
  ```bash
  sudo python3 App.py --tcp
  ```

---

## 🛠 Features

### DHCP
- Dynamic IP assignment with lease management
- Support for initial request and renewal
- Handles broadcast messages and acknowledgements

### DNS
- Domain name resolution with local cache
- Fallback to Google DNS (8.8.8.8) on cache miss
- Records stored in `DNS/records.json`

### GUI Application
- User roles: Guest, Gabai, Admin
- Full CRUD for synagogues (only by gabai)
- Gabai management (only by admin)
- Search by city, nusach, or text
- Visual log of DNS and DHCP responses

### RUDP (Reliable UDP)
- Custom protocol over UDP with:
  - Sequence and acknowledgment numbers
  - Checksum validation
  - Segment handling and flow control
  - Triple handshake (SYN, ACK, FIN)
  - Congestion control (AIMD / Slow Start)

---

## 📊 Diagrams & Protocol Flow

- Connection setup and teardown
- Request/response handling
- Packet segmentation logic
- Wireshark examples for packet loss, corruption, renewals

---

## 🔐 Example Admin Credentials

```
ID: 1
Password: 1243
```

---

## ❓ FAQ & Questions

- **What’s the difference between QUIC and TCP?**
- **Compare CUBIC and Vegas congestion algorithms**
- **Explain BGP vs OSPF**

(All answered in detail inside the PDF document)

---

## 🔗 Repository

📎 [GitHub Repository](https://github.com/eytan1998/NET6)

---

## 👥 Credits

Developed as part of a final project for a communication networks course by [Eytan Ankri](https://github.com/eytan1998).
