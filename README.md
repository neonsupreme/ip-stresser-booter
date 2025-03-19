# 🚀 Python IP Stresser / IP Booter DDOS V2.0

Say hello to **Python DDOS V2.0!** 🎉 Your ultimate **IP Stresser** and **IP Booter**, packed with powerful flood methods. Whether it's **UDP DDOS tools**, **TCP DDOS tools**, or **HTTP/HTTPS floods**, this Python-powered beast is built for network testing professionals. Test your servers like a pro with this slick **DDOS tool**! 💪

⚠️ **Disclaimer:** For **educational use and authorized testing only!** Only flood servers you own or have permission for. **Illegal use is strictly prohibited!** 🚨

---

## ✨ Features

### 🔧 Flood Protocols:

#### **UDP Floods 🌊 (UDP DDOS Tool):**
- **Plain**: Fixed-payload packets for steady streams. 📦
- **Random**: Random payloads for unpredictable chaos. 🎲
- **Burst**: 10-packet bursts with short pauses. 💥
- **Spoof**: Simulates random source IPs (non-raw spoofing). 🕵️
- **Frag**: Sends fragmented packets in two parts. 🧩

#### **TCP Floods ⚡ (TCP DDOS Tool):**
- **SYN Flood (Single)**: SYN packets to clog connections. 🎯
- **SYN Flood (Multi-threaded)**: 10-thread SYN chaos. 🧵
- **Data Flood (Single)**: Data blasts after connecting. 💾
- **Data Flood (Multi-threaded)**: 10-thread data storm. 🌩️
- **ACK Flood**: Small ACK-like packets post-connection. 📡
- **RST Flood**: Rapid connect-and-close for RST packets. 🔄
- **XMAS Flood**: All-flags packets for confusion. 🎄

#### **HTTP/HTTPS Floods 🌐 (IP Stresser):**
- **GET Flood**: Barrages servers with GET requests. 📡
- **POST Flood**: Slams servers with POST data. 📨
- **Slowloris (HTTPS)**: Slow connection buildup to exhaust resources. 🐢

### 🎨 Customization:
- **Target IP & port (1-65535)** for precise **IP booter** action. 🎯
- **Flood duration** in seconds—your call! ⏱️
- **Packet size (1-65500 bytes)** for UDP & TCP Data floods. 📏
- **TCP styles**: Single socket or 10-thread multi-threaded mayhem! 🧵

### 🖥️ Slick Interface:
- **ASCII art intro** with "Made by elitestresser.club". 🎨
- **Colorful output**: Cyan (start), Green (done), Red (errors). 🌈
- **Emojis**: Rockets (🚀), checks (✅), crosses (❌) for flair. ✨
- **Packet/request counts** after every flood. 📊
- **Window Title**: "Python DDOS V2.0 By elitestresser.club". 😎

🌟 **Made by [elitestresser.club](https://elitestresser.club):** Network testing legends! 🔥

---

## 🛠️ Installation

### 📋 Prerequisites
- **Python 3.x**: [Download here](https://www.python.org/downloads/) 🐍
- **A terminal** (Command Prompt, PowerShell, Linux Terminal) 💻

### 🚀 Steps

#### Clone the Repo:
```bash
git clone <your-repo-url>
cd python-ddos-v2.0
```

#### Install Dependencies:
```bash
pip install colorama requests
```
- **colorama**: For that colorful console magic. 🌈
- **requests**: For HTTP/HTTPS flood power. 🌐

#### Run It:
```bash
python ddos_tool.py
```
📜 Rename `ddos_tool.py` to your script’s filename!

---

## 🎮 Usage

### 1️⃣ **Launch the Tool**
Run it, and the title switches to **"Python DDOS V2.0 By elitestresser.club"**. You'll see:

```plaintext
 ____  ____   ____  _____    ____  ____    ____    ____ 
/    ||    \ |    ||     |  /    ||    \  /    |  /    |
|  o  ||  o  )|  o  ||   | |  o  ||  o  )|  o  | |   _|
|     ||     ||     ||  |  |     ||     ||     | |  |  |
|  _  ||  O  ||  _  ||   ] |  _  ||  O  ||  _  | |  |  |
|  |  ||     ||  |  ||  |   |  |  ||     ||  |  | |   _] |
||||||||||   |||||||| |__|

Python DDOS v2.0 - Made by elitestresser.club
```

### 2️⃣ **Choose Your Attack:**
- `1` for **UDP** 🌊
- `2` for **TCP** ⚡
- `3` for **HTTP/HTTPS** 🌐

### 3️⃣ **Set It Up:**
- **UDP**: Select method (1-5), enter IP, port, duration, packet size.
- **TCP**: Select method (1-7), enter IP, port, duration (packet size for Data Floods).
- **HTTP/HTTPS**: Select method (1-3), enter URL, duration.

#### **Example Runs**
##### 🌀 **UDP Burst Flood**
```plaintext
[🚀] UDP Burst Flood on 192.168.1.100:12345 | 1024 bytes | 5s...
[✅] Done! Sent 500 packets.
```

##### ⚡ **TCP XMAS Flood**
```plaintext
[🚀] TCP XMAS Flood on 192.168.1.100:80 | 5s...
[✅] Done! Sent 1234 XMAS packets.
```

##### 🌍 **HTTPS Slowloris**
```plaintext
[🚀] HTTPS Slowloris on https://192.168.1.100 | 10s...
[✅] Done! Opened 98 connections.
```

---

## 🧠 How It Works
- **UDP DDOS Tool** 🌊: Overloads ports with packets—plain, random, bursts, spoofed, or fragmented.
- **TCP DDOS Tool** ⚡: Clogs connections (SYN/RST), floods data, or confuses with ACK/XMAS packets.
- **IP Stresser** 🌐: Hammers web servers with GET/POST floods or slow HTTPS attacks.
- **IP Booter** 🎯: Targets IPs and ports with precision.

📈 See your flood’s impact with detailed **packet/connection counts!**

---

## 🙌 Credits

**Made by [elitestresser.club](https://elitestresser.club)** 🌟  
Built by the **network testing gurus** at [elitestresser.club](https://elitestresser.club), your home for top-tier **IP stresser** and **IP booter** tools. Visit us for more firepower! 🔥

---

## 📜 License

**For educational and legal testing only.** No formal license—use wisely and **respect the law!** ⚖️

---

## 🔑 Keywords
- 🌐 IP Stresser
- 🎯 IP Booter
- 💥 DDOS Tool
- 🌊 UDP DDOS Tool
- ⚡ TCP DDOS Tool
