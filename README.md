# 🔍 Port Scanner

## 📌 Project Overview

The Port Scanner is a Python-based cybersecurity tool that scans a target IP address or hostname to identify open TCP ports. It helps users understand which network services are accessible and demonstrates the fundamentals of network security and port scanning.

This project was developed as part of the **CodeTech Cyber Security Internship**.

---

## 🚀 Features

- Scan any valid IP address or hostname
- User-defined port range
- Detects open TCP ports
- Displays scan start and end time
- Handles invalid hostnames gracefully
- Simple command-line interface
- Beginner-friendly implementation

---

## 🛠️ Technologies Used

- Python 3
- Socket Module
- Datetime Module

---

## 📂 Project Structure

```
Port-Scanner/
│── port_scanner.py
│── README.md
```

---

## ▶️ Installation

1. Install Python 3 from https://www.python.org/
2. Clone this repository:

```bash
git clone https://github.com/yourusername/Port-Scanner.git
```

3. Open the project folder.

---

## ▶️ Run the Project

```bash
python port_scanner.py
```

---

## 💻 Example

**Input**

```
Target: scanme.nmap.org
Start Port: 20
End Port: 100
```

**Output**

```
==================================================
        PYTHON PORT SCANNER
==================================================

Scanning Target : scanme.nmap.org
Resolved IP     : 45.xxx.xxx.xxx

[OPEN ] Port 22
[OPEN ] Port 80

==================================================
SCAN COMPLETED
==================================================

Open Ports Found:
✔ Port 22
✔ Port 80

Total Open Ports: 2
```

---

## 📖 Learning Outcomes

- Understand the basics of TCP/IP networking
- Learn how port scanning works
- Use Python's Socket library for network programming
- Handle exceptions in Python
- Build a simple cybersecurity tool

---

## ⚠️ Disclaimer

This project is intended **only for educational and learning purposes**. Scan only systems and networks that you own or have explicit permission to test. Unauthorized port scanning may violate laws or network policies.

---

## 👩‍💻 Author

**Fahima Farkath U**

---

## 🆔 Internship Details

**Organization:** CodeTech IT Solutions

**Intern ID:** YOUR_INTERN_ID
