class RomanConverter:
    def __init__(self):
        self.int_to_roman_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

        self.roman_to_int_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def int_to_roman(self, num):
        result = ""
        for value, numeral in self.int_to_roman_map:
            while num >= value:
                result += numeral
                num -= value
        return result

    def roman_to_int(self, s):
        total = 0
        prev_value = 0
        for char in reversed(s):
            value = self.roman_to_int_map[char]
            if value < prev_value:
                total -= value
            else:
                total += value
                prev_value = value
        return total


# Example usage
converter = RomanConverter()

# Convert integer to Roman
print(converter.int_to_roman(1994))  # Output: MCMXCIV

# Convert Roman to integer
print(converter.roman_to_int("MCMXCIV"))  # Output: 1994
