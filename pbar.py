import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

start_timestamp = time.time()
def printProgress(percentage):
    global start_timestamp
    if percentage == 0:
        start_timestamp = time.time()

    val = int(percentage * 100)
    symbol = '━'
    lpad = ''.join([symbol for v in range(val)])
    rpad = ''.join([symbol for v in range(100 - val)])

    tps = val/(time.time() - start_timestamp)
    print("\rProgress: |"+bcolors.OKGREEN+f"{lpad}"+bcolors.ENDC+bcolors.OKBLUE+f"{rpad}"+bcolors.ENDC+f"| {val}% | {tps:.2f} T/s", end='',flush=True)
    if(val >= 100):
        print("")