# Problem: Find the largest element in an array
def find_largest(arr):
    max_element = arr[0]

    for num in arr:
        if num > max_element:
            max_element = num

    return max_element

# Example usage
if __name__ == "__main__":
    arr = [10, 25, 3, 99, 56]
    print(f"Given array:{arr}")
    print("Largest element:", find_largest(arr))