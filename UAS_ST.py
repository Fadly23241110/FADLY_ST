# Program untuk mengecek apakah sebuah bilangan adalah bilangan prima
# dan menghitung jumlah bilangan prima dari 1 sampai n

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def count_primes(n):
    count = 0
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count

# Meminta input dari pengguna
n = int(input("Masukkan sebuah bilangan: "))

# Menggunakan percabangan untuk mengecek apakah bilangan itu prima
if is_prime(n):
    print(f"{n} adalah bilangan prima.")
else:
    print(f"{n} bukan bilangan prima.")

# Menghitung dan mencetak jumlah bilangan prima dari 1 sampai n
jumlah_prima = count_primes(n)
print(f"Jumlah bilangan prima dari 1 sampai {n} adalah {jumlah_prima}.")
