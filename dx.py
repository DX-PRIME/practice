rows=int(input("Enter number of rows: "))
coluns=int(input("Enter number of columns: "))
symbol=input("Enter a symbol: ")
for i in range(rows):
    for j in range(coluns):
        print(symbol,end="")
    print()
