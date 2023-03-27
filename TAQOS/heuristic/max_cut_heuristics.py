#!/usr/bin python3.8.10
# -*- coding: utf-8 -*-
"""
@authors Valentin Gilbert <valentin.gilbert@cea.fr>

Description:
    Heuristics used to solve Maxcut problems
=========

"""

# third party import

# local import
from TAQOS.heuristic.dw_heuristic import run_dw_heuristic
from TAQOS.heuristic.mqlib_heuristic import run_mql_heuristic

# List of heuristic using MQLib
MQLIB_HEURISTICS = [
    'BASELINE',
    'DUARTE2005',
    'FESTA2002GPR',
    'FESTA2002GVNS',
    'FESTA2002GVNSPR'
]

# List of heuristics using D-Wave systems
DW_HEURISTICS = [
    'DW_2000Q_wo_embedding',
    'DW_Adv4.1_wo_embedding',
    'DW_Adv6.1_wo_embedding',
    'DW_Adv2_wo_embedding'
]


def get_maxcut_heuristic():
    """
    Return the list and brief description of available heuristics

    Returns
    -------
        dict<string, string>: name and description of the heurisitic
    """
    heuristics = {
        'Maxcut': {
            # Heuristics available in the MQLib:
            'BASELINE': 'Baseline heuristic',
            'DUARTE2005': 'Genetic algorithm with VNS as local search',
            'FESTA2002GPR': 'GRASP with path-relinking',
            'FESTA2002GVNS': 'GRASP with VNS local search',
            'FESTA2002GVNSPR': 'GRASP & VNS with path-relinking',

            # D-Wave heuristics (without embedding step):
            'DW_2000Q_wo_embedding': 'D-Wave 2000Q (Chimera topology) without embedding',
            'DW_Adv4.1_wo_embedding': 'D-Wave Advantage 4.1 (Pegasus topology) without embedding',
            'DW_Adv6.1_wo_embedding': 'D-Wave Advantage 6.1 (Pegasus topology) without embedding',
            'DW_Adv2_wo_embedding': 'D-Wave Advantage2 (Zephyr topology) without embedding'
        }
    }

    return heuristics


def run_maxcut_heuristic(name, instance, *args, **kwargs):
    """
    Run classical or quantum heuristic and return the

    Parameters
    ----------
    name : string
        name of the heuristic.
        Classical heuristics:
            'BASELINE': random
            'DUARTE2005': Genetic algorithm with VNS as local search
            'FESTA2002GPR': GRASP with path-relinking
            'FESTA2002GVNS': GRASP with VNS local search
            'FESTA2002GVNSPR': GRASP & VNS with path-relinking

            See MQLib documentation for more infos:
            https://github.com/MQLib/MQLib

        Quantum heuristics:
            'DW_2000Q_wo_embedding': D-Wave 2000Q annealer without embedding step
            'DW_Adv4.1_wo_embedding': D-Wave Advantage 4.1 without embedding step
            'DW_Adv6.1_wo_embedding': D-Wave Advantage 6.1 without embedding step
            'DW_Adv2_wo_embedding': D-Wave Advantage 2 without embedding step

    instance: MaxCutInstance
        instance being solved

    kwargs:
        For classical heuristics:
            rtsec: int
                maximal running time in seconds
            see env.py for default values being used

        For DW heuristics:
            annealing_time: int
                annealing time in micro seconds
            num_reads: number of shots
            see env.py for default values being used

    Returns
    -------
        dictionary storing results with keys:
            'time': details about the running time of the heuristic
            'parameter_setting': heuristic settings
            'solution': details about the solution
            'extra': extra information specific to the heuristic run
    """

    if name in MQLIB_HEURISTICS:
        return run_mql_heuristic(name, instance, *args, **kwargs)
    elif name in DW_HEURISTICS:
        return run_dw_heuristic(name, instance, *args, **kwargs)
    else:
        raise ValueError(f'Unknown heuristic {name}')
