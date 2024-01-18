import time
symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
i = 0
for tomato in range(20):
    i = (i + 1) % len(symbols)
    print('\r\033[K%s loading tomato...' % symbols[i], flush=True, end='')
    time.sleep(0.1)
