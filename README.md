# MulticastFlooder
Multithreaded udp spam tool for simulating multicast traffic 

To use run in a command line 
Args are address, port, # of packets, # of threads, and the rate of transmission as a %
for example:
python mcastflooder 224.0.0.251 5353 500 5 50

to run until interrupted use 0 instead of a value for # of packets
example: python mcastflooder 224.0.0.251 5353 0 5 50

Use Ctrl + C to exit when using this mode.
