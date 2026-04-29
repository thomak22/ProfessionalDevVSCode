def mean(numbers, weights=None):
    """Calculate the mean of a list of numbers. Can be weighted"""
    if weights is None:
        return sum(numbers) / len(numbers)
    else:
        return sum(n * w for n, w in zip(numbers, weights)) / sum(weights)

def median(numbers):
    """Calculate the median of a list of numbers. Sorts the list for you"""
    n = len(numbers)
    sorted_numbers = sorted(numbers)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

def mode(numbers):
    """Calculate the mode(s) of a list of numbers."""
    frequency = {}
    for number in numbers:
        frequency[number] = frequency.get(number, 0) + 1

    max_freq = max(frequency.values())
    modes = [num for num, freq in frequency.items() if freq == max_freq]

    return modes

