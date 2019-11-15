# KLEINcompiler
Translation of Programming Languages Compiler Project

Team Name: Fork Bomb
Team Members: Tyler Rahe, Alan Mckay, Killian Bailey


Project Description:

The project goal is to create a compiler that takes as input a program written 
in Klein and outputs the equivalent program written in the assembly language 
TinyMachine.

--- Development Stages:

-- CodeGenerator, Project 5:

    Associated implementation files:
    -print-one.kln
    -AST_node.py
    -code-generator.py
    
    Code Generator Description:
    The first phase of the code generator is that it starts jumping to the main function and then saves all of      
    
    
    
    
   



-- Parser, Project 3:

    Associated implementation files:
        -kleinp
        -src/parser.py
        -src/parse_table.py
        -src/AST_node.py
        
    Semantic Analyizer Description:
        The second phase of the parser is to build an abstact syntax tree which
        represents the various expressions and operations of the input program
        in the most general sense. These expressions and operations thereof are
        put into data structures which will later be used to convert the 
        statements into their equivalents during code generation.
        
    What is finished:
        -The inclusion of the semantic stack and the implementation of the parse
        algorithm to communicate between the parse stack and the semantic stack.
        
        -The inclusion of semantic actions within the parse table.
        
        *We currently have an enumeration class in the parse table which is used
        to evaluate the semantic actions returned on the parse table.
        
        *When the semantic action is evaluated with respect to the parse
        algorithm, it is used to index into a dictionary called object_factory
            ->The object factory returns the relevant AST_node class which is
            used to construct the relevant node object within the parse
            algorithm
            ->The resultant node is then pushed onto the semantic stack. The
            resultant node is also passed the semantic stack upon construction.
            Logic will exist within the node's constructor to know what to do
            with the stack and the various nodes and relevant tokens that reside
            in it.
        
    What is not finished:
        -The AST nodes themselves are not done. We've finished a couple of easy
        ones, those that only really need to house a value - such as an 
        identifier.
        -We don't have any error handling in place once the AST nodes are ready
        for testing
        -...and thus we haven't run any tests
        
    What else has been accomplished:
        -We've solved our problem with the parse table from project 2. We've
        also run the tests you've provided and they pass.
        -We've expanded the error classes. Each error writes to a relevant text
        file the initial program and the associated stdout error message.
            ->Lexical error appends the remainding program string to it's error
            log
            ->Parse error appends the parse stack trace to it's error log
        -We've fixed the scanner returning a none value when evaluating comments
            ->We've had to extend logic to do this, this has resulted in some
            messy code that needs to be refactored.
            

-- Parser, Project 2:

    Associated implementation files:
        -kleinf
        -src/parser.py
        -src/parse_table.py
    
    Syntactic Analyizer Description:
        The first phase of the parser is the implementation which decides if a 
        program is syntactically correct. That is, it makes sure that any given 
        combination of tokens are in a valid order. This is determined by the 
        grammar of the Klein language, which has been refactored to eliminate 
        the need for the parser to have to read in more than one token from 
        scanner at a time to decide whether or not a combination of tokens is 
        valid.
        
        The validity is determined by a parse table, which is determined by the 
        first and follow sets for every declaration statement within the 
        refactored grammar. These first and follow sets help us know every 
        possible token which leads a nonterminal and every possible token that 
        ends a terminal. With this information we can surmise all possible 
        combinations while considering nonterminal composition (including 
        nonterminals composed of other nonterminals) This is thus mapped to a 
        table using a specific algorithm which considers whether or not a 
        grammar statement has an empty character in it's first set.
        
        Thus the parser has a parse stack which assumes an end of file token 
        exists in addition to a nonterminal which represents the program as a 
        whole. It pops takes a look at the top element of the stack and uses it 
        to look up the valid combination of preceding tokens while considering 
        the current token that is being read by the scanner. The parser walks 
        the table using this logic, pushing terminals and nonterminals onto the
        parse stack based on the result of the current index of the parse table
        until either an invalid combination of tokens is discovered or the end 
        of file token is reached.
    
    Associated documentation files:
        -doc/parser/extended_grammar.txt
        -doc/parser/fist_and_follow_sets.txt
        -doc/parser/parse_table.pdf
            ->doc/parser/parse_table.ods
       
-- Scanner, Project 1:
    
    Associated impelementation files:
        -kleins
        -src/k_token.py
        -src/scanner.py

    Scanner Description:
        The scanner is the portion of the compiler which takes as input a klein 
        program as a single string and splits the string into a set of tokens. 
        The token class is described in k_token.py. The scanner steps through 
        each character of the program string and uses a set of conditions to 
        determine if a resultant character or string is a valid token. These 
        conditions are based on the possible terminals present in the language 
        specification. These may either be a single character, such as the case 
        of the unary and binary operators, or can be a string, such as any 
        identifier or number. Thus the conditions are based on a set of regular 
        expressions, noted in the scanner portion of the documents folder. 
        These regular expressions are used to build the conditions in place, 
        represented by the FSA diagram which is also housed in the same folder.

    Associated documentation files:
        -doc/scanner/regex.txt
        -doc/scanner/regex_FSA.jpg
            ->doc/regex_FSA.jff is the jflap file used to create the above jpeg.
        -doc/scanner/scanner_status_check.txt
         
--- The Repository ---

    --The home directory is KLEINcompiler/
        -The home directory is currently where the compiler will output any 
        error logs. This needs to be changed; an error_log folder should be 
        created for this purpose.
        
        -The home directory is also home to the various shell scripts used to 
        test the various stages of the compiler. The associations are noted in 
        the above project sections.
            ->./kleins
            ->./kleinf
            ->./kleinp
            *To run each script, run the  following command: 
            'sh <script name> <program to be tested>'
                *->Example: sh kleinf programs/multiply.kln     
                
        -The doc directory houses various forms of documentation, housed in 
        folders in respect to their implementation.
        
        -The programs directory houses various Klein programs used for testing 
        the various stages of our compiler. These are the files used as input 
        for the klein scripts housed in the home directory.
        
        -The src directory houses all files used for implementation of the 
        compiler
        
        -The tests directory houses files used to run the shell scripts noted 
        above
