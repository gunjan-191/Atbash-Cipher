# Atbash-Cipher

Atbash cipher is a substitution cipher with just one specific key where all the letters are reversed that is A to Z and Z to A. It was originally used to encode the Hebrew alphabets but it can be modified to encode any alphabet.

Algorithm: The following key is used in the Atbash algorithm
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ZYXWVUTSRQPONMLKJIHGFEDCBA

To encipher a message, find the letter you wish to encipher in the top row, then replace it with the letter in the bottom row.
In the example below, we encipher the message 'Hello world!. The first letter we wish to encipher is 'H', which is converted into 'S', so the first ciphertext letter is 'S' The next letter is 'e' which is converted into 'v' , so that comes next. The whole message is enciphered as:

Hello world!
Svool dliow!

In this we use lib.
     pip install pytest 

pytest lib, to do the unit testing.


Here we apply the condition  to get ascii values of char by finding the difference between them.
for example:-
     chr(219-ord(char)) 

chr is used to get unicode value from ascii code.

155 is ascii  code=  ø ( Lowercase slashed zero or empty set )
219 is ascii code = ( Block, graphic character )( HTML entity = &block; )
65 is ascii code = A
90 is ascii code = Z
97 is ascii code = a
122 is ascii code = z
