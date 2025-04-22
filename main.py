# Global variable to count comparisons
comparisons = 0

# Read integers into a list and return the list.
def read_nums():
    nums = input().split()
    return [int(num) for num in nums]

# Output the content of a list, separated by spaces.
def print_nums(numbers):
    for num in numbers:
        print(num, end=' ')
    print()

def merge(numbers, i, j, k):
    global comparisons

    merged_size = k - i + 1               
    merged_numbers = [0] * merged_size

    merge_pos = 0
    left_pos = i
    right_pos = j + 1

    while left_pos <= j and right_pos <= k:
        comparisons += 1
        if numbers[left_pos] < numbers[right_pos]:
            merged_numbers[merge_pos] = numbers[left_pos]
            left_pos += 1
        else:
            merged_numbers[merge_pos] = numbers[right_pos]
            right_pos += 1
        merge_pos += 1

    while left_pos <= j:
        merged_numbers[merge_pos] = numbers[left_pos]
        left_pos += 1
        merge_pos += 1

    while right_pos <= k:
        merged_numbers[merge_pos] = numbers[right_pos]
        right_pos += 1
        merge_pos += 1

    for m in range(merged_size):
        numbers[i + m] = merged_numbers[m]

def merge_sort(numbers, i, k):
    if i < k:
        j = (i + k) // 2
        print(f'{i} {j} | {j + 1} {k}')
        merge_sort(numbers, i, j)
        merge_sort(numbers, j + 1, k)
        merge(numbers, i, j, k)

if __name__ == '__main__':
    numbers = read_nums()

    print('unsorted:', end=' ')
    print_nums(numbers)
    print()

    merge_sort(numbers, 0, len(numbers) - 1)

    print('\nsorted:', end=' ')
    print_nums(numbers)

    # Output the number of comparisons
    print(f'comparisons: {comparisons}')
