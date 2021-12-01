alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(shift, text):
  new_word = []
  for x in text:
    shifted_letter = alphabet.index(x)
    try:
      new_word.append(alphabet[shifted_letter+shift])
    except IndexError:
            new_word.append(alphabet[shifted_letter-shift])

  new_word_str = ''.join(new_word)
  print(new_word_str)

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(shift,text)