vowels=["a","e","i","o","u","A","E","I","O","U"]
cons=["b","B","c","C","d","D","f","F","g","G","h","H","j","J","k","K","l","L","m","M","n","N","p","P","q","Q","r","R","s","S","t","T","v","V","w","W","x","X","y","Y","z","Z"]
name=input("Insert a word to translate that is one word, no numbers and is lowercased ")
vow=name+"hay"
if(name[0]in vowels):
   print(vow)

elif(name[0] in cons and name[1] in cons):
    print(name[2:]+ name[0:2] + "ay")
else:
    print(name[1:] + word[0] + "ay")


