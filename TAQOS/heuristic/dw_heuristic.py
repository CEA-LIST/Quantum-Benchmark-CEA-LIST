#!/usr/bin python3.8.10
# -*- coding: utf-8 -*-
"""
@authors Valentin Gilbert <valentin.gilbert@cea.fr>

Description:
   D-Wave heuristics used to solve optimisation problems
=========

"""

# third party import
import timeit
from dwave.system import DWaveSampler

# local import
from TAQOS.env import DW_AN_TIME, DW_NUM_READS, DWAVE_TOKEN

# Mapping between heuristic name and solver name
SOLVER_MAP = {
    'DW_2000Q_wo_embedding': 'DW_2000Q_6',
    'DW_Adv4.1_wo_embedding': 'Advantage_system4.1',
    'DW_Adv6.1_wo_embedding': 'Advantage_system6.1',
    'DW_Adv2_wo_embedding': 'Advantage2_prototype1.1'
}


def _get_dw_sampler(solver):
    """
    Get the D-wave sampler
    Parameters
    ----------
    solver : str
        name of the solver: 'DW_2000Q_6', 'Advantage_system4.1',
            'Advantage_system5.2', 'Advantage_system6.1',
            'Advantage2_prototype1.1'

    Returns
    ----------
    graph being solved
    """

    # Get the sampler from
    dw_sampler = DWaveSampler(
        endpoint='https://cloud.dwavesys.com/sapi',
        token=DWAVE_TOKEN,
        solver=solver,
        retry_interval=30
    )

    return dw_sampler


def format_dwave_results(heuristic, instance, sample_set, annealing_time, num_reads, service_time, embedding, embedding_time):
    """
    Format the results obtained from D-Wave quantum computer

    Parameters
    ----------
    heuristic : string
        name of the heuristic
    instance : Instance
        instance being solved
    sample_set : D-Wave SampleSet
        dictionary storing D-Wave results
    annealing_time : int
        annealing time in micro seconds
    num_reads : int
        number of annealing runs
    service_time : float
        D-Wave service time (from the call to the reception of the results)
        in seconds
    embedding : dict
        mapping of the variables to the qubits
    embedding_time : float
        embedding time, in seconds

    Returns
    -------
        dictionary storing the result of the simulation
    """
    sample_list = []

    wost_energy = max([float(energy) for energy, in sample_set.data(fields=['energy'])])

    best_partition = None
    mean_energy = 0
    best_energy = 0
    best_cut_size = 0

    # Convert the solution to bit string and perform the majority vote
    for sample_dict, occurence, energy in sample_set.data(
            fields=['sample', 'num_occurrences', 'energy']):
        occurence = int(occurence)
        energy = float(energy)

        if energy < best_energy:
            best_energy = energy
            best_partition = sample_dict

            for k in list(sample_dict.keys()):
                sample_dict[str(k)] = sample_dict[k]
                del sample_dict[k]

            best_cut_size = instance.get_cut_size(sample_dict)

        mean_energy += (occurence*energy)/num_reads

        sample_list.append({
            'sample': sample_dict,
            'num_occurrences': occurence,
            'energy': energy
        })

    energy_list = []
    for res_sample in sample_list:
        energy_list.append(res_sample['energy'])

    wall_clock_time = service_time * 10 ** 6 + embedding_time * 10 ** 6

    res_dict = {
        'heuristic_name': heuristic,
        'time': {
            'wall_clock_time': wall_clock_time,
            'dwave_service_time': service_time * 10 ** 6,
            'embedding_time': embedding_time * 10 ** 6,
            'qpu_time_info': sample_set.info['timing'],
        },
        # Specific parameters used for the heuristic
        'parameter_setting': {
            'embedding': embedding,
            'annealing_time': annealing_time,
            'num_reads': num_reads
        },
        'solution': {
            'best_partition': best_partition,
            'best_cut_size': best_cut_size,
            'best_energy': best_energy,
            'worst_energy': wost_energy,
            'mean_energy': mean_energy
        },
        'extra': {
            'sample_list': sample_list,
        }
    }

    return res_dict


def run_dw_heuristic(heuristic, instance,
                     annealing_time=DW_AN_TIME,
                     num_reads=DW_NUM_READS):
    """
    Run D-Wave quantum heuristic.

    Parameters
    ----------
    heuristic : string
        name of the heuristic
    instance : Instance
        instance being solved
    annealing_time : int
        annealing time in micro seconds
    num_reads : int
        number of annealing runs

    Returns
    -------
        dictionary storing the result of the simulation
    """
    if heuristic not in SOLVER_MAP:
        raise ValueError(f'Unknown heuristic {heuristic}')

    solver_name = SOLVER_MAP[heuristic]

    dw_sampler = _get_dw_sampler(solver_name)

    h_dict, J_ij_dict = instance.to_ising()

    start_time = timeit.default_timer()
    sample_set = dw_sampler.sample_ising(
        h_dict, J_ij_dict,  num_reads=num_reads,
        annealing_time=annealing_time
    )
    sample_set.resolve()
    finish_time = timeit.default_timer()
    service_time = finish_time - start_time

    # Ignore embedding processing
    embedding = dict(zip(
        list(instance.graph.nodes()), list(instance.graph.nodes())
    ))

    return format_dwave_results(
        heuristic, instance, sample_set, annealing_time,
        num_reads, service_time, embedding, embedding_time=0
    )
