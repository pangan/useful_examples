import signal
import sys


def do_loop():
    while True:
        print('.'),


def goodbye(signum, frame):
    
    print("Terminating", end='')
    
    #sys.stdout.write('Terminated by: {0}'.format(signum))
    sys.exit(0)

if __name__ == '__main__':
    signal.signal(signal.SIGTERM, goodbye)
    signal.signal(signal.SIGINT, goodbye)

    do_loop()
