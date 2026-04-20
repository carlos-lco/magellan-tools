# Stars Coordinates

Description
- Queries SIMBAD to retrieve coordinates and proper motions, and prints catalog lines formatted for Magellan instruments. Rotation Angle/Mode must be edited _a posteriori_ per observer needs.

Usage:

```
> magellan_stars_coords std_name
```

Examples:

```
> magellan_stars_coords LTT4364
> magellan_stars_coords "SN 1987A"
```




Dependencies
- `astroquery` (SIMBAD)
