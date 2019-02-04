import time
def tail(file):
    file.seek(0,2)
    while True:
        line = file.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

if __name__ == '__main__':
    logfile = open("/var/log/system.log","r")
    lines = tail(logfile)
    for line in lines:
        print line
