#!/usr/bin python3.8.10
# -*- coding: utf-8 -*-
"""
@authors Valentin Gilbert <valentin.gilbert@cea.fr>

Description:
   TAQOS library functions for the Maxcut problem.
=========

"""

# third party import

# local import
from TAQOS.heuristic.max_cut_heuristics import get_maxcut_heuristic, \
    run_maxcut_heuristic
from TAQOS.problem.max_cut.db_manager import list_instance_list, \
    load_maxcut_instance_list, save_maxcut_instance_list
from TAQOS.problem.max_cut.instance_generation import \
    generate_dwave_instance_group


def load_instance_list(group_name):
    """
    Load the instance list corresponding to a group name

    Parameters
    ----------
    group_name : string
        name of the group

    Returns
    -------
        InstanceList list of instances corresponding to the group
    """
    return load_maxcut_instance_list(group_name)


def save_instance_list(instance_list):
    """

    Parameters
    ----------
    instance_list :

    Returns
    -------

    """
    save_maxcut_instance_list(instance_list)


def list_instances():
    """
    List the available group of instances

    Returns
    -------
        list<string> group of instances
    """
    return list_instance_list()


def list_heuristics():
    """
    Gets the list of available heuristics

    Returns
    -------
        List of available heuristics
    """
    return get_maxcut_heuristic()


def run_heuristic(name, instance, *args, **kwargs):
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
    return run_maxcut_heuristic(name, instance, *args, **kwargs)


def generate_instance_group(group_name, solver_name, edge_weights, nb_instance):
    """
    Generate an instance group based on D-Wave chip topology

    Parameters
    ----------
    group_name : str
        group name
    solver_name : str
        should be a string in the list:
        ['DW_2000Q_6', 'Advantage_system4.1'
         'Advantage_system6.1', 'Advantage2_prototype1.1']
    edge_weights : distribution of weights
    nb_instance : int
        number of instances

    Returns
    -------
        InstanceList object that stores the list of instances
    """
    return generate_dwave_instance_group(group_name, solver_name, edge_weights, nb_instance)
