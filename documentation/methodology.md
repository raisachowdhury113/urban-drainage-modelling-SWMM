# Methodology

## Model framework
The supplied model was configured in EPA SWMM 5.2.4. The report identifies CMS flow units, Horton infiltration and Dynamic Wave routing. The simulation period is 18 August 2026, 00:00 to 06:00.

## Catchment representation
The INP file contains 35 subcatchments. Each subcatchment is linked to rain gauge R1 and an outlet node. Subcatchment parameters are provided in `../data/subcatchment_parameters.csv`.

## Drainage network
The supplied model contains 45 junctions, 40 conduits, one storage unit, one pump and one outfall. Inventories are extracted into the data folder. The network figure uses native coordinates and conduit endpoint definitions in the INP.

## Rainfall
Rain gauge R1 uses time series TS1 with a one-hour recording interval. The report states total precipitation of 142.0 mm. Time-series ordinates are reproduced in `rain_gauge_timeseries_input.csv`. Confirm the intended rainfall hyetograph and rain-gauge interpretation before design conclusions.

## Infiltration and routing
The model specifies Horton infiltration and Dynamic Wave routing. The report gives a 20-second routing time step, 5-minute wet-weather time step and 15-minute report time step.

## LID
The model defines `LID_GR` as type `GR` and applies it to S14, S1, S30 and S23. Layer and usage parameters remain in the original INP.

## Output review
The supplied RPT was used to extract continuity indicators, flooding summaries and conduit flow summaries. These are descriptive outputs from the supplied simulation; they are not independently calibrated or validated.
