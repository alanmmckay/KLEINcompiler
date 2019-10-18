# KLEINcompiler
Translation of Programming Languages Compiler Project

Team Name: Fork Bomb
Team Members: Tyler Rahe, Alan Mckay, Killian


Project Description:

In this project we are creating a compiler that takes as input programs written in Klein, and produces output programs written in the assembly language TM.

--- Scanner, Project 1---

For this portion we needed to create a program that would take in a programs written in the Klein language and output a stream of tokens. To do this we first started by understanding the klein language and what constitutes a token in the language.  Next we set up regular expressions for each defined token.  After that we created a DFA using those reg ex's to base our code off.  In the DOCS directory you will be able to see the defined reg ex's as well as the state machine. Our state machine is not totally complete as it does not handle comments in the language and does not have returns coming off each state, so that it did not get too large just keep that in mind when reviewing it.  We have not run in to any cases where our code does not handle a program with legal Klein tokens. If any are found please notify one of us so that we can rectify this. Having said that currently when our compiler see's a comment it returns a token of none type. Our code reflects our state machine in concept but not perfectly in documentation, there will be comments in the code to clarify location within the state machine.


--- Parser, Project 2 ---

Status:

-Finished:
    ->Refactoed Grammar
        -Located in doc/refactored-grammar.txt
    ->First Sets
        -Located in doc/first-and-follow-sets.txt
    ->Follow Sets
        -Located in doc/first-and-follow-sets.txt
    ->Parse Table
        -Located in doc/parse_table_verbose.ods
            ->doc/parse_table.ods is the parse table which refers to the line numbers of each grammar statement located in refactored-grammar.txt
            ->There are pdfs of these files too.
            
Our team lost some time calculating the follow sets. We ended up checking our work using some online calculators, and lost our confidence when the results of these calculators weren't consistent with the rules for figuring a follow set.

The first and follow sets are defined functionally, followed up by literal definitions:
    i.e., first(FORMALS) = {first(NONEMPTYFORMALS), ε) = {identifier, ε}.
    
-Unfinished
    ->parse_table.py
    ->parser.py

Implementing our parse table is the current hold up. What we have set in parse_table.py is two enumeration classes and a dictionary representing the parse table.
    -Each index of the parse table dictionary is an immutable dictionary. This means each tuple must be unique.  The first value is a NonTerminal and the second value is a Terminal. Our initial implementation used token type, instead of a terminal value, to determine what action to take. As our token types are defined, this causes problems. For example, there is a case where (EXPR-TAIL, OPERATORS) leads to two different outcomes, one which is an epsilon case and another that puts < <EXPR> onto the stack.
    -Thus an enumeration class was created to represent the various terminals. The challenge we are currently facing is how to check for these Terminal types when passing values to index into the parse table dictionary.
        ->To solve this we are considering implementing tuples of three, passing terminal values as the third index of the tuple for terminals which are defined within the Terminal enumeration class. We would pass some sort of null value for the other cases.
        ->One approach we are also considering is expanding the set of token types.
        
What also needs to be done is a clean up of our directories and readme. Some consistency also needs to be had in terms of our coding standards. On our todo list is also expanding on valid and invalid tests cases and Klein programs.

--- The Repository ---

home directory = KLEINcompiler

doc:
begin_state_machine.jff - JFlap file for our state machine
klein_machine.jpg - this is an image of the state machine we came up with, it is missing comments and returns off certain states to minimize size for easier understanding.
regex.txt - this file contains our reg ex's for each token
scannerstatuscheck.txt - this is our initial check in on the project.
refactored-grammar.txt
first-and-follow-sets.txt
parse_table.ods
parse_table.pdf
parse_table_verbose.ods
parse_table_berbose.pdf

programs:
This directory contains legal and non legal Klein programs to test our compiler with.
multiply.kln - this is the legal program created by the team.

src:
errors.py
k_token.py - this is the file that sets up token type, what it is, and how it is represented.
scanner.py - this is the file that the program is ran through where characters are defined as specific token types.
parse_table.py - The file that contains the parse table as a dictionary.
parser.py - The file that parses through a set of tokens.
tests.py - contains tests for the scanner and token class

tests:
print_tokens.py - this file reads the program into a string, feeds it into the scanner and outputs token representation.

kleins:
Is a shell script that tests the scanner.

kleinsf:
A shell script that tests the parser.

TO RUN:

Run the command > sh klein(s/f) programs/print-one.kln
(programs/print-one.kln) - in the command above can be replaced with the file path to any klein program.
