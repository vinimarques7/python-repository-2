# N = int(input("Me dê um número: "))

# for i in range(N):
#     A = input()
#     B = input()

#     if A[-1] == B[-1]:
#         print("encaixa")
#     else:
#         print("nao encaixa")

# Number of test cases
N = int(input())

for _ in range(N):
    A, B = input().split()  # Read A and B for each test case
    
    # Check if B corresponds to the last digits of A
    if A.endswith(B):
        print("encaixa")
    else:
        print("nao encaixa")



