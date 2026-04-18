# magellan-tools
Suite of simple scripts to prepare catalogs and observations.


### mike_slit_orientation

MIKE slits dont follow the sky orientation of the sky, but its Position Angle (PA)
can be predicted. Accordingly, if a specific PA is necessary for a given observation
this tool helps to find the most convenient moment at the night to achieve the observation.

Usage:
```
>  mike_slit_orientation 16:23:21.3 -23:52:34.2    2026 04 18  04 30

#  Elevation(deg)  HourAng(hours)  ParAng(deg)  SidTime(hours)   PA(deg)
       51.28          21.15        -107.18          13.54          81.54

```

---
Carlos
