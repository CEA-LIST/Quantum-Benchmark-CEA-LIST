#!/usr/bin python3.8.10
# -*- coding: utf-8 -*-
"""
@authors Valentin Gilbert <valentin.gilbert@cea.fr>

Description:
   Generic class specifying problem instance
=========

"""

# third party import

# local import


class Instance:
    def __init__(self, id):
        """
        Create an instance

        Parameters
        ----------
        id : int
            id of the instance
        """
        self.id = id

    def get_metrics(self):
        """
        Compute the list of metrics associated to the instance

        Returns
        -------
            dict<string, float>: metric name associated to its value
        """
        pass

    def to_ising(self):
        """
        Convert the instance to an ising model

        Returns
        -------
            auto-coupling and coupling bias
        """
        pass

    def to_mqlib_instance(self):
        """
        Convert the instance to an MQLib instance

        Returns
        -------
            MQLib instance
        """
        pass
