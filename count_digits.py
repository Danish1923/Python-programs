number=int(input("Enter the Poitive Numbers:"))

count=0

while number>=1:
    print(number)
    number=number // 10
    count=count+1
print(f"Digit={count}")
#python count_digits.py