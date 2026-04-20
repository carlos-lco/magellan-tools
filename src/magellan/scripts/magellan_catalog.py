import numpy as np
import os,sys



# Available instruments
modes = ['HRZ','EQU','OFF','GRV']
instruments=['IMACS','MAGE','MIKE','LDSS3','FIRE_ECHELLE','FIRE_LONGSLIT','FOURSTAR']



txt='''

Catalog creator tool. Use this script to create an observing catalog in the Magellan format.

Usage:

    >  magellan_catalog  input_file_with_targets     instrument   mode


Examples:

    >  magellan_catalog   my_targets.txt    LDSS3C        OFF  
    >  magellan_catalog   my_targets.txt    MIKE          GRV  
    >  magellan_catalog   my_targets.txt    MAGE          HRZ  
    >  magellan_catalog   my_targets.txt    IMACS         EQU  
    >  magellan_catalog   my_targets.txt    FIRE_ECHELLE  EQU  
    >  magellan_catalog   my_targets.txt    FIRE_LONGSLIT OFF  
    >  magellan_catalog   my_targets.txt    FOURSTAR      EQU  


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


'''


if(len(sys.argv)!=4):
    sys.exit(txt)


inst = sys.argv[2]
mode = sys.argv[3]
# To capitals
inst=inst.upper()
mode=mode.upper()

if(inst not in instruments):
    sys.exit(txt)
if(mode not in modes):
    sys.exit(txt)

# reading the strings data
target_name, ra_coord,dec_coord = np.loadtxt(sys.argv[1],unpack=True,usecols=(0,1,2),dtype='U',ndmin=2)

# reading the numeric part of the data
epoch, mr_ra, mr_dec, angle = np.loadtxt(sys.argv[1],unpack=True,usecols=(3,4,5,6),ndmin=2)



# Cases:

# FOURSTAR
if(inst=='FOURSTAR'):
    for i in range(len(target_name)):
        line='%25s |  %15s | %15s | 2000.0 | %7.3f | Comment'%(target_name[i],ra_coord[i],dec_coord[i],angle[i])
        print(line)
else:

    # MIKE
    if(inst=='MIKE'):
        mode='GRV'
        angle = 0*angle
    
    #MAGE
    if(inst=='MAGE'):
        rzp = 44.5
        if(mode=='HRZ'):
            angle = angle*0 + rzp
        if(mode=='EQU' or mode=='OFF'):
            angle = angle + rzp
        if(mode=='GRV'):
            sys.exit('Please try other mode for MAGE.')
    
    #IMACS
    if(inst=='IMACS'):
        rzp = -46.15
        if(mode=='HRZ'):
            angle = angle*0 + rzp
        if(mode=='EQU' or mode=='OFF'):
            angle = angle + rzp
        if(mode=='GRV'):
            sys.exit('Please try other mode for IMACS.')
    
    #LDSS3C
    if(inst=='LDSS3C'):
        rzp = -62.5
        if(mode=='HRZ'):
            angle = angle*0 + rzp
        if(mode=='EQU' or mode=='OFF'):
            angle = angle + rzp
        if(mode=='GRV'):
            sys.exit('Please try other mode for LDSS3C.')
    
    #FIRE_ECHELLE
    if(inst=='FIRE_ECHELLE'):
        rzp = -30
        if(mode=='HRZ'):
            angle = angle*0 + rzp
        if(mode=='EQU' or mode=='OFF'):
            angle = angle + rzp
        if(mode=='GRV'):
            sys.exit('Please try other mode for FIRE_ECHELLE.')
    
    #FIRE_LONGSLIT
    if(inst=='FIRE_LONGSLIT'):
        rzp = 60
        if(mode=='HRZ'):
            angle = angle*0 + rzp
        if(mode=='EQU' or mode=='OFF'):
            angle = angle + rzp
        if(mode=='GRV'):
            sys.exit('Please try other mode for FIRE_LONGSLIT.')
    
    
    for i in range(len(target_name)):
        line = '%03d %25s %15s %15s  2000.0   %9.6f  %9.6f  %8.3f  %3s 0 0 0 0 0 0 %8.3f #comments--> '%(i+1,target_name[i],ra_coord[i],dec_coord[i],mr_ra[i],mr_dec[i],angle[i],mode,epoch[i])
        print(line)




def main():
    pass  # nothing needed

if __name__ == "__main__":
    main()
    

