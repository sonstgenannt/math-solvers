def charnum(letter):
    return (ord(letter)-65)%32

def numchar(number):
    return chr(number+65)

def stringconv(string, function):
    new = []
    for character in string:
        new.append(function(character))
    return new
        
def decrypt_vigenere(key, message):
    loop = []
    for letter in key:
        loop.append(charnum(letter))
    
    output = ""
    
    index = 0
    for letter in message:
        #print(letter, charnum(letter), loop[index%len(loop)])
        number = charnum(letter)-loop[index%len(loop)]
        output = output + numchar(number%26)
        index += 1
        
    return output

def encrypt_vigenere(key, ciphertext):
    loop = []
    for letter in key:
        loop.append(charnum(letter))
    
    output = ""
    
    index = 0
    for letter in ciphertext:
        #print(letter, charnum(letter), loop[index%len(loop)])
        number = charnum(letter)+loop[index%len(loop)]
        output = output + numchar(number%26)
        index += 1
        
    return output

print(decrypt_vigenere("KEY", "KPEYVGDLK"))
print(encrypt_vigenere("KEY", "CRYPTOGRAPHY"))
