import unicodedata
while True:
    try:
        sentence = input().lower()
        filtered = list(c for c in unicodedata.normalize('NFD', sentence) if unicodedata.category(c) in ('Ll','Nd', 'Mn'))                
        n = len(filtered)
        for i in range(n):
            if unicodedata.category(filtered[i]) == 'Mn':                
                filtered[i],filtered[i-1] = filtered[i-1],filtered[i]
        j = n-1
        palindrome = True
        for i in range(n//2):
            if filtered[i] != filtered[j]:
                palindrome = False
                print('A busca continua, o Palindromo Perdido ainda nao foi encontrado.')
                break
            j+=-1
        if palindrome:
            print('Parabens, voce encontrou o Palindromo Perdido!')
    except EOFERROR:
        break
