__author__ = "Carlos Contreras Velasquez"
__email__ = "ccontreras@carnegiescience.edu"
import numpy as np
import os,sys
from astroquery.simbad import Simbad
from scipy.special import erf
customSimbad = Simbad()
customSimbad.add_votable_fields('pmra','pmdec','flux(V)')


txt='''

This tool gives a first guess of exposure time in order to get some S/N in the order # 62 (Vmag, ~5500 AA)
given airmass, seeing, slit-width and binning in Y direction.


If the target is a bright star, the V_mag can be obtained from Simbad, in that case do as:

Usage1 :   >    mike_exposure_time_estimator    target  S/N  airmass  seeing  slit-width   binning-Y

Otherwise give the magnitude directly:

Usage2 :   >    mike_exposure_time_estimator    target  S/N  airmass  seeing  slit-width   binning-Y   V_mag



Examples:

Example: >    mike_exposure_time_estimator      LTT4364  100     1.6     0.85     0.70        1
Example: >    mike_exposure_time_estimator      LTT4364  100     1.3     1.55     1.00        2

Example: >    mike_exposure_time_estimator       X        50     1.6     0.85     0.70        1        15
Example: >    mike_exposure_time_estimator      AnyStar   50     1.3     1.55     1.00        2        17.5





There are no clouds in the underlying assumptions, so modify the exposure time accordingly.


'''

if (len(sys.argv)!=7 and len(sys.argv)!=8):
    sys.exit(txt)

object_name = sys.argv[1] 

s2n_req = float(sys.argv[2])
airm    = float(sys.argv[3])
seeing  = float(sys.argv[4])
slit    = float(sys.argv[5])
binn_y  =   int(sys.argv[6])

if(len(sys.argv)==8):
    m_V = float(sys.argv[7])
else:
    result_table = customSimbad.query_object(object_name)
    if( result_table is None):
        sys.exit("\nNo results.\nTry rewrite/other target name.")
    if('V' in result_table.colnames):
        m_V = result_table['V'][0]
    else:
        print(result_table.keys)
#print("%s  V: %.2f "%(object_name,m_V))
Tau =erf(0.8325*slit/seeing)
k_V = 0.11 # From ESO web page: https://www.eso.org/sci/observing/tools/Extinction.html
Sy = 0.05*binn_y #
M_V = 17.70 # from Marcelos's numbers
Iv = pow(10, 0.4*(M_V - m_V - k_V * (airm - 1)))
expt = ( s2n_req **2 ) / (Iv * Sy * Tau)
    
line='\n-----%s-----\n  V: %.2f  required S/N: %5.1f --> Exposure Time: %7.1f sec  [binn-Y: %d, seeing: %.2f, airmass: %.2f, slit: %.2f\"]'%(object_name,m_V,s2n_req,expt,binn_y,seeing,airm,slit)
print(line)
    


def main():
    pass  # nothing needed

if __name__ == "__main__":
    main()
    
