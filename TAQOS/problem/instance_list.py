#!/usr/bin python3.8.10
# -*- coding: utf-8 -*-
"""
@authors Valentin Gilbert <valentin.gilbert@cea.fr>

Description:
   Generic class specifying list of problem instances
=========

"""

# third party import

# local import


class InstanceList(list):
    def __init__(self, group_name):
        """
        Build an instance list

        Parameters
        ----------
        group_name : string
            path storing the list of instances
        """
        super().__init__()
        self.group_name = group_name

    def get_coverage(self, epsilon):
        """
        Compute the coverage rate of the instance set

        Parameters
        ----------
        epsilon : float
            coverage factor

        Returns
        -------
            dict<string, float> coverage value for each metric
        """
        pass
