import reader
import os

from pprint import pprint
from lexer.lexer import Lexer

def print_tokens(tokens):
  for token in tokens:
    print('(%3d, %3d) \t-\t  %s \t\t %s' % (token['lin'], token['col'], token['lexeme'], token['token']))

data = reader.read('./entry/main.c')

lexer = Lexer(data)
tokens = lexer.parse()



if len(lexer.errors) > 0:
  print('Lexer encountered one or more errors. Parsing fail! \n')
  
  for error in lexer.errors:
    if error['type'] == 'CHAR_OF_INVALID_ALPHABET':  
      print('Error on line %3d (col %3d): The "%c" char doesn\'t included in the valid alphabet' % (error['lin'], error['col'], error['data']))

    if error['type'] == 'MISMATCH_TOKEN':  
      print('Error on line %3d (col %3d): Unexpected token %s' % (error['lin'], error['col'], error['data']))
  
  exit()

  
# pprint(tokens)
print_tokens(tokens)