end=int(input("Enter the Number:"))
start=1
total=0

while start<=end:
    print(start)
    total=total+start
    start=start+2

print(f"sum={total}")
#python sum_odd_while.py