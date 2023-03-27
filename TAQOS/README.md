# TAQOS Benchmark protocol

TAQOS is a benchmark protocol to perform a Tight Analysis of Quantum 
Optimization Systems.

We recommend executing the source code with python 3.8.10. in a virtual
environment.

## Configuration of the environment

Environment variables are stored in the file **env.py**. Check
these variables before running any script (especially the D-Wave token and project path)

```shell
# Set the python path of your project directory containing the directory TAQOS
export PYTHONPATH=path/to/project/directory

# Create a virtual environment with python 3.8.10
python -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# run a jupyter notebook
jupyter-notebook
```

You're all set, you can access the content of the notebooks on a web 
browser: 127.0.0.1:8888

## Directory description

- **db**: Stores the maxcut instances. The description of each instance 
is stored in text files in maxcut_db. The results are stored as JSON 
files in maxcut_results
- **demo**: Semonstration notebook that give examples to use to library.
- **graph_generator**: Used for graph generation.
- **heuristic**: MQLib and D-Wave solvers.
- **instance_metrics**: Metrics and coverage tools.
- **logger**: Logging system.
- **problem**: Instance structure.

## File description

- **env.py**: Stores the environment variables.
- **maxcut.py**: TAQOS features for the maxcut problem.

## How to use the library

Please refer to the demonstration notebooks available in the
directory **demo** to get insights on how to use the library.

## Licence
This work is under CeCILL-B free software licence agreement.