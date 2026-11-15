import time

# Non-Recursive Method
def non_recursive(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")

        c = a + b
        a = b
        b = c


# Recursive Method
def recursive(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return recursive(n - 1) + recursive(n - 2)


# Main Program
n = int(input("Enter number: "))

# Non-Recursive Execution Time
start = time.perf_counter_ns()

print("\nNon-Recursive Fibonacci: ", end="")
non_recursive(n)

end = time.perf_counter_ns()
time1 = (end - start) / 1000


# Recursive Execution Time
start = time.perf_counter_ns()

print("\nRecursive Fibonacci: ", end="")

for i in range(n):
    print(recursive(i), end=" ")

end = time.perf_counter_ns()
time2 = (end - start) / 1000


# Display Execution Time
print("\n\nExecution Time:")
print("Non-Recursive:", time1, "microseconds")
print("Recursive:", time2, "microseconds")
