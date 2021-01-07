Specification
=============
- We want to parse the antimony string and identify problems without converting the antimony code to sbml. 
    - Do this using the lark-parser along with the antimony grammar (that we can get from libAntimony source code)
- We want syntax highlighting (in which case we should rename the package to something more inclusive)
- Implement A "Nice" and a "Naggy" mode which have different sets of checks turned on or off by default
- Fully customizable list of checks that can be turned on or off. 


Warnings
---------
- missing semi-colon
- no compartment set, using default compartment
- Unnamed reaction
- two reactions with the same rate law. 
- Fully duplicate reactions
- check for existance of filepaths in antimony import statements. 

Errors
--------
- missing rate law
- species/compartment/parameter appears in reaction but no value set
- Two reactions with the same name



Improvements
------------
- Identify where code can be expressed more concisely, highlight and tell the user. 
- like: 
    - species A, B, C in Cell; 
- instead of: 
    - species A in Cell;
    - species B in Cell;
    - species C in Cell;
    















