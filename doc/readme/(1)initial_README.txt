# KLEINcompiler
Translation of Programming Languages Compiler Project

Team Name: Fork Bomb
Team Members: Tyler Rahe, Alan Mckay, Killian


Project Description:

In this project we are creating a compiler that takes as input programs written in Klein, and produces output programs written in the assembly language TM.

The first portion of this project and the portion that is currently complete is the scanner portion.

For this portion we needed to create a program that would take in a programs written in the Klein language and output a stream of tokens. To do this we first started by understanding the klein language and what constitues a token in the language.  Next we set up regular epressions for each defined token.  After that we created a DFA using those reg ex's to base our code off.  In the DOCS directory you will be able to see the defined reg ex's as well as the state machine. Our state machine is not totally complete as it does not handle comments in the language and does not have returns coming off each state, so that it did not get too large just keep that in mind when reviewing it.  We have not run in to any cases where our code does not handle a program with legal Klein tokens. If any are found please notify one of us so that we can rectify this. Having said that currently when our compiler see's a comment it returns a token of none type. Our code reflects our state machine in concept but not perfectly in documentation, there will be comments in the code to clarify location within the state machine.


The Repository:

home directory = KLEINcompiler

doc:
begin_state_machine.jff - JFlap file for our state machine
klein_machine.jpg - this is an image of the state machine we came up with, it is missing comments and returns off certain states to minimize size for easier understanding.
RegularExpressions.txt - this file contains our reg ex's for each token
scannerstatuscheck.txt - this is our initial check in on the project.

programs:
This directory contains legal and non legal Klein programs to test our compiler with.
multiply.kln - this is the legal program created by the team.

src:
errors.py
k_token.py - this is the file that sets up token type, what it is, and how it is represented.
scanner.py - this is the file that the program is ran through where characters are defined as specific token types.
tests.py - contains tests for the scanner and token class

tests:
print_tokens.py - this file reads the program into a string, feeds it into the scanner and outputs token representation.

kleins:
Is a shell script that kicks off the process.


TO RUN:

To kick off the scanner portion of the project we will be using the shell script described above.

Run the command > sh kleins programs/print-one.kln
(programs/print-one.kln) - in the command above can be replaced with the file path to any klein program.
