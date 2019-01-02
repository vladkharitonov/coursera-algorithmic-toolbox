# python3


def max_pairwise_product(numbers):
    largest = 0
    secondLargest = 0
    for i in numbers:
        if i >= largest:
            secondLargest = largest
            largest = i
        elif i >= secondLargest:
            secondLargest = i
    return largest * secondLargest


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
