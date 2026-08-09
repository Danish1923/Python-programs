principal=float(input("Enter the Principal amount:"))
rate=float(input("Enter the Rate of Interest:"))
years=float(input("Enter the Total No.of.years:"))

ci=principal*(1+rate/100)**years-principal

print(ci)