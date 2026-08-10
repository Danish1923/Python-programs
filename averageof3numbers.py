#collecting the user input
num=list(map(int, input("Enter the numbers (Note:each separated by space):").split()))

#function for calculate the sum and find average
def average_of_num(num):
    result=sum(num) / len(num)
    return result

#average_of_num(num)

print(f"The average of the total numer is {average_of_num(num):.2f}")