# def print_rangoli(n):
#     # your code goes here
#
#     import string
#     alpha = string.ascii_lowercase
#
#     # Create the list of rows
#     lines = []
#     for i in range(n):
#         s = '-'.join(alpha[n - 1:i:-1] + alpha[i:n])
#         lines.append(s.center(4 * n - 3, '-'))
#
#     # Combine all rows
#     rangoli_pattern = '\n'.join(lines[::-1] + lines[1:])
#     print(rangoli_pattern)
#     return rangoli_pattern
#
#
# if __name__ == '__main__':
#     n = int(input())
#     print_rangoli(n)
#

def rangoli(size):

    import string
    alpha = string.ascii_lowercase

    # Create the list of rows
    lines = []
    for i in range(size):
        s = '-'.join(alpha[size - 1:i:-1] + alpha[i:size])
        lines.append(s.center(4 * size - 3, '-'))

    # Combine all rows
    rangoli_pattern = '\n'.join(lines[::-1] + lines[1:])
    return rangoli_pattern


# Example Usage
if __name__ == "__main__":
    while True:
        size = int(input("Enter the size of the rangoli: "))
        print(rangoli(size))
        continue_choice = input("Do you want to print another rangoli? (yes to continue, no to exit): ").strip().lower()
        if continue_choice != 'yes':
            print("Exiting...")
            break
