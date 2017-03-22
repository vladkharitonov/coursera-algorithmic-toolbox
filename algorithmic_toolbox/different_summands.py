# Uses python3
import sys

def optimal_summands(n):
    if n == 2:
        summands = [2]
        return summands
    summands = [1,]
    n = n - 1
    while n > 0:
    	if n <= (summands[-1] + 1) * 2:
    		summands.append(n)
    		return summands
    	n -= summands[-1] + 1
    	summands.append(summands[-1] + 1)
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
