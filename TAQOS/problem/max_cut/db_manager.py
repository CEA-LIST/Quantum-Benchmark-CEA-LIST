#!/usr/bin python3.8.10
# -*- coding: utf-8 -*-
"""
@authors Valentin Gilbert <valentin.gilbert@cea.fr>

Description:
    Basic function to list and load the instances
=========
"""

# third party import
import glob
import os
import networkx as nx

# local import
from TAQOS.env import PROJECT_PATH
from TAQOS.problem.max_cut.maxcut_instance import MaxCutInstance
from TAQOS.problem.max_cut.maxcut_instance_list import MaxcutInstanceList
from optimization_problems.common.logging_device import log_warning

# Path where the instances are saved
MAXCUT_DB_PATH = os.path.join(PROJECT_PATH, 'db', 'maxcut_db')


def list_instance_list():
    """
    List the available group of instances

    Returns
    -------
        list<string> group of instances
    """
    db_list = []

    for directory in glob.glob(f'{MAXCUT_DB_PATH}/*'):
        db_list.append(os.path.basename(directory))

    return db_list


def load_maxcut_instance_list(group_name):
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
    path = os.path.join(MAXCUT_DB_PATH, group_name)
    instance_list = MaxcutInstanceList(group_name)

    for file_path in glob.glob(path+'/*.txt'):
        fi = open(file_path, 'rb')
        graph = nx.read_weighted_edgelist(fi)
        id = int(file_path.split('/')[-1].split('_')[0])
        maxcut_instance = MaxCutInstance(id, graph)
        instance_list.append(maxcut_instance)

    return instance_list


def save_maxcut_instance_list(instance_list):
    """
    Save the list of instances withing the maxcut database

    Parameters
    ----------
    instance_list : InstanceList
        List of instances
    """
    storage_path = os.path.join(MAXCUT_DB_PATH, instance_list.group_name)

    if not os.path.exists(storage_path):
        os.mkdir(storage_path)
        for instance in instance_list:
            file_name = os.path.join(storage_path,
                                     f'{instance.id}_MaxcutInstance.txt')
            fo = open(file_name, "wb")
            nx.write_weighted_edgelist(instance.graph, fo)
    else:
        log_warning(f'Path {storage_path} already existing. Please remove the directory or use another group name')
