import argparse

def parse_args():

	parser = argparse.ArgumentParser("Run SaTScan")

	parser.add_argument(
		"--CaseFile",
		type=str,
		required=True,
		help="case data filename",
		dest="CaseFile",
	)

	parser.add_argument(
		"--ControlFile",
		type=str,
		required=False,
		help="control data filename",
		dest="ControlFile",
	)

	parser.add_argument(
		"--PrecisionCaseTimes",
		type=int,
		required=True,
		help="time precision (0=None, 1=Year, 2=Month, 3=Day, 4=Generic)",
		dest="PrecisionCaseTimes",
		choices=[0, 1, 2, 3, 4]
	)

	parser.add_argument(
		"--StartDate",
		type=str,
		required=True,
		help="study period start date (YYYY/MM/DD)",
		dest="StartDate",
	)

	parser.add_argument(
		"--EndDate",
		type=str,
		required=True,
		help="study period end date (YYYY/MM/DD)",
		dest="EndDate",
	)

	parser.add_argument(
		"--PopulationFile",
		type=str,
		required=False,
		help="population data filename",
		dest="PopulationFile",
	)

	parser.add_argument(
		"--CoordinatesFile",
		type=str,
		required=True,
		help="coordinate data filename",
		dest="CoordinatesFile",
	)

	parser.add_argument(
		"--CoordinatesType",
		type=int,
		required=True,
		help="coordinate type (0=Cartesian, 1=latitude/longitude)",
		dest="CoordinatesType",
		choices=[0, 1]
	)

	parser.add_argument(
		"--UseGridFile",
		type=str,
		required=False,
		help="use grid file? (y/n)",
		dest="UseGridFile",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--GridFile",
		type=str,
		required=False,
		help="grid data filename",
		dest="GridFile",
	)

	parser.add_argument(
		"--AnalysisType",
		type=int,
		required=True,
		help="analysis type (1=Purely Spatial, 2=Purely Temporal, 3=Retrospective Space-Time, 4=Prospective Space-Time, 5=Spatial Variation in Temporal Trends, 6=Prospective Purely Temporal, 7=Seasonal Temporal)",
		dest="AnalysisType",
		choices=[1, 2, 3, 4, 5, 6, 7]
	)

	parser.add_argument(
		"--ModelType",
		type=int,
		required=True,
		help="model type (0=Discrete Poisson, 1=Bernoulli, 2=Space-Time Permutation, 3=Ordinal, 4=Exponential, 5=Normal, 6=Continuous Poisson, 7=Multinomial)",
		dest="ModelType",
		choices=[0, 1, 2, 3, 4, 5, 6, 7]
	)

	parser.add_argument(
		"--ScanAreas",
		type=int,
		required=False,
		help="scan areas (1=High Rates(Poison,Bernoulli,STP); High Values(Ordinal,Normal); Short Survival(Exponential); Higher Trend(Poisson-SVTT), 2=Low Rates(Poison,Bernoulli,STP); Low Values(Ordinal,Normal); Long Survival(Exponential); Lower Trend(Poisson-SVTT), 3=Both Areas)",
		dest="ScanAreas",
		choices=[1, 2, 3]
	)

	parser.add_argument(
		"--TimeAggregationUnits",
		type=int,
		required=True,
		help="time aggregation units (0=None, 1=Year, 2=Month, 3=Day, 4=Generic)",
		dest="TimeAggregationUnits",
		choices=[0, 1, 2, 3, 4]
	)

	parser.add_argument(
		"--TimeAggregationLength",
		type=int,
		required=True,
		help="time aggregation length (Positive Integer)",
		dest="TimeAggregationLength",
	)

	parser.add_argument(
		"--ResultsFile",
		type=str,
		required=True,
		help="analysis main results output filename",
		dest="ResultsFile",
	)

	parser.add_argument(
		"--SaveSimLLRsASCII",
		type=str,
		required=False,
		help="output simulated log likelihoods ratios in ASCII format? (y/n)",
		dest="SaveSimLLRsASCII",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--IncludeRelativeRisksCensusAreasASCII",
		type=str,
		required=False,
		help="output risk estimates in ASCII format? (y/n)",
		dest="IncludeRelativeRisksCensusAreasASCII",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--CensusAreasReportedClustersASCII",
		type=str,
		required=False,
		help="output location information in ASCII format? (y/n)",
		dest="CensusAreasReportedClustersASCII",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--MostLikelyClusterEachCentroidASCII",
		type=str,
		required=False,
		help="output cluster information in ASCII format? (y/n)",
		dest="MostLikelyClusterEachCentroidASCII",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--MostLikelyClusterEachCentroidDBase",
		type=str,
		required=False,
		help="output cluster information in dBase format? (y/n)",
		dest="MostLikelyClusterEachCentroidDBase",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--CensusAreasReportedClustersDBase",
		type=str,
		required=False,
		help="output location information in dBase format? (y/n)",
		dest="CensusAreasReportedClustersDBase",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--IncludeRelativeRisksCensusAreasDBase",
		type=str,
		required=False,
		help="output risk estimates in dBase format? (y/n)",
		dest="IncludeRelativeRisksCensusAreasDBase",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--SaveSimLLRsDBase",
		type=str,
		required=False,
		help="output simulated log likelihoods ratios in dBase format? (y/n)",
		dest="SaveSimLLRsDBase",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--MostLikelyClusterCaseInfoEachCentroidASCII",
		type=str,
		required=False,
		help="output cluster case information in ASCII format? (y/n)",
		dest="MostLikelyClusterCaseInfoEachCentroidASCII",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--MostLikelyClusterCaseInfoEachCentroidDBase",
		type=str,
		required=False,
		help="output cluster case information in dBase format? (y/n)",
		dest="MostLikelyClusterCaseInfoEachCentroidDBase",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--OutputGoogleEarthKML",
		type=str,
		required=False,
		help="output Google Earth KML file (y/n)",
		dest="OutputGoogleEarthKML",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--OutputShapefiles",
		type=str,
		required=False,
		help="output shapefiles (y/n)",
		dest="OutputShapefiles",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--OutputCartesianGraph",
		type=str,
		required=False,
		help="output cartesian graph file (y/n)",
		dest="OutputCartesianGraph",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--Polygons1",
		type=int,
		required=False,
		help="polygon inequalities (comma separated decimal values)",
		dest="Polygons1",
	)

	parser.add_argument(
		"--MultipleDataSetsPurposeType",
		type=int,
		required=False,
		help="multiple data sets purpose type (0=Multivariate, 1=Adjustment)",
		dest="MultipleDataSetsPurposeType",
		choices=[0, 1]
	)

	parser.add_argument(
		"--StudyPeriodCheckType",
		type=int,
		required=False,
		help="study period data check (0=Strict Bounds, 1=Relaxed Bounds)",
		dest="StudyPeriodCheckType",
		choices=[0, 1]
	)

	parser.add_argument(
		"--GeographicalCoordinatesCheckType",
		type=int,
		required=False,
		help="geographical coordinates data check (0=Strict Coordinates, 1=Relaxed Coordinates)",
		dest="GeographicalCoordinatesCheckType",
		choices=[0, 1]
	)

	parser.add_argument(
		"--UseNeighborsFile",
		type=str,
		required=False,
		help="use neighbors file (y/n)",
		dest="UseNeighborsFile",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--NeighborsFilename",
		type=str,
		required=False,
		help="neighbors file",
		dest="NeighborsFilename",
	)

	parser.add_argument(
		"--UseMetaLocationsFile",
		type=str,
		required=False,
		help="use meta locations file (y/n)",
		dest="UseMetaLocationsFile",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--MetaLocationsFilename",
		type=str,
		required=False,
		help="meta locations file",
		dest="MetaLocationsFilename",
	)

	parser.add_argument(
		"--MultipleCoordinatesType",
		type=int,
		required=False,
		help="multiple coordinates type (0=OnePerLocation, 1=AtLeastOneLocation, 2=AllLocations)",
		dest="MultipleCoordinatesType",
		choices=[0, 1, 2]
	)

	parser.add_argument(
		"--MaxCirclePopulationFile",
		type=str,
		required=False,
		help="maximum circle size filename",
		dest="MaxCirclePopulationFile",
	)

	parser.add_argument(
		"--IncludePurelyTemporal",
		type=str,
		required=False,
		help="include purely temporal clusters? (y/n)",
		dest="IncludePurelyTemporal",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--SpatialWindowShapeType",
		type=int,
		required=False,
		help="window shape (0=Circular, 1=Elliptic)",
		dest="SpatialWindowShapeType",
		choices=[0, 1]
	)

	parser.add_argument(
		"--NonCompactnessPenalty",
		type=int,
		required=False,
		help="elliptic non-compactness penalty (0=NoPenalty, 1=MediumPenalty, 2=StrongPenalty)",
		dest="NonCompactnessPenalty",
		choices=[0, 1, 2]
	)

	parser.add_argument(
		"--MaxSpatialSizeInPopulationAtRisk",
		type=int,
		required=False,
		help="maximum spatial size in population at risk (<=50)",
		dest="MaxSpatialSizeInPopulationAtRisk",
	)

	parser.add_argument(
		"--MaxSpatialSizeInMaxCirclePopulationFile",
		type=int,
		required=False,
		help="maximum spatial size in max circle population file (<=50)",
		dest="MaxSpatialSizeInMaxCirclePopulationFile",
	)

	parser.add_argument(
		"--MaxSpatialSizeInDistanceFromCenter",
		type=str,
		required=False,
		help="maximum spatial size in distance from center (positive integer)",
		dest="MaxSpatialSizeInDistanceFromCenter",
	)

	parser.add_argument(
		"--UseMaxCirclePopulationFileOption",
		type=str,
		required=False,
		help="restrict maximum spatial size - max circle file? (y/n)",
		dest="UseMaxCirclePopulationFileOption",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--UseDistanceFromCenterOption",
		type=str,
		required=False,
		help="restrict maximum spatial size - distance? (y/n)",
		dest="UseDistanceFromCenterOption",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--IsotonicScan",
		type=int,
		required=False,
		help="isotonic scan (0=Standard, 1=Monotone)",
		dest="IsotonicScan",
		choices=[0, 1]
	)

	parser.add_argument(
		"--MaxTemporalSizeInterpretation",
		type=int,
		required=False,
		help="how max temporal size should be interpretted (0=Percentage, 1=Time)",
		dest="MaxTemporalSizeInterpretation",
		choices=[0, 1]
	)

	parser.add_argument(
		"--MaxTemporalSize",
		type=int,
		required=False,
		help="maximum temporal cluster size (<=90)",
		dest="MaxTemporalSize",
	)

	parser.add_argument(
		"--IncludePurelySpatial",
		type=str,
		required=False,
		help="include purely spatial clusters? (y/n)",
		dest="IncludePurelySpatial",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--IncludeClusters",
		type=int,
		required=False,
		help="temporal clusters evaluated (0=All, 1=Alive, 2=Flexible Window)",
		dest="IncludeClusters",
		choices=[0, 1, 2]
	)

	parser.add_argument(
		"--IntervalStartRange",
		type=int,
		required=False,
		help="flexible temporal window start range (YYYY/MM/DD,YYYY/MM/DD)",
		dest="IntervalStartRange",
	)

	parser.add_argument(
		"--IntervalEndRange",
		type=int,
		required=False,
		help="flexible temporal window end range (YYYY/MM/DD,YYYY/MM/DD)",
		dest="IntervalEndRange",
	)

	parser.add_argument(
		"--MinimumTemporalClusterSize",
		type=int,
		required=False,
		help="minimum temporal cluster size (in time aggregation units)",
		dest="MinimumTemporalClusterSize",
	)

	parser.add_argument(
		"--MinimumCasesInLowRateClusters",
		type=str,
		required=False,
		help="minimum cases in low rate clusters (positive integer)",
		dest="MinimumCasesInLowRateClusters",
	)

	parser.add_argument(
		"--MinimumCasesInHighRateClusters",
		type=str,
		required=False,
		help="minimum cases in high clusters (positive integer)",
		dest="MinimumCasesInHighRateClusters",
	)

	parser.add_argument(
		"--RiskLimitHighClusters",
		type=str,
		required=False,
		help="risk limit high clusters (y/n)",
		dest="RiskLimitHighClusters",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--RiskThresholdHighClusters",
		type=int,
		required=False,
		help="risk threshold high clusters (1.0 or greater)",
		dest="RiskThresholdHighClusters",
	)

	parser.add_argument(
		"--RiskLimitLowClusters",
		type=str,
		required=False,
		help="risk limit low clusters (y/n)",
		dest="RiskLimitLowClusters",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--RiskThresholdLowClusters",
		type=int,
		required=False,
		help="risk threshold low clusters (0.000 - 1.000)",
		dest="RiskThresholdLowClusters",
	)

	parser.add_argument(
		"--TimeTrendAdjustmentType",
		type=int,
		required=False,
		help="time trend adjustment type (0=None, 1=Nonparametric, 2=LogLinearPercentage, 3=CalculatedLogLinearPercentage, 4=TimeStratifiedRandomization, 5=CalculatedQuadraticPercentage)",
		dest="TimeTrendAdjustmentType",
		choices=[0, 1, 2, 3, 4, 5]
	)

	parser.add_argument(
		"--TimeTrendPercentage",
		type=int,
		required=False,
		help="time trend adjustment percentage (>-100)",
		dest="TimeTrendPercentage",
	)

	parser.add_argument(
		"--SpatialAdjustmentType",
		type=int,
		required=False,
		help="spatial adjustments type (0=No Spatial Adjustment, 1=Spatially Stratified Randomization)",
		dest="SpatialAdjustmentType",
		choices=[0, 1]
	)

	parser.add_argument(
		"--UseAdjustmentsByRRFile",
		type=str,
		required=False,
		help="use adjustments by known relative risks file? (y/n)",
		dest="UseAdjustmentsByRRFile",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--AdjustmentsByKnownRelativeRisksFilename",
		type=int,
		required=False,
		help="adjustments by known relative risks file name (with HA Randomization=1)",
		dest="AdjustmentsByKnownRelativeRisksFilename",
	)

	parser.add_argument(
		"--TimeTrendType",
		type=int,
		required=False,
		help="time trend type - SVTT only (Linear=0, Quadratic=1)",
		dest="TimeTrendType",
	)

	parser.add_argument(
		"--AdjustForWeeklyTrends",
		type=str,
		required=False,
		help="adjust for weekly trends, nonparametric",
		dest="AdjustForWeeklyTrends",
	)

	parser.add_argument(
		"--CriticalValue",
		type=str,
		required=False,
		help="report critical values for .01 and .05? (y/n)",
		dest="CriticalValue",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--ReportClusterRank",
		type=str,
		required=False,
		help="report cluster rank (y/n)",
		dest="ReportClusterRank",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--PrintAsciiColumnHeaders",
		type=str,
		required=False,
		help="print ascii headers in output files (y/n)",
		dest="PrintAsciiColumnHeaders",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--ResultsTitle",
		type=str,
		required=False,
		help="user-defined title for results file",
		dest="ResultsTitle",
	)

	parser.add_argument(
		"--EarlySimulationTermination",
		type=str,
		required=False,
		help="terminate simulations early for large p-values? (y/n)",
		dest="EarlySimulationTermination",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--ProspectiveStartDate",
		type=str,
		required=False,
		help="prospective surveillance start date (YYYY/MM/DD)",
		dest="ProspectiveStartDate",
	)

	parser.add_argument(
		"--AdjustForEarlierAnalyses",
		type=str,
		required=False,
		help="adjust for earlier analyses(prospective analyses only)? (y/n)",
		dest="AdjustForEarlierAnalyses",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--IterativeScan",
		type=str,
		required=False,
		help="perform iterative scans? (y/n)",
		dest="IterativeScan",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--IterativeScanMaxIterations",
		type=int,
		required=False,
		help="maximum iterations for iterative scan (0-32000)",
		dest="IterativeScanMaxIterations",
	)

	parser.add_argument(
		"--IterativeScanMaxPValue",
		type=int,
		required=False,
		help="max p-value for iterative scan before cutoff (0.000-1.000)",
		dest="IterativeScanMaxPValue",
	)

	parser.add_argument(
		"--MonteCarloReps",
		type=int,
		required=False,
		help="Monte Carlo replications (0, 9, 999, n999)",
		dest="MonteCarloReps",
	)

	parser.add_argument(
		"--EarlyTerminationThreshold",
		type=str,
		required=False,
		help="early termination threshold",
		dest="EarlyTerminationThreshold",
	)

	parser.add_argument(
		"--PValueReportType",
		type=int,
		required=False,
		help="p-value reporting type (Default p-value=0, Standard Monte Carlo=1, Early Termination=2, Gumbel p-value=3)",
		dest="PValueReportType",
	)

	parser.add_argument(
		"--ReportGumbel",
		type=str,
		required=False,
		help="report Gumbel p-values (y/n)",
		dest="ReportGumbel",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--CalculateOliveira",
		type=str,
		required=False,
		help="calculate Oliveira's F",
		dest="CalculateOliveira",
	)

	parser.add_argument(
		"--NumBootstrapReplications",
		type=int,
		required=False,
		help="number of bootstrap replications for Oliveira calculation (minimum=100, multiple of 100)",
		dest="NumBootstrapReplications",
	)

	parser.add_argument(
		"--OliveiraPvalueCutoff",
		type=int,
		required=False,
		help="p-value cutoff for cluster's in Oliveira calculation (0.000-1.000)",
		dest="OliveiraPvalueCutoff",
	)

	parser.add_argument(
		"--PerformPowerEvaluation",
		type=str,
		required=False,
		help="perform power evaluation - Poisson only (y/n)",
		dest="PerformPowerEvaluation",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--PowerEvaluationTotalCases",
		type=str,
		required=False,
		help="total cases in power evaluation",
		dest="PowerEvaluationTotalCases",
	)

	parser.add_argument(
		"--CriticalValueType",
		type=int,
		required=False,
		help="critical value type (0=Monte Carlo, 1=Gumbel, 2=User Specified Values)",
		dest="CriticalValueType",
		choices=[0, 1, 2]
	)

	parser.add_argument(
		"--PowerEstimationType",
		type=int,
		required=False,
		help="power estimation type (0=Monte Carlo, 1=Gumbel)",
		dest="PowerEstimationType",
		choices=[0, 1]
	)

	parser.add_argument(
		"--AlternativeHypothesisFilename",
		type=str,
		required=False,
		help="power evaluation alternative hypothesis filename",
		dest="AlternativeHypothesisFilename",
	)

	parser.add_argument(
		"--NumberPowerReplications",
		type=str,
		required=False,
		help="number of replications in power step",
		dest="NumberPowerReplications",
	)

	parser.add_argument(
		"--PowerEvaluationsSimulationMethod",
		type=int,
		required=False,
		help="power evaluation simulation method for power step (0=Null Randomization, 1=N/A, 2=File Import)",
		dest="PowerEvaluationsSimulationMethod",
		choices=[0, 1, 2]
	)

	parser.add_argument(
		"--PowerEvaluationsSimulationSourceFilename",
		type=str,
		required=False,
		help="power evaluation simulation data source filename",
		dest="PowerEvaluationsSimulationSourceFilename",
	)

	parser.add_argument(
		"--PowerEvaluationsMethod",
		type=int,
		required=False,
		help="power evaluation method (0=Analysis And Power Evaluation Together, 1=Only Power Evaluation With Case File, 2=Only Power Evaluation With Defined Total Cases)",
		dest="PowerEvaluationsMethod",
		choices=[0, 1, 2]
	)

	parser.add_argument(
		"--CriticalValue05",
		type=int,
		required=False,
		help="power evaluation critical value .05 (> 0)",
		dest="CriticalValue05",
	)

	parser.add_argument(
		"--CriticalValue01",
		type=int,
		required=False,
		help="power evaluation critical value .001 (> 0)",
		dest="CriticalValue01",
	)

	parser.add_argument(
		"--CriticalValue001",
		type=int,
		required=False,
		help="power evaluation critical value .001 (> 0)",
		dest="CriticalValue001",
	)

	parser.add_argument(
		"--ReportPowerEvaluationSimulationData",
		type=str,
		required=False,
		help="report power evaluation randomization data from power step (y/n)",
		dest="ReportPowerEvaluationSimulationData",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--PowerEvaluationsSimulationOutputFilename",
		type=str,
		required=False,
		help="power evaluation simulation data output filename",
		dest="PowerEvaluationsSimulationOutputFilename",
	)

	parser.add_argument(
		"--OutputTemporalGraphHTML",
		type=str,
		required=False,
		help="output temporal graph HTML file (y/n)",
		dest="OutputTemporalGraphHTML",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--TemporalGraphReportType",
		type=int,
		required=False,
		help="temporal graph cluster reporting type (0=Only most likely cluster, 1=X most likely clusters, 2=Only significant clusters)",
		dest="TemporalGraphReportType",
		choices=[0, 1, 2]
	)

	parser.add_argument(
		"--TemporalGraphMostMLC",
		type=str,
		required=False,
		help="number of most likely clusters to report in temporal graph (positive integer)",
		dest="TemporalGraphMostMLC",
	)

	parser.add_argument(
		"--TemporalGraphSignificanceCutoff",
		type=int,
		required=False,
		help="significant clusters p-value cutoff to report in temporal graph (0.000-1.000)",
		dest="TemporalGraphSignificanceCutoff",
	)

	parser.add_argument(
		"--IncludeClusterLocationsKML",
		type=str,
		required=False,
		help="whether to include cluster locations kml output (y/n)",
		dest="IncludeClusterLocationsKML",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--ThresholdLocationsSeparateKML",
		type=str,
		required=False,
		help="threshold for generating separate kml files for cluster locations (positive integer)",
		dest="ThresholdLocationsSeparateKML",
	)

	parser.add_argument(
		"--CompressKMLtoKMZ",
		type=str,
		required=False,
		help="create compressed KMZ file instead of KML file (y/n)",
		dest="CompressKMLtoKMZ",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--LaunchMapViewer",
		type=str,
		required=False,
		help="automatically launch map viewer - gui only (y/n)",
		dest="LaunchMapViewer",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--ReportHierarchicalClusters",
		type=str,
		required=False,
		help="report hierarchical clusters (y/n)",
		dest="ReportHierarchicalClusters",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--ReportGiniClusters",
		type=str,
		required=False,
		help="report gini clusters (y/n)",
		dest="ReportGiniClusters",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--SpatialMaxima",
		type=int,
		required=False,
		help="spatial window maxima stops (comma separated decimal values[<=50] )",
		dest="SpatialMaxima",
	)

	parser.add_argument(
		"--GiniIndexClusterReportingType",
		type=int,
		required=False,
		help="gini index cluster reporting type (0=optimal index only, 1=all values)",
		dest="GiniIndexClusterReportingType",
		choices=[0, 1]
	)

	parser.add_argument(
		"--GiniIndexClustersPValueCutOff",
		type=int,
		required=False,
		help="max p-value for clusters used in calculation of index based coefficients (0.000-1.000)",
		dest="GiniIndexClustersPValueCutOff",
	)

	parser.add_argument(
		"--ReportGiniIndexCoefficents",
		type=str,
		required=False,
		help="report gini index coefficents to results file (y/n)",
		dest="ReportGiniIndexCoefficents",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--CriteriaForReportingSecondaryClusters",
		type=int,
		required=False,
		help="criteria for reporting secondary clusters(0=NoGeoOverlap, 1=NoCentersInOther, 2=NoCentersInMostLikely,  3=NoCentersInLessLikely, 4=NoPairsCentersEachOther, 5=NoRestrictions)",
		dest="CriteriaForReportingSecondaryClusters",
		choices=[0, 1, 2, 3, 4, 5]
	)

	parser.add_argument(
		"--UseReportOnlySmallerClusters",
		type=str,
		required=False,
		help="restrict reported clusters to maximum geographical cluster size? (y/n)",
		dest="UseReportOnlySmallerClusters",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--MaxSpatialSizeInPopulationAtRisk_Reported",
		type=int,
		required=False,
		help="maximum reported spatial size in population at risk (<=50)",
		dest="MaxSpatialSizeInPopulationAtRisk_Reported",
	)

	parser.add_argument(
		"--UseMaxCirclePopulationFileOption_Reported",
		type=str,
		required=False,
		help="restrict maximum reported spatial size - max circle file? (y/n)",
		dest="UseMaxCirclePopulationFileOption_Reported",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--MaxSizeInMaxCirclePopulationFile_Reported",
		type=int,
		required=False,
		help="maximum reported spatial size in max circle population file (<=50)",
		dest="MaxSizeInMaxCirclePopulationFile_Reported",
	)

	parser.add_argument(
		"--UseDistanceFromCenterOption_Reported",
		type=str,
		required=False,
		help="restrict maximum reported spatial size - distance? (y/n)",
		dest="UseDistanceFromCenterOption_Reported",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--MaxSpatialSizeInDistanceFromCenter_Reported",
		type=str,
		required=False,
		help="maximum reported spatial size in distance from center (positive integer)",
		dest="MaxSpatialSizeInDistanceFromCenter_Reported",
	)

	parser.add_argument(
		"--OutputGoogleMaps",
		type=str,
		required=False,
		help="generate Google Maps output (y/n)",
		dest="OutputGoogleMaps",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--EllipseShapes",
		type=int,
		required=False,
		help="elliptic shapes - one value for each ellipse (comma separated decimal values)",
		dest="EllipseShapes",
	)

	parser.add_argument(
		"--EllipseAngles",
		type=int,
		required=False,
		help="elliptic angles - one value for each ellipse (comma separated integer values)",
		dest="EllipseAngles",
	)

	parser.add_argument(
		"--SimulatedDataMethodType",
		type=int,
		required=False,
		help="simulation methods (0=Null Randomization, 1=N/A, 2=File Import)",
		dest="SimulatedDataMethodType",
		choices=[0, 1, 2]
	)

	parser.add_argument(
		"--SimulatedDataInputFilename",
		type=int,
		required=False,
		help="simulation data input file name (with File Import=2)",
		dest="SimulatedDataInputFilename",
	)

	parser.add_argument(
		"--PrintSimulatedDataToFile",
		type=str,
		required=False,
		help="print simulation data to file? (y/n)",
		dest="PrintSimulatedDataToFile",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--SimulatedDataOutputFilename",
		type=str,
		required=False,
		help="simulation data output filename",
		dest="SimulatedDataOutputFilename",
	)

	parser.add_argument(
		"--RandomSeed",
		type=int,
		required=False,
		help="randomization seed (0 < Seed < 2147483647)",
		dest="RandomSeed",
	)

	parser.add_argument(
		"--ExecutionType",
		type=int,
		required=False,
		help="analysis execution method  (0=Automatic, 1=Successively, 2=Centrically)",
		dest="ExecutionType",
		choices=[0, 1, 2]
	)

	parser.add_argument(
		"--NumberParallelProcesses",
		type=int,
		required=False,
		help="number of parallel processes to execute (0=All Processors, x=At Most X Processors)",
		dest="NumberParallelProcesses",
		choices=[0]
	)

	parser.add_argument(
		"--LogRunToHistoryFile",
		type=str,
		required=False,
		help="log analysis run to history file? (y/n)",
		dest="LogRunToHistoryFile",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--SuppressWarnings",
		type=str,
		required=False,
		help="suppressing warnings? (y/n)",
		dest="SuppressWarnings",
		choices=['y', 'n']
	)

	parser.add_argument(
		"--RandomlyGenerateSeed",
		type=str,
		required=False,
		help="randomly generate seed (y/n)",
		dest="RandomlyGenerateSeed",
		choices=['y', 'n']
	)

	return parser.parse_args()
if __name__ == "__main__":
	arg = parse_args()
