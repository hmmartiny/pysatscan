# Running SaTScan in Python [![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
A quick wrapper for running SaTScan (https://www.satscan.org/) in a Python script or Notebook.

## How to run:
I did try to replicate the [NYC fever data example](https://www.satscan.org/rsatscan/rsatscan.html) that is also shown in the [`rsatscan`](https://cran.r-project.org/web/packages/rsatscan/index.html) package in R.

### Interactive session
The Jupyter Notebook named [Tutorial](Tutorial.ipynb) show how to use the PySaTScan in an interactive Python session.

### Terminal
The script `pysatscan/run.py` provides the terminal application, although it might not be that useful as it's simply just the same as running the satscan directly in the terminal.. But it's there!

```python
python pysatscan/run.py --CaseFile sample_data/NYCfever.cas --PrecisionCaseTimes 3 --StartDate 2001/11/1 --EndDate 2001/11/24 --CoordinatesFile sample_data/NYCfever.geo --TimeAggregationUnits 3 --AnalysisType 4 --ModelType 2 --UseDistanceFromCenterOption y --MaxSpatialSizeInDistanceFromCenter 3 --NonCompactnessPenalty 0 --MaxTemporalSizeInterpretation 1 --MaxTemporalSize 7 --ProspectiveStartDate 2001/11/24 --ReportGiniClusters n --LogRunToHistoryFile n  --CoordinatesType 1 --TimeAggregationLength 1 --ResultsFile NYCfever.res
```
