n=int(input("Wpisz pierwszą liczbę(minimum 1, maximum 9999):"));
if n < 1:
    print("Ta liczba jest za mała. Próbuj jeszcze raz.");
    n = int(input("Wpisz pierwszą liczbę(minimum 1, maximum 9999):"));
elif n > 9999:
    print("Ta liczba jest za duża. Spróbuj jeszcze raz")
    n = int(input("Wpisz pierwszą liczbę(minimum 1, maximum 9999):"));

m=int(input("Wpisz drugą liczbę większą od pierwszej(minimum 1, maximum 10000):")) + 1;

if n < 2:
    print("Ta liczba jest za mała. Próbuj jeszcze raz.");
    n = int(input("Wpisz pierwszą liczbę(minimum 2, maximum 10000):"));
elif n > 9999:
    print("Ta liczba jest za duża. Spróbuj jeszcze raz")
    n = int(input("Wpisz pierwszą liczbę(minimum 2, maximum 10000):"));
elif m < n:
    print("Druga liczba musi być większa")
    m = int(input("Wpisz drugą liczbę większą od pierwszej(minimum 1, maximum 10000):")) + 1;

for i in range(n,m):
    # albo mozna wpisac i % 15 == 0
    if (i % 3) == 0 and (i % 5) == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz");
    elif i % 5 == 0:
        print("Buzz");
    else:
        print(i);

