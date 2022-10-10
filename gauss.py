def main():
    A = input("Enter matrix elements (space separated)\n")
    n = input("How many rows? ")
    m = input("How many columns? ")

    n = int(n[0])
    m = int(m[0])

    A = A.strip().split(" ")

    rows = []
    columns = []
    j = 0
    for elem in A:
        columns.append(elem)
        if(j == m-1):
            j = 0
            rows.append(columns)
            columns = []
        else:
            j += 1

    print("\nA has%2d out of %2d elements." % (len(A), n*m))
    if(len(A) < n*m):
        print("Filling remaining %2d elements with zeros." % (n*m-len(A)))
        for i in range(n*m - len(A)):
            columns.append('0')
            if(j == m-1):
                j = 0
                rows.append(columns)
                columns = []
            else:
                j += 1

    A = rows
    for i in range(n):
        print (A[i])

if __name__ == "__main__":
    main()