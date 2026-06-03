# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for _ in range(t):
    s = input()
    even = s[::2]  # characters at even indices
    odd = s[1::2]  # characters at odd indices
    print(even, odd)