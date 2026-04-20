# MIKE Slit Orientation Predictor

Description
- Computes the slit position angle (PA) for a target at a given UT time for planning MIKE observations. 
- Also prints elevation to assess observability.

Usage
```
 > mike_slit_orientation  ra  dec   yy mm dd  hh mm
```

Example

```
 > mike_slit_orientation 16:23:21.3 -23:52:34.2  2024 05 09   02 30
```

Notes
- Output columns: Elevation(deg), Hour Angle, Parallactic Angle, Sidereal Time, PA(deg).
- PA returned is in [0,180] degrees. Script warns if elevation is below observability limits.

Dependencies
- `astroplan`, `astropy`.
---
