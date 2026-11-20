# Urban Stormwater Drainage Modelling and Green Roof LID Assessment
### Green Road, Dhaka, Bangladesh

**Software:** EPA SWMM 5.2.4  
**Model approach:** Rainfall–runoff simulation with Dynamic Wave routing  
**Focus:** Urban drainage representation, hydraulic response and Green Roof Low Impact Development (LID)

---

## Project overview

I developed an EPA SWMM model to represent an urban stormwater drainage system for a study catchment identified in the project materials as Green Road, Dhaka, Bangladesh. The model brings together subcatchments, junctions, conduits, a storage unit, a pump and an outfall to examine the response of the represented drainage system to a time-varying rainfall input.

I also configured Green Roof LID controls in four subcatchments. This provides a basis for examining distributed stormwater management within an urban catchment.

The repository contains the original model input and its matching simulation report/output, extracted model inventories, baseline performance summaries, and figures generated from the supplied model data.

> **Scope note:** This is an academic modelling project. The supplied files do not establish field calibration, independent validation, surveyed geospatial positioning, or a construction-ready design. Model coordinates are retained in their native SWMM coordinate system and should not be interpreted as geographic coordinates.

## Model at a glance

| Item | Configuration |
|---|---:|
| Subcatchments | 35 |
| Junctions | 45 |
| Conduits | 40 |
| Storage units | 1 |
| Pumps | 1 |
| Outfalls | 1 |
| LID usage entries | 4 |
| Flow units | CMS |
| Infiltration method | Horton |
| Routing method | Dynamic Wave |
| Simulation period | 18 August 2026, 00:00–06:00 |
| Report time step | 15 minutes |
| Wet-weather time step | 5 minutes |
| Routing time step | 20 seconds |

## Design rainfall input

The model uses rain gauge `R1`, connected to time series `TS1`. The supplied report records total precipitation of **142.0 mm**. The time-series ordinates are available in `data/rain_gauge_timeseries_input.csv`; the figure in `figures/` visualises the input ordinates as stored in the INP file.

## LID configuration

The input file defines a Green Roof control (`LID_GR`, type `GR`) and assigns it to four subcatchments: **S14, S1, S30 and S23**. The LID usage and layer parameters are included in the original INP and extracted CSV inventory.

The report records the following LID performance values for each of the four listed subcatchments:

| Reported LID metric | Value |
|---|---:|
| Total inflow | 142.00 mm |
| Drain outflow | 115.31 mm |
| Initial storage | 12.00 mm |
| Final storage | 39.06 mm |
| LID continuity error | -0.24% |

These are SWMM-reported LID-unit results. They should not be interpreted as catchment-wide runoff reductions without additional area-weighted analysis and a comparable baseline scenario.

## Baseline simulation results

The matching report (`results/baseline_simulation_report.rpt`) records:

| Indicator | Reported result |
|---|---:|
| Total precipitation | 142.000 mm |
| Surface runoff | 130.574 mm |
| Infiltration loss | 1.226 mm |
| Runoff continuity error | -0.346% |
| Wet-weather inflow | 19.431 million litres |
| Flooding loss | 17.537 million litres |
| Flow-routing continuity error | +0.215% |
| Nonconverging routing steps | 6.69% |

The report lists node flooding at J2, J3, J7, J11, J29, J45, J22 and J39. The extracted values are in `data/node_flooding_summary_baseline.csv`.

I treat these as baseline model outputs rather than as evidence that the drainage system is adequate. Continuity error describes water-balance closure; it does not by itself establish hydraulic performance or design suitability.

## Network topology

`figures/swmm_network_topology.png` is generated from the node coordinates and conduit endpoints stored in the supplied INP file. The axes are labelled as model coordinates because the INP does not provide a verified geographic coordinate reference system.

## Repository contents

```text
.
├── README.md
├── model/
├── results/
├── data/
├── figures/
├── documentation/
└── scripts/
```

## Reproducibility

1. Install EPA SWMM 5.2 or a compatible later version.
2. Open `model/green_road_original.inp`.
3. Review the model configuration and run the simulation.
4. Compare the generated report with `results/baseline_simulation_report.rpt`.

The supplied `.out` file is the binary output from the same simulation as the supplied INP and RPT, according to the project file history. Re-running in a different SWMM build or environment may produce small differences.

## Skills demonstrated

- Urban stormwater modelling with EPA SWMM
- Rainfall–runoff simulation
- Horton infiltration configuration
- Dynamic Wave hydraulic routing
- Drainage network representation
- Green Roof LID configuration
- Interpretation of hydrologic and hydraulic model outputs
- Engineering documentation and reproducible project organisation

## Future development

Potential extensions include checking model connectivity and boundary conditions, reviewing routing stability, comparing baseline and LID scenarios on a consistent basis, conducting parameter sensitivity analysis, and incorporating verified GIS/catchment data and observed rainfall or flow records where available.

## Author

**Raisa Chowdhury**  
B.Sc. in Civil and Environmental Engineering  
Islamic University of Technology (IUT), Bangladesh
