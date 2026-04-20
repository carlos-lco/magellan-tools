# Magellan Catalogs

Description
- Process an ascii input file with 7 columns into a usable Magellan Catalog.


Catalog creator tool. Use this script to create an observing catalog in the Magellan format.

Usage:

```
    >  magellan_catalog  input_file_with_targets     instrument   mode
```

Examples:

```
    >  magellan_catalog   my_targets.txt    LDSS3C        OFF  
    >  magellan_catalog   my_targets.txt    MIKE          GRV  
    >  magellan_catalog   my_targets.txt    MAGE          HRZ  
    >  magellan_catalog   my_targets.txt    IMACS         EQU  
    >  magellan_catalog   my_targets.txt    FIRE_ECHELLE  EQU  
    >  magellan_catalog   my_targets.txt    FIRE_LONGSLIT OFF  
    >  magellan_catalog   my_targets.txt    FOURSTAR      EQU  
```


where the input file contains 7 columns:

    1. Target name in 1 string (no blank spaces)
    2. RA coordinates in sexagesimal notation.
    3. Dec coordinates in sexagesimal notation.
    4. Epoch of coordinates (can be left as zero if proper motion is negligible).
    5. RA Motion rate in LCO format (sec/year). Can be calculated as:  RA_PM / [15000 * cos(Dec)] (use zero if negligible).
    6. Dec Motion rate in LCO format (arcsec/year). Can be calculated as:  DEC_PM / 1000  (use zero if negligible).
    7. Position Angle (PA)  (use zero if rotation mode is not EQU or OFF ).


    Input file Example:

    Feige34   10:39:36.756  +43:06:08.816  2015.5    +0.001267            -0.025586    0
    HD93521   10:48:23.512  +37:34:13.116  2015.5    +0.000033            +0.002131  -30 
    LTT4364   11:45:49.386  -64:50:34.818  2015.5    +0.417391            -0.344933   90
    M31        0:42:44.33    41:16:07.50     0           0                     0       0
    ...


Available modes: GRV, EQU, OFF &  HRZ.
Available insturments:  MIKE, LDSS3C, IMACS, MAGE, FOURSTAR, FIRE_ECHELLE, FIRE_LONGSLIT.




Dependencies
- `numpy, astropy`
