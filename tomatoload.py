import time
symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
def tomato_load(rep):
    i = 0
    for tomato in rep:
        i = (i + 1) % len(symbols)
        print('\r\033[K%s loading tomato...' % symbols[i], flush=True, end='')
        time.sleep(0.1)
