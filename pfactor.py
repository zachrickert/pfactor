# Will factor a number into prime numbers.


def main():
    import math
    print("This program finds the prime factorization of a number.")
    numb = int(input("Enter a number: "))

    top_numb = int(math.sqrt(numb))
    # Only has to check up to the square root of a number for primes.
    # There can not be a factor greater than the square root of a number,
    # unless there is a factor less than the square root.
    is_first_answer = True

    is_prime = [True] * top_numb

    for i in range(2, top_numb):
        if (is_prime[i]):
            for j in range(i ** 2, top_numb, i):
                is_prime[j] = False

            while (numb % i == 0):
                if (is_first_answer):
                    answer = str(numb) + " = " + str(i)
                    is_first_answer = False
                else:
                    answer = answer + " * " + str(i)

                numb = numb / i
                top_numb = int(math.sqrt(numb))

    if (numb > 1):
        if (is_first_answer):
            answer = str(numb) + " is prime"
        else:
            answer = answer + " * " + str(numb)

    print(answer)

main()
