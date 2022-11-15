## File format description

### CNF format
See DIMACS CNF format : [http://www.satcompetition.org/2011/format-benchmarks2011.html](http://www.satcompetition.org/2011/format-benchmarks2011.html)

### Solution format
The extension of solution format is ".sol".
Each line start with a character that specifies the line type and content:

* Comment line: It is the same as in CNF format

* From line: 

     `f <type> <name>`

    where &#60;type&#62; is "file" and &#60;name&#62; is the filename containing the CNF instance to be solved.

* Solution line:

    `s <type> <sol> <assign>`

    where &#60;type&#62; is "min" (resp. "max") if the solution correspond to a MAX-SAT (resp. MIN-SAT) solution, &#60;sol&#62; is the number of satisfied clauses and &#60;assign&#62; is the solution found for the problem. The solution is a sequence of values where `i` (resp. `-i`) means that the variable `i` must be set to `True` (resp. `False`).