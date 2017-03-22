# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    max_value_item = 0
    value_per_weight = [int(a) / int(b) for a,b in zip(values, weights)]

    while capacity > 0:
        max_value_item = value_per_weight.index(max(value_per_weight))

        if weights[max_value_item] >= capacity:
            value += value_per_weight[max_value_item] * capacity
            return value

        value += values[max_value_item]
        value_per_weight[max_value_item] = 0
        capacity -= weights[max_value_item]
        if all(i == 0 for i in value_per_weight):
            return value
    	
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
