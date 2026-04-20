__author__ = "Carlos Contreras Velasquez"
__email__ = "ccontreras@carnegiescience.edu"
import numpy as np
from math import cos,pi
import os,sys
from astroquery.simbad import Simbad
from magellan.core import ra_deg2equ,dec_deg2equ


customSimbad = Simbad()
customSimbad.add_votable_fields('pmra','pmdec')



txt='''


This tool connnects with Simbad to get coordinates of stars (and some other known celestial objects)
to get coordinates (Equinox 2000.0) and proper motions to create proper catalog lines for Magellan
telescopes. The user selects the correct line depending of the instrument to be used. The Rotation Angle
and the Rotation Mode must be edited according to the observer needs.


Usage: >  magellan_stars_coords   std_name

Example: > magellan_stars_coords LTT4364
Example: > magellan_stars_coords LTT\\ 4364
Example: > magellan_stars_coords 'SN 1987A'


'''


if (len(sys.argv)!=2):
    sys.exit(txt)


object_name = sys.argv[1] 

# Facility instruments and their Rotation Zero Points to present day 2026-04-20
instruments=['MIKE','LDSS3','IMACS','MAGE','FIRE-echelle','FIRE-longslit']
rot_zp     =[0, -62.5, -46.15, 44.5 , -30.0, 60.0]
obs_mode   =['GRV','HRZ','HRZ','HRZ','HRZ','HRZ']

result_table = customSimbad.query_object(object_name)
if( result_table is None):
    sys.exit("\nNo results.\nTry rewrite/other name.")


#print(result_table[0])

ra = result_table['ra'][0]
dec = result_table['dec'][0]

ra_s = ra_deg2equ(ra)   
de_s = dec_deg2equ(dec) 

pmra = result_table['pmra'][0]
pmdec= result_table['pmdec'][0]

lcopmra=0
lcopmdec=0
if(abs(pmra)>0 or abs(pmdec)>0):
    lcopmra = float(pmra/15000/cos(dec*pi/180.0))
    lcopmdec= float(pmdec/1000)

new_name=object_name.replace(' ','-')
NL = len(object_name)
c  = 0
for i in range(len(instruments)):
    line="%03d %s %s %s 2000.0 %+.6f %+.6f %7.2f %s 0 0 0 0 0 0 2000.0 # %s"%(i+1,new_name,ra_s,de_s,lcopmra, lcopmdec,rot_zp[i],obs_mode[i],instruments[i])
    print(line)


# -------------------------


def main():
    pass  # nothing needed

if __name__ == "__main__":
    main()

