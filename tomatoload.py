import time
symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
i = 0
while True:
    i = (i + 1) % len(symbols)
    print('\r\033[K%s loading...' % symbols[i], flush=True, end='')
    time.sleep(0.1)
