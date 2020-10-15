

# Расширенный евклидов алгоритм нахождения модулярного обратного

def egcd(a, b): 
	x,y, u,v = 0,1, 1,0
	while a != 0: 
		q, r = b//a, b%a 
		m, n = x-u*q, y-v*q 
		b,a, x,y, u,v = a,r, u,v, m,n 
	gcd = b 
	return gcd, x, y 

def modinv(a, m): 
	gcd, x, y = egcd(a, m) 
	if gcd != 1: 
		return None 
	else: 
		return x % m 



# # функция шифрования аффинного шифра
# # возвращает зашифрованный текст
def affine_encrypt(text, key): 
	''' 
	C = (a*P + b) % 26 
	'''
	return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26) 
				+ ord('A')) for t in text.upper().replace(' ', '') ]) 


# функция расшифровки аффинного шифра
# возвращает исходный текст 
def affine_decrypt(cipher, key): 
	''' 
	P = (a^-1 * (C - b)) % 26 
	'''
	return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1])) 
					% 26) + ord('A')) for c in cipher ]) 
# объявление текста и ключа

def main(): 
    text=input("введите текст, который будет зашифрован или расшифрован: ")
	#text = 'AFFINE CIPHER'
   # key=[list(input("введите клавишу A,пробел, затем клавишу B:"))]
    n = int(input("введите количество ключей : ")) 
  
# Below line read inputs from user using map() function  
    key = list(map(int,input("введите ключ A,пробел, затем ключ B:").strip().split()))[:n] 
   # key = [17, 20] 
# вызов функции шифрования
    affine_encrypted_text = affine_encrypt(text, key) 
    print('зашифрованный текст: {}'.format( affine_encrypted_text )) 

	# вызов функции дешифрования
    print('Расшифрованный Текст: {}'.format
	( affine_decrypt(affine_encrypted_text, key) )) 


if __name__ == '__main__': 
	main() 

