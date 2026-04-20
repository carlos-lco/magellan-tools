# MIKE Exposure Time Estimator

Description
- This tool estimates an exposure time to achieve a requested S/N around 5500 AA (V band) 
with MIKE at given airmass, seeing, slit-width and binning.
This is just a zero order approximation, to have a rough idea of the exposure time needed
for a given target, and to be fine tuned during observations.


Usage:

1) If the target name is known V magnitude can be taken from SIMBAD:

```
> mike_exposure_time_estimator target S/N airmass seeing slit-width binning-Y
```

2) Provide magnitude explicitly:
```
> mike_exposure_time_estimator target S/N airmass seeing slit-width binning-Y   V_mag
```

Examples:

```
> mike_exposure_time_estimator LTT4364  100  1.6  0.80  0.70  1
> mike_exposure_time_estimator AnyStar   50  1.3  0.95  1.00  2   17.5
```


Dependencies
- `astroquery` (SIMBAD), `scipy`, `numpy`

---
