# Model inventory

Parsed from the supplied INP file:

- Subcatchments: 35
- Junctions: 45
- Conduits: 40
- Storage units: 1
- Pumps: 1
- Outfalls: 1
- LID usage records: 4

## Configuration observations

- Pump Pu1 connects U1 to O1 and has status ON, but the report shows zero pump utilisation and zero outfall discharge.
- No conduit record in the supplied INP has U1 as its upstream or downstream node. The supplied network therefore does not show a conduit connection from the junction/conduit network into U1.
- `ALLOW_PONDING` is set to NO.
- J36, J37, J39 and J38 have a maximum depth of zero in the input file; verify intended node settings before hydraulic interpretation.
- The LID control is `GR` (Green Roof).

These are configuration observations, not claims about the intended design. Confirm intended topology, pump curve and boundary conditions before modifying the model.
