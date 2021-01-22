# Running SaTScan in Python [![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
A quick wrapper for running SaTScan (https://www.satscan.org/) in a Python script or Notebook.

## Installation
1. Install the non-graphical version of SaTScan from [here](https://www.satscan.org/download_satscan.html).
2. Add
3. Install pysatscan from test-pypi: 
```
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps pysatscan
```

## Usage
I did try to replicate the [NYC fever data example](https://www.satscan.org/rsatscan/rsatscan.html) that is also shown in the [`rsatscan`](https://cran.r-project.org/web/packages/rsatscan/index.html) package in R.

### Script
The simplest way to use:
```python
from pysatscan.pysatacan import PySaTScan
satscan = PySaTScan()

# set settings
satscan.set_setting('CaseFile', 'sample_data/NYCfever.cas')
satscan.set_setting('PrecisionCaseTimes', 3)
satscan.set_setting('StartDate', '2001/11/1')
satscan.set_setting('EndDate', '2001/11/24')
satscan.set_setting('CoordinatesFile', 'sample_data/NYCfever.geo')
satscan.set_setting('CoordinatesType', 1)
satscan.set_setting('AnalysisType', 4)
satscan.set_setting('ModelType', 2)
satscan.set_setting('TimeAggregationUnits', 3)
satscan.set_setting('TimeAggregationLength', 1)
satscan.set_setting('UseDistanceFromCenterOption', 'y')
satscan.set_setting('MaxSpatialSizeInDistanceFromCenter', 3)
satscan.set_setting('NonCompactnessPenalty', 0)
satscan.set_setting('MaxTemporalSizeInterpretation', 1)
satscan.set_setting('MaxTemporalSize', 7)
satscan.set_setting('ProspectiveStartDate', '2001/11/24')
satscan.set_setting('ReportGiniClusters', 'n')
satscan.set_setting('LogRunToHistoryFile', 'n')
satscan.set_setting('ResultsFile', 'NYCfever.res')
satscan.set_setting('OutputShapefiles', 'y')

# List settings (Uncomment the line below)
# satscan.list_settings()

# run satscan
p = satscan.run(verbose=False)

# get summary
satscan.summary()
```

The Jupyter Notebook named Tutorial.ipynb show how to use the PySaTScan in an interactive Python session and other functions included in the package.

### Terminal
The script `pysatscan/run.py` provides the terminal application, although it might not be that useful as it's simply just the same as running the satscan directly in the terminal.. But it's there!

```python
python pysatscan/run.py --CaseFile sample_data/NYCfever.cas --PrecisionCaseTimes 3 --StartDate 2001/11/1 --EndDate 2001/11/24 --CoordinatesFile sample_data/NYCfever.geo --TimeAggregationUnits 3 --AnalysisType 4 --ModelType 2 --UseDistanceFromCenterOption y --MaxSpatialSizeInDistanceFromCenter 3 --NonCompactnessPenalty 0 --MaxTemporalSizeInterpretation 1 --MaxTemporalSize 7 --ProspectiveStartDate 2001/11/24 --ReportGiniClusters n --LogRunToHistoryFile n  --CoordinatesType 1 --TimeAggregationLength 1 --ResultsFile NYCfever.res
```
