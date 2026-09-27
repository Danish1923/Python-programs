print("-----Grade Checker-----")
mark=float(input("Enter your Mark:"))

if 90<=mark<=100:
    print("Excellent")
elif 75<=mark<=89:
    print("Very Good")
elif 60<=mark<=74:
    print("Good")
elif 40<=mark<=59:
    print("Pass")
elif 0<=mark<40:
    print("Fail")
else:
    print("Enter Valid Mark")
