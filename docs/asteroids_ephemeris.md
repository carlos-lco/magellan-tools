# Asteroids Ephemeris

Description
- Connects to JPL Horizons to get ephemeris and motion rates (LCO format) for asteroids and comets to create a ready-to-use Magellan catalog.

Usage:
```
> magellan_asteroids_ephemeris NAME UT-DATE-START UT-DATE-END TIME-STEP
```

Examples

```
> magellan_asteroids_ephemeris 87306 2022-05-21 2022-05-22 10m

> magellan_asteroids_ephemeris 87306 2022-05-21 2022-05-22 1h
```

Comets can be queried as well, but using the last orbit's ID. For example:

```
> magellan_asteroids_ephemeris 90004899  2022-05-21  2022-05-22   10m
```

Notes
- Output is printed to stdout. Saved as an ascii file it can be used as a Magellan observing catalog.
- The user should edit the Rotation-Angle and Rotation-Mode columns depending on requested instrument and observing mode.
- Motion Rates in the LCO format are included in the output catalog.

Dependencies
- `astroquery` (JPL Horizons), `astropy`, `numpy`
