#!/usr/bin python3.8.10
# -*- coding: utf-8 -*-
"""
@authors Valentin Gilbert <valentin.gilbert@cea.fr>

Description:
    Generate Graphs based on D-Wave annealers' architecture
=========
"""

# third party import
from dwave.system import DWaveSampler

# local import
from TAQOS.env import DWAVE_TOKEN


def get_dw_sampler_graph(solver):
    """
    Return the graph associated to a D-Wave sampler

    Parameters
    ----------
    solver str
        solver name: ['DW_2000Q_6', 'Advantage_system4.1'
            'Advantage_system6.1', 'Advantage2_prototype1.1']

    Returns
    -------
        networkx graph associated to the solver
    """

    dw_sampler = DWaveSampler(
        endpoint='https://cloud.dwavesys.com/sapi',
        token=DWAVE_TOKEN,
        solver=solver,
        retry_interval=30
    )

    return dw_sampler.to_networkx_graph()
