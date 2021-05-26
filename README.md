# C lexical analyzer compiler

Analisador léxico básico da linguagem `C Ansi`, desenvolvido em Python.

## Bibliotecas utilizadas:

- 'os'
- 'sys'
- 're'
- 'pprint'


## Execução:

```bash
## Executar o script de entrada
python3 main.py
```

Os códigos de teste utilizados então em `./entry`. O ponto de entrada `main.py` é responsável pela leitura do arquivo `main.c`, e processamento do conteúdo.


## Demonstração

O seguinte código foi utilizado para teste base:


```c
int a = 1000
// "INT" não é identificador, é keyword 
// áaर
/* áaर
*/

e
int char = 123;

/**
 *
 *
 * afsafsa fsaf safsa
 *
 * andre
 *
 */

int main(int arg1, a2 1) {char a = 'a';
  lo = (c == 'a' || 
    c == 'e' /* afsaa */ || 
    c == 'i' || c =='o' || c =='u'
    );

  int negative = -104

  "String with 
    multi
    line
  " int b = 1

  // Octal number
  int a = 0107;
  printf("aaa %i", a);

  return 0;
}

```

Resultado do analisador léxico:

```c
/* 
Legend:
(line, column)  -         lexeme         token
*/

(  1,   1)      -         int            INT
(  1,   5)      -         a              ID
(  1,   7)      -         =              ATTR
(  1,   9)      -         1000           INTEGER_CONST
(  7,   1)      -         e              ID
(  8,   1)      -         int            INT
(  8,   5)      -         char           CHAR
(  8,  10)      -         =              ATTR
(  8,  12)      -         123            INTEGER_CONST
(  8,  15)      -         ;              PCOMMA
( 19,   1)      -         int            INT
( 19,   5)      -         main           ID
( 19,   9)      -         (              LBRACKET
( 19,  10)      -         int            INT
( 19,  14)      -         arg1           ID
( 19,  18)      -         ,              COMMA
( 19,  20)      -         a2             ID
( 19,  23)      -         1              INTEGER_CONST
( 19,  24)      -         )              RBRACKET
( 19,  26)      -         {              LBRACE
( 19,  27)      -         char           CHAR
( 19,  32)      -         a              ID
( 19,  34)      -         =              ATTR
( 19,  36)      -         'a'            CHAR_CONST
( 19,  39)      -         ;              PCOMMA
( 20,   3)      -         lo             ID
( 20,   6)      -         =              ATTR
( 20,   8)      -         (              LBRACKET
( 20,   9)      -         c              ID
( 20,  11)      -         ==             EQ
( 20,  14)      -         'a'            CHAR_CONST
( 20,  18)      -         ||             OR
( 21,   5)      -         c              ID
( 21,   7)      -         ==             EQ
( 21,  10)      -         'e'            CHAR_CONST
( 21,  26)      -         ||             OR
( 22,   5)      -         c              ID
( 22,   7)      -         ==             EQ
( 22,  10)      -         'i'            CHAR_CONST
( 22,  14)      -         ||             OR
( 22,  17)      -         c              ID
( 22,  19)      -         ==             EQ
( 22,  21)      -         'o'            CHAR_CONST
( 22,  25)      -         ||             OR
( 22,  28)      -         c              ID
( 22,  30)      -         ==             EQ
( 22,  32)      -         'u'            CHAR_CONST
( 23,   5)      -         )              RBRACKET
( 23,   6)      -         ;              PCOMMA
( 25,   3)      -         int            INT
( 25,   7)      -         negative               ID
( 25,  16)      -         =              ATTR
( 25,  18)      -         -              MINUS
( 25,  19)      -         104            INTEGER_CONST
( 27,   3)      -         "String with 
    multi
    line
  "              STRING_CONST
( 30,   5)      -         int            INT
( 30,   9)      -         b              ID
( 30,  11)      -         =              ATTR
( 30,  13)      -         1              INTEGER_CONST
( 33,   3)      -         int            INT
( 33,   7)      -         a              ID
( 33,   9)      -         =              ATTR
( 33,  11)      -         0107           OCTAL_CONST
( 33,  15)      -         ;              PCOMMA
( 34,   3)      -         printf                 ID
( 34,   9)      -         (              LBRACKET
( 34,  10)      -         "aaa %i"               STRING_CONST
( 34,  18)      -         ,              COMMA
( 34,  20)      -         a              ID
( 34,  21)      -         )              RBRACKET
( 34,  22)      -         ;              PCOMMA
( 36,   3)      -         return                 RETURN
( 36,  10)      -         0              INTEGER_CONST
( 36,  11)      -         ;              PCOMMA
( 37,   1)      -         }              RBRACE
```


Esse caso de teste não possui um código com erros. Os arquivos `entry/main2.c` e `entry/main3.c` possuem exemplos com erros de alfabeto inválido e token inválido.