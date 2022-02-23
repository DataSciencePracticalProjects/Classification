"""
Write a program that will convert the sequence of numbers entered by
the user into text, e.g .:
112 -> "one one two"
9973 -> "nine nine seven three"
Hint: you need the input () function, a dictionary and a loop.
"""
dict = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

def convert(numbers):
    total = []
    for num in numbers:
        total.append(f'{dict[int(num)]} ')
    return total


if __name__ == '__main__':
    input_numbers = input('Give a numbers: ').replace(" ", "")
    print(input_numbers)
    into_text = convert(input_numbers)
    print(f'{"" "".join(into_text)}')


