#!/usr/bin python3.8.10
# -*- coding: utf-8 -*-
"""
@authors Valentin Gilbert <valentin.gilbert@cea.fr>

Description:
    Computes coverage metrics associated to graphs.
"""

# third party import
import networkx as nx
import numpy as np

# local import


def get_metrics(G):
    """
    Returns the metrics associated to the graph G

    Parameters
    ----------
        G : networkx graph

    Returns
    -------
        dict<string, float> store the metrics associated to the graph
    """

    # Create the list of degree for each node
    degree_list = G.degree(G.nodes())

    # Eccentricity normalized by the number of nodes
    eccentricity = [v / G.number_of_nodes() for k, v in nx.eccentricity(G).items()]

    # Mean of neighbor degree
    neighbor_degree_list = list(nx.average_neighbor_degree(G).values())

    metric_dict = {
        # Density
        'density': nx.density(G),

        # Diameter of the graph normalized by the number of nodes
        'diameter': nx.diameter(G) / G.number_of_nodes(),

        # Eccentricity: the eccentricity of a node v is the maximum distance
        # from v to all other nodes in G
        'min_eccentricity': min(eccentricity),
        'max_eccentricity': max(eccentricity),
        'mean_eccentricity': np.mean(eccentricity),
        'stdev_eccentricity': np.std(eccentricity),

        # Metrics relative to the degree of the nodes in the graph
        # normalized by the maximum possible degree (number of nodes - 1)
        'min_degree': min([d[1] for d in degree_list]) / (G.number_of_nodes() - 1),
        'max_degree': max([d[1] for d in degree_list]) / (G.number_of_nodes() - 1),
        'mean_degree': np.mean([d[1] for d in degree_list]) / (G.number_of_nodes() - 1),
        'stdev_degree': np.std([d[1] for d in degree_list]) / (G.number_of_nodes() - 1),

        # Average neighbor degree
        'min_neighbor_degree': min(neighbor_degree_list) / (G.number_of_nodes() - 1),
        'max_neighbor_degree': max(neighbor_degree_list) / (G.number_of_nodes() - 1),
        'mean_neighbor_degree': np.mean(neighbor_degree_list) / (G.number_of_nodes() - 1),
        'stdev_neighbor_degree': np.std(neighbor_degree_list) / (G.number_of_nodes() - 1),

        # Algebraic connectivity
        # Second smallest eigenvalue of the Laplacian matrix
        'algebraic_connectivity': nx.algebraic_connectivity(G)
    }

    return metric_dict
