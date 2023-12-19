Phone = input("Enter your Phone Number ")
Digits_Mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "Zero"
}
output = " "
for ch in Phone:
    output += Digits_Mapping.get(ch, "!") + " "

print(output)
