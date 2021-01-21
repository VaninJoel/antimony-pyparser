# antimony-pyparser
Small Python package for parsing antimony using Pythons [lark](https://github.com/lark-parser/lark). 

## Current Development strategy
* Adopt the original Bison code and reshape it until all the [original test strings](https://github.com/sys-bio/antimony/tree/develop/src/test/test-data) parse.
* Keep the grammar as similar as possible to the original Bison code. 

## Alternative strategies
* Use an alternative tool for using the original bison grammar directly. [pybison](https://github.com/smvv/pybison) seems reasonable.
* Write the grammar from the ground up in a TDD style. This might actually be an easier development strategy as 
  we could make incremental steps, but clearly more work than adopting the original. 
