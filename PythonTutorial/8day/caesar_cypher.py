# Caesar Cypher app

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input('Type "encode" to encrypt or "decode" to decrypt a message.\n')
text =  input('Type your message:\n').lower()
shift = int(input('Type the number to shift:\n'))
  
def encode(text, shift):
  result = []
  for letter in text:
    val = alphabet.index(letter)
    shift_val = val + shift
    if shift_val > 26:
      shift_val -= 26
    print(f"{val} + {shift} = {shift_val}")
    result.append(alphabet[shift_val])
  encoded_text = "".join(result)
  print(encoded_text)
  
encode(text, shift) # => 7,4,11,11,14