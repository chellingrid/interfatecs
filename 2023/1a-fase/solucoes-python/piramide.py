n,p=input().split(" ")
n=int(n)

first_character = 65 if(p == 'maiusculas') else 97

letters=''

for i in range(n):
    letters+=chr(first_character+i)        
    print('.'*(25-i)+letters)
    
    

