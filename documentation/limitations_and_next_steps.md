# Limitations and recommended next steps

This repository documents the supplied academic SWMM model and its reported outputs.

1. **No field calibration/validation evidence supplied.** No observed flow, water level or independently validated rainfall dataset was included.
2. **Geospatial reference not established.** INP coordinates are local model coordinates; no verified CRS or georeferenced study-area boundary is provided.
3. **Rainfall input verification.** The report states 142 mm total precipitation. Confirm TS1 ordinates, rain-gauge format and interval against the intended design hyetograph.
4. **Network connectivity.** The INP contains no conduit connected to U1, while Pu1 connects U1 to O1. The report records zero pump utilisation and zero outfall discharge. Verify the intended hydraulic pathway.
5. **Routing stability.** The RPT reports 6.69% nonconverging steps and several high local continuity errors. Review time steps, geometry, node depths and hydraulic conditions.
6. **LID comparison.** A matched baseline run without LID and a consistent LID scenario are required to quantify catchment-level benefits. The current LID summary alone does not establish runoff reduction.
7. **Design applicability.** This is not a construction-ready design without verified survey data, design criteria, calibration/validation and professional review.

## Suggested development sequence
- Verify source rainfall and catchment parameter provenance.
- Verify node, conduit, storage, pump and outfall connectivity.
- Resolve numerical stability issues without tuning solely to improve continuity statistics.
- Establish a defensible baseline.
- Run controlled LID scenarios with consistent assumptions.
- Conduct sensitivity analysis for uncertain parameters.
- Add verified GIS mapping and observed data if available.
