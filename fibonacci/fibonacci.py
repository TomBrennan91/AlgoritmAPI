

def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    memo = [0, 1]
    for i in range(2, n + 1):
        memo.append(fibonacci_helper(i, memo))
    return memo[n]

def fibonacci_helper(n: int, memo: list) -> int:

    if n < len(memo):
        return memo[n]
    else:
        return fibonacci_helper(n - 1, memo) + fibonacci_helper(n - 2, memo)
