def roman_dictionary():
    return {
        1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
        6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
        11: 'XI', 12: 'XII', 13: 'XIII', 14: 'XIV', 15: 'XV',
        16: 'XVI', 17: 'XVII', 18: 'XVIII', 19: 'XIX', 20: 'XX',
        21: 'XXI', 22: 'XXII', 23: 'XXIII', 24: 'XXIV'
    }

def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def main():
    roman_dict = roman_dictionary()
    print("Roman Numeral Dictionary:")
    print_dictionary(roman_dict)
    
    number = int(input("Enter a positive integer (0 or negative to quit): "))
    while number > 0:
        try:
            if number in roman_dict:
                print(f"Roman numeral for {number}: {roman_dict[number]}")
            else:
                add_new = input(f"Roman numeral for {number} not found. Add it to the dictionary? (y/n): ")
                if add_new.lower() == 'y':
                    new_roman = input(f"Enter the alphabetic Roman numeral for {number}: ")
                    if new_roman.isalpha():
                        roman_dict[number] = new_roman.upper()
                        print(f"Added {number}: {new_roman.upper()} to the dictionary.")
                    else:
                        print("Invalid Roman numeral format.")
                else:
                    print("Not adding to the dictionary.")
        except ValueError:
            print("Invalid input.")

        number = int(input("Enter a positive integer (0 or negative to quit): "))

    print("Final Roman Numeral Dictionary:")
    print_dictionary(roman_dict)
main()
