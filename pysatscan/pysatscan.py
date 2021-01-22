#!/usr/bin/python3
import re

"""
Python interface for running SaTScan analysis
"""

__author__ = 'Hannah-Marie Martiny'
__maintainer__ = 'Hannah-Marie Martiny'
__email__ = 'hanmar@food.dtu.dk'

import subprocess

class PySaTScan:
    """
    Python Interface for Running SaTScan

    Parameters
    ----------
    executable : str, optional
        Path or alias for running satscan in terminal, by default 'satscan'
    """

    def __init__(self, executable='satscan'):
        self.executable = executable

    def set_setting(self, name, value):
        """Set a value for one of the parameters

        Parameters
        ----------
        name : str
            parameter name
        value : str, int or float
            value to be set for parameter
        """

        if isinstance(value, list):
            if name == 'Polygons':
                for i, v in enumerate(value):
                    vname = 'Polygons' + str(i+1)
                    setattr(self, vname, v)
        else:
            setattr(self, name, value)

    def list_settings(self):
        """Print a list of all settings set in current PySaTScan session"""

        for k, v in self.__dict__.items():
            print('{}: {}'.format(k,v))

    def run(self, verbose=True, **kwargs):
        """Run the SaTScan command

        Parameters
        ----------
        verbose : bool, optional
            [description], by default True

        Returns
        -------
        [type]
            [description]
        """

        # build cmd
        cmd = [self.executable]

        # add additional settings to cmd
        for k, v in self.__dict__.items():
            if k == 'executable':
                continue
            cmd += ['--{}'.format(k), str(v)]
        
        cmd = " ".join(cmd)
        if verbose:
            print(cmd)

        p = subprocess.run(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        if verbose:
            if p.returncode == 0:
                print(p.stdout.decode())
            else:
                print(p.stderr.decode())

        return p
    
    def summary(self, alpha=0.05):
        """Print the summary of a SaTScan run"""

        if not hasattr(self, 'ResultsFile'):
            raise AttributeError("There are no ResultsFile saved as an attribute, suggesting SaTScan has not run successfully.")

        # read
        with open(self.ResultsFile, 'r') as f:
            lines = [l for l in f.readlines()]
        
        # just preamble
        print("".join(lines[6:13]))

        # data summary
        i = 15
        while i < len(lines):
            print(lines[i].strip())
            if len(lines[i].strip()) == 0:
                break
            i += 1

        # get number of clusters
        p_cluster = re.compile(r'^\d\.Location\sIDs\sincluded.:.+$')
        p_pval = re.compile(r'^P-value\.+:\s<?\s?(.+)$')
        i += 2
        n_clusters = 0
        n_clusters_sig = 0
        while i < len(lines):
            m_cluster = p_cluster.match(lines[i].strip())
            if m_cluster:
                n_clusters += 1
            
            m_pval = p_pval.match(lines[i].strip())
            if m_pval:
                pval = p_pval.findall(lines[i].strip())[0]
                pval = float(pval)

                if pval < alpha:
                    n_clusters_sig += 1

            
            if lines[i].count('-') > 10:
                break
            i += 1
        
        print("There were {} clusters identified.".format(n_clusters))
        print("There were {} clusters with p < {}".format(n_clusters_sig, alpha))