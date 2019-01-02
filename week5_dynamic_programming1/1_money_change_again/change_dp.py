# Uses python3
import sys

def get_change(m):
    coins = 0
    remainder = m
    while remainder > 0:
    	if remainder % 4 == 0:
    		coins += int(remainder / 4)
    		remainder = 0
    	elif (remainder % 3 == 0) & (int(remainder // 4) < 2):
    		coins += int(remainder / 3)
    		remainder = 0
    	elif remainder > 4:
    		coins += 1
    		remainder -= 4
    	else:
    		coins += 1
    		remainder -= 1
    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
