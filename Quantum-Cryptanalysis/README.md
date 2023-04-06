# First Attempts at Cryptanalyzing a (Toy) Block Cipher by Means of Quantum Optimization Approaches

This repository contains all the raw data and instances used to write the extended paper "First Attempts at Cryptanalyzing a (Toy) Block Cipher by Means of Quantum Optimization Approaches" and the original paper "A First Attempt at Cryptanalyzing a (Toy) Block Cipher by Means of QAOA" [[1]](#1) by L. Phab, S. Louise and R. Sirdey.

To cite this work, please use:
```
@inproceedings{
    PhabEtAl2022,
    title={{A First Attempt at Cryptanalyzing a (Toy) Block Cipher by Means of QAOA}},
    author={Phab, Luca and Louise, St{\'e}phane and Sirdey, Renaud},
    booktitle={International Conference on Computational Science},
    pages={218--232},
    year={2022},
    organization={Springer},
    doi={https://doi.org/10.1007/978-3-031-08760-8_19}
}
```

--------

## Instances folder
### Content
* `phi<X>.cnf` (resp. `phi<X>.sol`) files where &#60;X&#62; is a number contains the CNF instances derived from the known-plaintext attack (resp. the corresponding MIN-SAT and MAX-SAT optimal solutions) used to evaluate and compare QAOA and the QA algorithm.
* `sample` folder contains all instances (grouped in the subfolder `hf_n<X>` by number of variables &#60;X&#62;) derived from the known-plaintext attack (and their corresponding MIN-SAT and MAX-SAT optimal solutions) used to study the best parameters (reduction, instance type before applying the embedding, RCS) of the QA algorithm.

### File format description
#### CNF format
See CNF format in [[2]](#2).

#### Solution format
The extension of solution format is ".sol".
Each line starts with a character that specifies the line type and content:

* comment line:

    `c <comment>`

* from line:

     `f <type> <name>`

    where &#60;type&#62; is "file" and &#60;name&#62; is the filename containing the CNF instance to be solved.

* solution line:

    `s <type> <sol> <assign>`

    where &#60;type&#62; is "max" (resp. "min") if the solution correspond to a MAX-SAT (resp. MIN-SAT) solution, &#60;sol&#62; is the number of satisfied clauses and &#60;assign&#62; is the found solution. The solution is a sequence of values where &#60;i&#62; (resp. -&#60;i&#62;) means that the variable &#60;i&#62; must be set to True (resp. False).

----------

## Data folder
### Content
* `dwave` folder contains all data obtained by solving our instances and samples using D-Wave solvers:
  * `phi<X>_at_rcs0<Y>_ntr-kzfd_ising.csv` contains the results of the solving of our instance &#x03C6;&#60;X&#62; with a RCS of 0.&#60;Y&#62; for 10 random embeddings when varying the annealing time. The instance is first transformed into a QUBO instance using NTR-KZFD reduction, then it is converted into an Ising instance before applying an embedding.
  * `rcs_n<n>_f<Y>-<Z>_<red>_<type>.csv` contains the results of the solving of the formulas numbered from &#60;Y&#62; to &#60;Z&#62; (stored in the sample folder `instances/hf_n<n>`) with an annealing time of 20&#181;s for 10 random embeddings when varying RCS. The instance is first transformed into a QUBO instance using &#60;red&#62; reduction, then it is converted into &#60;type&#62; instance before applying an embedding.
* `qaoa` folder contains all data obtained by solving our instances using QAOA on Qiskit Aer simulators or IBM Quantum computers:
  * `phi<X>_p<pmax>_iter<Y>_<H>_<M><Z>.csv` contains the results of the solving of our instance &#x03C6;&#60;X&#62; when varying p from 1 to &#60;pmax&#62;, with the maxiter parameter of the classical optimizer set to &#60;Y&#62;, using the heuristic &#60;H&#62; on the simulator or real quantum computer &#60;M&#62; (if &#60;M&#62; is not specified in the filename then the qasm\_simulator was used). We've done the experiments several times so it is the &#60;Z&#62;-th experiment with these parameters (if &#60;Z&#62; is not explicited then &#60;Z&#62; = 1). 
* `random` folder contains all data obtained by solving our samples with a random selection solver:
  * `randomsolve_n<n>.csv` contains the results of the solving of the formulas numbered from 0 to 14 (stored in the sample folder `instances/hf_n<n>`) using a random selection solver.

Some CSV files begin with a comment line (starting with "#") that provides extra data about the solving or the instances.

### CSV header description
#### CSV header in QAOA files
* p: Number of QAOA layers
* avg_cost: Expectation value over &#60;shots&#62; executions
* opt_proba: Success probability over &#60;shots&#62; executions
* angles_i: optimal &#946;<sub>i</sub> found by the classical optimizer (i < p)
* angles_{i+p}: optimal &#947;<sub>i</sub> found by the classical optimizer (i < p)

&#60;shots&#62; is defined in the comment line and is always 256 for all our QAOA experiments.

#### CSV header in D-Wave files
Each line corresponds to the results over &#60;shots&#62;=100 executions. 

* j: Index of the formula to be solved
* k: Group id of &#60;shots&#62; executions (done with the same embedding)
* rcs: Relative Chain Strength (RCS)
* at: Annealing time (&#181;s)
* meanr: Mean of r<sup>*</sup>
* minr: Min of r<sup>*</sup>
* maxr: Max of r<sup>*</sup>
* proba: Success probability
* nbdup: Number of duplications
* maxdup: Maximum chain length
* nbduperrors: Sum over the &#60;shots&#62; executions of the number of duplication errors.

#### CSV header in random solving files
Each line corresponds to the results over &#60;shots&#62;=100 random solving.

* j: Index of the formula to be solved
* k: Group id of &#60;shots&#62; random solutions
* meanr: Mean of r<sup>*</sup>
* minr: Min of r<sup>*</sup>
* maxr: Max of r<sup>*</sup>
* proba: Success probability

----------

## References
<span id="1">[1]</span> **A First Attempt at Cryptanalyzing a (Toy) Block Cipher by Means of QAOA** \
L. Phab, S. Louise and R. Sirdey \
Computational Science-ICCS 2022: 22nd International Conference, London, UK, June 21-23, 2022, Proceedings, Part IV (pp. 218-232). \
DOI: [https://doi.org/10.1007/978-3-031-08760-8_19](https://doi.org/10.1007/978-3-031-08760-8_19)

<span id="2">[2]</span> **Satisfiability: Suggested Format** \
Challenge, DIMACS \
[https://www.domagoj-babic.com/uploads/ResearchProjects/Spear/dimacs-cnf.pdf](https://www.domagoj-babic.com/uploads/ResearchProjects/Spear/dimacs-cnf.pdf)
