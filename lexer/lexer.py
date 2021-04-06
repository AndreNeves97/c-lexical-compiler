import re

from lexer.tokens import tokens_regex_rules


class Lexer:
  
  
  def __init__(self, source):
    self.source = source

  def parse(self):
    self.code = self.source
    self.errors = []
    return self.start_scanning_data()
    
  def start_scanning_data(self):
    rules = [
      '(?P<%s>%s)' % rule for rule in tokens_regex_rules
    ]
    
    regex_pattern = '|'.join(rules)

    tokens = []
    inside_line_comment = False
    inside_block_comment = False
    
    current_line = 1
    current_column = 1
    
    position_of_current_line = 0
    
    for match in re.finditer(regex_pattern, self.code):
      token = match.lastgroup
      lexeme = match.group(token)
      
      if token == 'NEWLINE':
        current_line += 1
        position_of_current_line = match.end()
          
        if inside_line_comment:
          inside_line_comment = False
        continue
      
      if inside_line_comment:
        continue
      
      
      if inside_block_comment:
        if token == 'END_BLOCK_COMMENT':
          inside_block_comment = False
        continue
      
      if token == 'LINE_COMMENT':
        inside_line_comment = True
        continue
    
      if token == 'START_BLOCK_COMMENT':
        inside_block_comment = True
        continue
      
      if token == 'SKIP':
        continue

      current_column = match.start() - position_of_current_line + 1
      
      if token == 'MISMATCH':
        self.handle_mismatch_token_error(lexeme, current_line, current_column)
      
      self.verify_lexeme_alphabet(lexeme, current_line, current_column)
      
      
      
      tokens.append({
        'token': token,
        'lexeme': lexeme,
        'lin': current_line,
        'col': current_column
      })
    
      if token == 'STRING_CONST':
        linebreak_count = lexeme.count('\n')
        current_line += linebreak_count
        
        if linebreak_count > 0:
          position_of_current_line =  match.start() + lexeme.rfind('\n') + 1

    return tokens
  
  def verify_lexeme_alphabet(self, lexeme, current_line, current_column):
    for char in lexeme:
      if ord(char) > 127:
        self.handle_alphabet_error(char, current_line, current_column)

  def handle_alphabet_error(self, char, current_line, current_column):
    self.errors.append({
      'type': 'CHAR_OF_INVALID_ALPHABET',
      'data': char,
      'lin': current_line,
      'col': current_column
    })
    
  def handle_mismatch_token_error(self, lexeme, current_line, current_column):
    self.errors.append({
      'type': 'MISMATCH_TOKEN',
      'data': lexeme,
      'lin': current_line,
      'col': current_column
    })