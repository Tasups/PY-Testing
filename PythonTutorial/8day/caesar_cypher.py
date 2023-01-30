# Caesar Cypher app

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input('Type "encode" to encrypt or "decode" to decrypt a message.\n')

if direction == "encode":
  text =  input('Type your message:\n').lower()
  shift = int(input('Type the number to shift:\n'))
    
  def encode(plain_text, shift_amount):
    encoded_result = ""
    for letter in plain_text:
      position = alphabet.index(letter)
      shifted_position = position + shift_amount
      if shifted_position > 26:
        shifted_position -= 26
      # print(f"{position} + {shift_amount} = {shifted_position}")
      encoded_result += alphabet[shifted_position]
    print(f"The encoded text is:\n{encoded_result}")
    
  encode(plain_text=text, shift_amount=shift) # => 7,4,11,11,14

if direction == "decode":
  coded_text = input('Type message to decode:\n').lower()
  unshift = int(input('Type the number to unshift:\n'))
  
  def decode(encoded_text, unshift_amount):
    decoded_result = ""
    for letter in encoded_text:
      position = alphabet.index(letter)
      unshifted_position = position - unshift_amount
      if unshifted_position < 0:
        unshifted_position += 26
      decoded_result += alphabet[unshifted_position]
    print(f"The decoded text is:\n{decoded_result}")
    
  decode(encoded_text=coded_text, unshift_amount=unshift)