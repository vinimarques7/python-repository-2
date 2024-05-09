def parenteses(N):
    aberto = 0 
    
    for i in range (len(N)):
        if N[i] == '(':
            aberto += 1
        elif N[i] == ')':
            if aberto > 0:
                aberto -= 1
            else:
                return "incorrect"
    if aberto == 0:
        return "correct"
    else:
        return "incorrect"
while True:
    try:
        N = input()
        print(parenteses(N))
    except EOFError:
        break