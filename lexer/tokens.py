tokens_regex_rules = [
  # Coments
  ('LINE_COMMENT',          r'\/\/'),
  ('START_BLOCK_COMMENT',   r'\/\*'),
  ('END_BLOCK_COMMENT',     r'\*\/'),
  
  ('NEWLINE',       r'\n'),
  ('SKIP',          r'[ \t\r]+'),
  
  
  ('DEFINE',		    r'define'),
  ('INCLUDE',		    r'include'),
  ('PRAGMA',		    r'pragma'),
  
  # Keywords: Variables and consts declaraion
  ('CONST',		      r'const'),
  ('INT',		        r'int'),
  ('CHAR',          r'char'),
  ('DOUBLE',		    r'double'),
  ('FLOAT',         r'float'),
  ('LONG',		      r'long'),
  ('UNSIGNED',		  r'unsigned'),
  ('TYPEDEF',		    r'typedef'),
  ('UNION',		      r'union'),
  ('SIZEOF',		    r'sizeof'),
  ('STATIC',		    r'static'),
  ('STRUCT',		    r'struct'),
  ('SHORT',		      r'short'),
  ('SIGNED',		    r'signed'),
  ('REGISTER',		  r'register'),
  ('VOID',		      r'void'),
  ('AUTO',		      r'auto'),
  ('ENUM',  		    r'enum'),
  ('EXTERN',		    r'extern'),
  ('VOLATILE',		  r'volatile'),
  
  #  Keywords: Flow controls
  ('GOTO',		      r'goto'),
  ('RETURN',        r'return'),
  ('IF',            r'if'),
  ('ELSE',          r'else'),
  ('SWITCH',		    r'switch'),
  ('CASE',		      r'case'),
  ('DEFAULT',		    r'default'),
  ('DO',		        r'do'),
  ('WHILE',         r'while'),
  ('FOR',		        r'for'),
  ('CONTINUE',	    r'continue'),
  ('BREAK',		      r'break'),
  
  #  Operators
  ('EQ',            r'=='),
  ('NE',            r'!='),
  ('LE',            r'<='),
  ('GE',            r'>='),
  ('OR',            r'\|\|'),
  ('AND',           r'&&'),
  ('ATTR',          r'\='),
  ('LT',            r'<'),
  ('GT',            r'>'),
  ('PLUS',          r'\+'),
  ('MINUS',         r'-'),
  ('ASTERISK',      r'\*'),
  ('HASH',          r'\#'),
  ('PIPE',          r'\|'),
  ('AMPERSAND',     r'&'),
  ('NEG',           r'\!'),
  ('DIV',           r'\/'),
  ('MOD',           r'\%'),
  
  # Patterns
  ('CHAR_CONST',    r"'(\\'|[^'])'"),
  ('STRING_CONST',  r'"(\\"|[^"])*"'),
  ('ID',            r'[a-zA-Z_]\w*'),
  ('FLOAT_CONST',   r'\d*\.\d+'),
  ('BINARY_CONST',  r'0b[0-1]+'),
  ('OCTAL_CONST',   r'0[0-7]+'),
  ('HEXA_CONST',    r'0x[0-9a-fA-F]+'),
  ('INTEGER_CONST', r'\d+'),
  
  
  # Punctuations
  ('LBRACKET',      r'\('),
  ('RBRACKET',      r'\)'),
  ('LBRACE',        r'\{'),
  ('RBRACE',        r'\}'),
  ('LSQUARE',       r'\['),
  ('RSQUARE',       r'\]'),
  ('COMMA',         r','),
  ('PCOMMA',        r';'),
  ('COLON',         r':'),
  ('DOT',           r'\.'),
  
  # Others
  ('MISMATCH',      r'.'),
]