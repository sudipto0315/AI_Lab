def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_odd_even_prime_nonprime(numbers):
    odd_count = 0
    even_count = 0
    prime_count = 0
    non_prime_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

        if is_prime(num):
            prime_count += 1
        else:
            non_prime_count += 1

    return odd_count, even_count, prime_count, non_prime_count

def main():
    numbers = [3, 6, 8, 11, 12, 13, 17, 20, 23, 29, 30]
    odd_count, even_count, prime_count, non_prime_count = count_odd_even_prime_nonprime(numbers)

    print("Number of odd numbers:", odd_count)
    print("Number of even numbers:", even_count)
    print("Number of prime numbers:", prime_count)
    print("Number of non-prime numbers:", non_prime_count)

if __name__ == "__main__":
    main()