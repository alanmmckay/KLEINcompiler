# KLEINcompiler
Translation of Programming Languages Compiler Project
Team Name: Fork Bomb
Team Members: Tyler Rahe, Alan Mckay, Killian Bailey


Project Description:

The project goal is to create a compiler that takes as input a program written 
in Klein and outputs the equivalent program written in the assembly language 
TinyMachine.


-- Final Submission, Project 7:

    Project 7 is to implement some form of optimization to the TM output. 
    Unfortunately we did not get around to this. We did do some clean up and 
    fixes pertaining to areas lacking in the previous stages.
    
    What was completed:
    -TM programs now allow arguments to be fed in through the command line.
        ->The DMEM allocated to the initial main function call now factors the 
        arguments that may exist when the TM machine runs.
    -Function declaration output no longer saves and restores register values 
    for temporary register usage.
    -Negation and Not operation tm output is fixed.
    -Type checking error messages have been refined and are more informative.
    -A whole slew of klein programs have been created for testing purposes.
    -Directory restructuring.
    
    
--- The Compiler ---

The compiler has implements all features of klein as described in 
http://www.cs.uni.edu/~wallingf/teaching/cs4550/compiler/specification.html
except:
    -Arithmetic operations operate from right to left when stringed with
    operations within their respective set ({+,-},{*,/}).
        ->This can be prevented by taking full advantage of parenthesis to group
          respective operands.
          
Flaws in implementation:
    -A lot of the logic is loaded into AST_node.py. This is the file which 
    houses the class information for the abstract syntax tree. The layout itself
    is quite clever, but type check and code generation methods are added to 
    them. This poses a problem in terms of separation of responsibility. The 
    logic in AST_node.type_check() is specific to type checking klein programs;
    the logic in in AST_node.code_gen() is specific to outputting code in tm.
    Provided more time, we would explore a means to refactor these methods into
    some exterior mechanism beside the abstract syntax tree.
    
    -The tm being output is not efficient, ignoring the lack of any optimizer 
    implementation. Most instructions output have the value stored in some 
    memory position. This produces a lot of redundant instructions to IMEM and 
    a lot of redundant data to DMEM. The most egregious lack of optimization 
    comes from the IdentifierNode outputting a load instruction. This was an 
    adhoc fix to print statements having no means to access an argument.
    
    -The error handling needs to be expanded upon. Effort was strong in the 
    beginning of the project, but stalled out when time started becoming more 
    of a premium and workload was shifted away from this effort. Error returns 
    pertaining to parse errors do not help the user of a compiler as they are 
    more geared for compiler debugging.
    
         
--- The Repository ---

    --The home directory is KLEINcompiler/
        -The home directory is where error logs will be output.
        
        -The home directory is also home to the various shell scripts used to 
        test the various stages of the compiler. Each represents an running the
        compiler for each implementation stage of this project.
            ->./kleins : scanner; creation of a set of tokens
            ->./kleinf : parse table look ups
            ->./kleinp : abstract syntax tree creation
            ->./kleinv : type checker
            ->./kleinc : code_generation; the completed compiler
            *To run each script, run the  following command: 
            'sh <script name> <program to be tested>'
                *->Example: sh kleinc programs/exclusive_or.kln     
                
        -The doc directory houses various forms of documentation, housed in 
        folders in respect to their implementation.
        
        -The programs directory houses a small handful of programs we've created
        for the use of the compiler. It also houses a set of programs provided
        by Dr. Wallingford within the class-programs folder.
        
        -The tests directory houses various Klein programs used for testing 
        the various stages of our compiler.
        
        -The src directory houses all files used for implementation of the 
        compiler
            -src/drivers houses files used to run the shell scripts, noted above
