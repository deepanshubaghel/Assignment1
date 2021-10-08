#Task1
Referral id: DIRSS1104
Name: Deepanshu Baghel
--------------------------------------

1:
  r = 5
for i in range(r, 0, -1):
    for j in range(0, i):
        print("5", end=" ")
    print("")
   
OUTPUT:-
       5 5 5 5 5 
       5 5 5 5 
       5 5 5 
       5 5 
       5 
-------------------------------------
2:

  r = 5
for i in range(r, 0, -1):
    for j in range(0, i + 1):
        print(j, end=" ")
    print(" ")

OUTPUT:-

      0 1 2 3 4 5  
      0 1 2 3 4  
      0 1 2 3  
      0 1 2  
      0 1  
---------------------------------------
3:

  rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ")
        j = j + 1
    i = i + 1
    print()

OUTPUT:-

       1 
       3 3 
       5 5 5 
       7 7 7 7 
       9 9 9 9 9 
-----------------------------------------
4:

  rows = 6
for row in range(1, rows):
    for column in range(row, 0, -1):
        print(column, end=" ")
    print("")

OUTPUT:
      
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1 
-------------------------------------------
5:

 start = 1
stop = 2
lastnumber = stop
for row in range(2, 6):
    for col in range(start, stop):
        lastnumber -= 1
        print(lastnumber, end=" ")
    print("")
    start = stop
    stop += row
    lastnumber = stop

OUTPUT:-

1 
3 2 
6 5 4 
10 9 8 7 
-------------------------------------------
6:

 def printPascal(n):
    for line in range(0, n):
        for i in range(0, line + 1):
            print(binomialCoeff(line, i), "", end="")
        print()


def binomialCoeff(n, k):
    r = 1
    if (k > n - k):
        k = n - k
    for i in range(0, k):
        r = r * (n - i)
        r = r // (i + 1)

    return r


n = 7
printPascal(n)

OUTPUT:-

1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1 
--------------------------------------------
7:

 rows = 5
for i in range(1, rows + 1):
    for j in range(1, rows + 1):
        if j <= i:
            print(i, end=' ')
        else:
            print(j, end=' ')
    print()

OUTPUT:-

1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5 
------------------------------------------------
8:

 rows = 9
for i in range(1, rows):
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()

OUTPUT:-

1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 
6 12 18 24 30 36 
7 14 21 28 35 42 49 
8 16 24 32 40 48 56 64 
--------------------------------------------------
9:

  rows = 5
k = 3 * rows
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")

OUTPUT:-

               * * * * * * 
                * * * * * 
                 * * * * 
                  * * * 
                   * * 
                    * 
-------------------------------------------------
10:

 n = 8
m = (2 * n)
for i in range(0, n):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        print("* ", end=" ")
    print(" ")

OUTPUT:-

                *   
               *  *   
              *  *  *   
             *  *  *  *   
            *  *  *  *  *   
           *  *  *  *  *  *   
          *  *  *  *  *  *  *   
         *  *  *  *  *  *  *  *   
-------------------------------------------------------
11:

  rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")

for i in range(rows + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")

OUTPUT:-

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * *  
* * * *  
* * *  
* *  
*  
---------------------------------------------
12:

  rows = 6
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=" ")
    print(" ")
for i in range(rows - 1, 0, -1):
    for j in range(-1, i - 1):
        print("*", end=" ")
    print(" ")

OUTPUT:-

*  
* *  
* * *  
* * * *  
* * * * *  
* * * * * *  
* * * * *  
* * * *  
* * *  
* *  
*  
----------------------------------------------
13:

  rows = 5
i = 1
while i <= rows:
    j = i
    while j < rows:

        print(" ", end=" ")
        j += 1
    k = 1
    while k <= i:
        print("*", end=" ")
        k += 1
    print()
    i += 1
i = rows
while i >= 1:
    j = i
    while j <= rows:
        print(" ", end=" ")
        j += 1
    k = 1
    while k < i:
        print("*", end=" ")
        k += 1
    print(" ")
    i -= 1

OUTPUT:-

        * 
      * * 
    * * * 
  * * * * 
* * * * * 
  * * * *  
    * * *  
      * *  
        *
-------------------------------------------------
14:

  row = 6
for i in range(row, 0, -1):
    for j in range(row-i):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print("")

for i in range(2, row+1):
    for j in range(row-i):
        print(" ", end="")
    for j in range(1, 2*i):
        print("*", end="")
    print("")

OUTPUT:-

***********
 *********
  *******
   *****
    ***
     *
    ***
   *****
  *******
 *********
***********
--------------------------------------------- 
           


   
