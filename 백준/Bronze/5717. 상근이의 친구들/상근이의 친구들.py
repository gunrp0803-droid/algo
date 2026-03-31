import sys

while True:
    try:
        line = sys.stdin.readline()
        if not line:
            break
            
        m, f = map(int, line.split())
     
        if m == 0 and f == 0:
            break
            
        print(m + f)
    except ValueError:
        break