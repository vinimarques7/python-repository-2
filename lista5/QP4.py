NR = {
    1000: "M",
    900: "CM",
    500: "D",
    400: "CD",
    100: "C",
    90: "XC",
    50: "L",
    40: "XL",
    10: "X",
    9: "IX",
    5: "V",
    4: "IV",
    1: "I",
}

N = int(input())

nr = ""

for elemento, num in num_r.items():
    while N >= elemento:
        num_r += num
        N -= elemento

print(num_r)