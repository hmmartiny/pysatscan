#!/usr/bin/python3

"""
Run SaTScan analysis

this works:
satscan --CaseFile sample_data/NYCfever.cas --PrecisionCaseTimes 3 --StartDate 2001/11/1 --EndDate 2001/11/24 --CoordinatesFile sample_data/NYCfever.geo --CoordinatesType 1 --AnalysisType 4 --ModelType 2 --TimeAggregationUnits 3 --MaxTemporalSizeInterpretation 1 --MaxTemporalSize 7 --UseDistanceFromCenterOption y --MaxSpatialSizeInDistanceFromCenter 3 --NonCompactnessPenalty 0 --ProspectiveStartDate 2001/11/24 --ReportGiniClusters n --LogRunToHistoryFile n --ResultsFile NYCfever.res --TimeAggregationLength 1

"""

__author__ = 'Hannah-Marie Martiny'
__maintainer__ = 'Hannah-Marie Martiny'
__email__ = 'hanmar@food.dtu.dk'

import argparse
from pysatscan import PySaTScan
from arguments import parse_args

if __name__ == "__main__":
    args = parse_args()

    # initalize wrapper
    pysatscan = PySaTScan()

    # set arguments
    for arg in vars(args):
        if getattr(args, arg) is None:
            continue
        
        pysatscan.set_setting(
            name=arg,
            value=getattr(args, arg)
        )
    
    pysatscan.list_settings()
    p = pysatscan.run()

    print(p.stdout.decode())
    print(p.stderr.decode())