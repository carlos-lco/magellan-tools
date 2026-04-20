__author__ = "Carlos Contreras Velasquez"
__email__ = "ccontreras@carnegiescience.edu"
import numpy as np
from astroquery.jplhorizons import Horizons
from astropy import units as u
from astropy.coordinates import SkyCoord
import os,sys


txt='''

This tool connects to JPL Horizons to get ephemeris and motion rates (LCO format: sec/sec & arcsec/sec)
for asteroids and comets to create an ephemeris table that can be used as a ready-to-use catalog
for observing with Magellan telescopes. 

Usage:
          >  asteroids_magellan_ephemeris   NAME    UT-DATE-START    UT-DATE-END    TIME-STEP

Example1  >  asteroids_magellan_ephemeris  87306    2022-05-21   2022-05-22  30m

Example2  >  asteroids_magellan_ephemeris  87306    2022-05-21   2022-05-22  1h 


For comets use the Comet last orbit calculation ID, for example, for  Lemmon (C/2025 A6) is 90004899, then:


Example2  >  asteroids_magellan_ephemeris  90004899  2022-05-21   2022-05-22  1h 


After creating the catalog, the observer needs to edit the Rotation-Angle and Rotation-Mode columns
depending on the required instrument and orientation on the sky.


'''



if(len(sys.argv)!=5):
    sys.exit(txt)


ast_name=sys.argv[1]
ut_start = sys.argv[2]
ut_end   = sys.argv[3]
time_step = sys.argv[4]

obj = Horizons(id=ast_name, location='304',epochs={'start':ut_start, 'stop':ut_end, 'step':time_step},id_type=None)


eph = obj.ephemerides()
eph['RA_rate'].convert_unit_to('arcsec/s')
eph['DEC_rate'].convert_unit_to('arcsec/s')
eph['RA-Rate [s/s]']=eph['RA_rate']/np.cos(eph['DEC']*np.pi/180)/15

c = SkyCoord(ra=eph['RA'], dec=eph['DEC'], frame='icrs')

eph['ra']=c.ra.to_string(unit=u.hour, sep=':')
eph['dec']=c.dec.to_string(unit=u.degree, sep=':')



try:
    tabla=eph['datetime_str', 'ra', 'dec','RA-Rate [s/s]','DEC_rate','airmass','V']
    N = len(eph['ra'])
    print('##\n## Ephemeris for %s .\n##\n## Please change the Rotation Mode and Angle to your needs.\n##'%(eph['targetname'][0]))
    for i in range(N):
        line="%03d   %15s  %-15s  %-15s  2000.0  0  0  0  HRZ  0 0 0  0 0 0  0 # Rates: %13.10f %13.10f  V= %6.2f airmass= %6s ID: %s"%(i+1,eph['datetime_str'][i].replace(' ','_UT').replace(':','_'),eph['ra'][i],eph['dec'][i],eph['RA-Rate [s/s]'][i],eph['DEC_rate'][i],eph['V'][i],eph['airmass'][i],eph['targetname'][i])
        print(line)

except:
    tabla=eph['datetime_str', 'ra', 'dec','RA-Rate [s/s]','DEC_rate','airmass']
    N = len(eph['ra'])
    print('##\n## Ephemeris for %s .\n##\n## Please change the Rotation Mode and Angle to your needs.\n##'%(eph['targetname'][0]))
    for i in range(N):
        line="%03d   %15s  %-15s  %-15s  2000.0  0  0  0  HRZ  0 0 0  0 0 0  0 # Rates: %13.10f %13.10f  airmass= %6s ID: %s"%(i+1,eph['datetime_str'][i].replace(' ','_UT').replace(':','_'),eph['ra'][i],eph['dec'][i],eph['RA-Rate [s/s]'][i],eph['DEC_rate'][i],eph['airmass'][i],eph['targetname'][i])
        print(line)



#--------------------------------------

def main():
    pass  # nothing needed

if __name__ == "__main__":
    main()


