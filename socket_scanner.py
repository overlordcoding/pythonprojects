from socket import *
import time
startTime = time.time()
print("""
𝓟𝓸𝓻𝓽 𝓡𝓾𝓹𝓽𝓾𝓻𝓮 𝓢𝓬𝓪𝓷𝓷𝓮𝓻 𝓯𝓻𝓮𝓮 𝓮𝓭𝓲𝓽𝓲𝓸𝓷
""")

if __name__ == "__main__":
    target = input('enter host for scanning:')
    t_IP = gethostbyname(target)
    print('Starting scan on host: ', t_IP)

    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if (conn == 0):
            print('Port %d: OPEN' % (i,))
        s.close()
print("time taken:", time.time() - startTime)
