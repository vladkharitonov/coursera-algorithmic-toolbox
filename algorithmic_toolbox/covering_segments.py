# Uses python3
import sys

def optimal_points(segments):
    segments = sorted(segments, key = lambda x: x[1])
    endpoints = [x[1] for x in segments]
    points = [endpoints[0],]

    for s in segments:
        if s[0] > points[-1]:
            points.append(s[1])

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: (x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')