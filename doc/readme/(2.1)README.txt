# KLEINcompiler
Translation of Programming Languages Compiler Project

Team Name: Fork Bomb
Team Members: Tyler Rahe, Alan Mckay, Killian Bailey


Project Description:

The project goal is to create a compiler that takes as input a program written in Klein and outputs the equivalent program written in the assembly language TinyMachine.

--- Development Stages:

-- Scanner, Project 1:
    
    Associated impelementation files:
        -kleins
        -src/k_token.py
        -src/scanner.py

    Scanner Description:
        The scanner is the portion of the compiler which takes as input a klein program as a single string and splits the string into a set of tokens. The token class is described in k_token.py. The scanner steps through each character of the program string and uses a set of conditions to determine if a resultant character or string is a valid token. These conditions are based on the possible terminals present in the language specification. These may either be a single character, such as the case of the unary and binary operators, or can be a string, such as any identifier or number. Thus the conditions are based on a set of regular expressions, noted in the scanner portion of the documents folder. These regular expressions are used to build the conditions in place, represented by the FSA diagram which is also housed in the same folder.

    Associated documentation files:
        -doc/scanner/regex.txt
        -doc/scanner/regex_FSA.jpg
            ->doc/regex_FSA.jff is the jflap file used to create the above jpeg.
        -doc/scanner/scanner_status_check.txt
        
-- Parser, Project 2:

    Associated implementation files:
        -kleinf
        -src/parser.py
        -src/parse_table.py
    
    Parser Description:
        The first phase of the parser is the implementation which decides if a program is syntactically correct. That is, it makes sure that any given combination of tokens are in a valid order. This is determined by the grammar of the Klein language, which has been refactored to eliminate the need for the parser to have to read in more than one token from scanner at a time to decide whether or not a combination of tokens is valid.
        
        The validity is determined by a parse table, which is determined by the first and follow sets for every declaration statement within the refactored grammar. These first and follow sets help us know every possible token which leads a nonterminal and every possible token that ends a terminal. With this information we can surmise all possible combinations while considering nonterminal composition (including nonterminals composed of other nonterminals) This is thus mapped to a table using a specific algorithm which considers whether or not a grammar statement has an empty character in it's first set.
        
        Thus the parser has a parse stack which assumes an end of file token exists in addition to a nonterminal which represents the program as a whole. It pops takes a look at the top element of the stack and uses it to look up the valid combination of preceding tokens while considering the current token that is being read by the scanner. The parser walks the table using this logic, pushing terminals and nonterminals onto the parse stack based on the result of the current index of the parse table until either an invalid combination of tokens is discovered or the end of file token is reached.
    
    Associated documentation files:
        -doc/parser/extended_grammar.txt
        -doc/parser/fist_and_follow_sets.txt
        -doc/parser/parse_table.pdf
            ->doc/parser/parse_table.ods
        
--- The Repository ---

    --The home directory is KLEINcompiler/
        -The home directory is currently where the compiler will output any error logs. This needs to be changed; an error_log folder should be created for this purpose.
        
        -The home directory is also home to the various shell scripts used to test the various stages of the compiler. The associations are noted in the above project sections.
            ->./kleins
            ->./kleinf
            ->./kleinp
            *To run each script, run the command 'sh <script name> <program to be tested>'
                *->Example: sh kleinf programs/multiply.kln     
                
        -The doc directory houses various forms of documentation, housed in folders in respect to their implementation.
        
        -The programs directory houses various Klein programs used for testing the various stages of our compiler. These are the files used as input for the klein scripts housed in the home directory.
        
        -The src directory houses all files used for implementation of the compiler
        
        -The tests directory houses files used to run the shell scripts noted above
