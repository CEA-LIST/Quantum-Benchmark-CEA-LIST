#!/usr/bin python3.8.10
# -*- coding: utf-8 -*-
"""
@authors Valentin Gilbert <valentin.gilbert@cea.fr>

Description:
    MQLib heuristics to solve Maxcut problems
=========

"""

# third party import
import MQLib as mql

# local import
from TAQOS.env import RTSEC


def format_mqlib_results(heuristic, instance, result, rtsec):
    """
    Format the results obtained from MQLib solvers

    Parameters
    ----------
    heuristic : string
        name of the heuristic
    instance : Instance
        instance being solved
    result : dict
        result structure returned by the MQLib
    rtsec : int
        processing time limit (in second)

    Returns
    -------
        dictionary storing the result of the simulation
    """
    solution_dict = dict(zip([i for i in instance.graph.nodes()], result['solution']))

    res_dict = {
        'heuristic_name': heuristic,
        'time': {
            'wall_clock_time': rtsec
        },
        'parameter_setting': {
            'max_runtime': rtsec
        },
        'solution': {
            'best_partition': solution_dict,
            'best_cut_size': instance.get_cut_size(solution_dict),
            'best_energy': instance.compute_energy(solution_dict)
        },
        'extra': {
            'bestsolhistory_objvals': result['bestsolhistory_objvals'],
            'bestsolhistory_runtimes': result['bestsolhistory_runtimes']
        }
    }

    return res_dict


def run_mql_heuristic(heuristic, instance, rtsec=RTSEC):
    """
    Run MQLib heuristic

    Parameters
    ----------
    heuristic : string
        name of the heuristic
    instance : Instance
        instance being solved
    rtsec : int
        processing time limit (in second)

    Returns
    -------
        dictionary storing the result of the simulation
    """
    result = mql.runHeuristic(heuristic, instance.to_mqlib_instance(), rtsec=rtsec)
    return format_mqlib_results(heuristic, instance, result, rtsec)
