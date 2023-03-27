#!/usr/bin python3.8.10
# -*- coding: utf-8 -*-
"""
@authors Valentin Gilbert <valentin.gilbert@cea.fr>

Description:
    Generate instances of the maxcut problem
=========
"""

# third party import
import random

# local import
from TAQOS.graph_generator.dwave_graph_generation import get_dw_sampler_graph
from TAQOS.problem.max_cut.maxcut_instance import MaxCutInstance
from TAQOS.problem.max_cut.maxcut_instance_list import MaxcutInstanceList


def generate_dwave_instance_group(group_name, solver_name, edge_weights, nb_instance):
    """
    Generate maxcut instance group based on D-Wave solver topology

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
    instance_list = MaxcutInstanceList(group_name)
    graph = get_dw_sampler_graph(solver_name)

    for i in range(nb_instance):
        graph_i = graph.copy()

        # Generate random weight from the list edge_weight
        for edge in graph_i.edges():
            graph_i[edge[0]][edge[1]]['weight'] = random.choice(edge_weights)

        instance = MaxCutInstance(i, graph_i)
        instance_list.append(instance)

    return instance_list
