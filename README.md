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


### mike_exposure_time_estimator


Usage 1, for a known star:

```
>  mike_exposure_time_estimator  LTT4364  100     1.6     0.85     0.70        2 

-----LTT4364-----
  V: 11.51  required S/N: 100.0 --> Exposure Time:   533.3 sec  [binn-Y: 2, seeing: 0.85, airmass: 1.60, slit: 0.70"]

```

Usage 2, for a given V magnitude:
```
>  mike_exposure_time_estimator  star-X  100     1.6     0.85     0.70        4  13

-----star-X-----
  V: 13.00  required S/N: 100.0 --> Exposure Time:  1049.0 sec  [binn-Y: 2, seeing: 0.85, airmass: 1.60, slit: 0.70"]

```




---
Carlos
