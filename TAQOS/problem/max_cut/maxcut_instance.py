#!/usr/bin python3.8.10
# -*- coding: utf-8 -*-
"""
@authors Valentin Gilbert <valentin.gilbert@cea.fr>

Description:
    Instance structure of the Maxcut problem
=========
"""

# third party import
import MQLib as mql
import networkx as nx

# local import
from TAQOS.instance_metrics.graph_metrics import get_metrics
from TAQOS.problem.instance import Instance
from optimization_problems.common.logging_device import create_logger, \
    log_debug


class MaxCutInstance(Instance):
    def __init__(self, id, graph):
        """
        Build the maxcut instance from filepath

        Parameters
        ----------
        id: int
            path of the instance
        graph: networkx graph
            input graph
        """
        super().__init__(id)
        self.graph = graph

    def to_ising(self):
        """
        Compute auto-coupling and coupling factors

        Returns
        -------
            dict of auto-coupling bias (h_dict)
            dict of coupling bias (J_ij_dict)
        """
        J_ij_dict = {}
        for ed in self.graph.edges():
            J_ij_dict[(int(ed[0]), int(ed[1]))] = self.graph.edges()[ed][
                'weight']

        h_dict = {}
        for bias in self.graph.nodes():
            h_dict[int(bias)] = 0

        return h_dict, J_ij_dict

    def to_mqlib_instance(self):
        """
        Build MQLib instance from the current graph

        Returns
        -------
            MQLib instance
        """
        return mql.Instance('M', self.graph)

    def get_metrics(self):
        """
        Compute the list of metrics associated to the instance

        Returns
        -------
            dict<str, double>: dictionary of metrics
        """
        return get_metrics(self.graph)

    def compute_energy(self, solution_dict):
        """
        Compute the energy associated to a solution

        Parameters
        ----------
        solution_dict : dict<string, int>
            Partition of each node

        Returns
        -------
            float: energy of the solution
        """
        sol_energy = 0
        for ed in self.graph.edges():
            sol_energy += self.graph.edges()[ed]['weight']*solution_dict[ed[0]]*solution_dict[ed[1]]

        return sol_energy

    def get_cut_size(self, solution_dict):
        partition = [k for k, v in solution_dict.items() if v == 1]
        return nx.cut_size(self.graph, partition, weight='weight')
