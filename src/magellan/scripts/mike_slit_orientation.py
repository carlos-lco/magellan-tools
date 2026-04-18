from astroplan import Observer
LCO = Observer.at_site("Las Campanas Observatory")
from astropy.coordinates import EarthLocation
import astropy.units as u
Clay_location=EarthLocation.from_geodetic(-70.6925*u.deg, -29.01403*u.deg,2390*u.m)
LCO_Clay = Observer(location=Clay_location, name="Clay", timezone="America/Santiago")
from astropy.time import Time
from astropy.coordinates import SkyCoord
from magellan.core import ra2deg,dec2deg
import sys,os


txt='''


This tool helps the user to plan a MIKE night, i.e. to select the best time to observe
a target with a specific PA (Position Angle). For example, when a neighbor object
needs to be avoided, or when a specific orientation is needed for an extended object
or any other case. The resulting PA corresponds to the slit's orientation at the moment  
of telescope's acquisition of the target.  The PA is given in the interval [0,180] degrees.

The tool gives the elevation at the observing time as well, in order to check the
observability of the target (must be > 20 degrees).


Usage:

    MIKE_predict   ra(deg)  dec(deg)  yy(int)  mm(int)  dd(int)   hhh(int)  mmm(int)



Where the input parameters correspond to target coords and observing date and hour:
    ra: Right Ascention
    dec: Declination
    yy : UT year
    mm : UT month
    dd : UT day
    hhh: UT hour 
    mmm: UT minutes 


Example:

    mike_slit_orientation   16:23:21.3 -23:52:34.2    2024 05 09  02 30

'''


if(len(sys.argv)!=8):
    sys.exit(txt)



ra_t = ra2deg( sys.argv[1])
de_t = dec2deg(sys.argv[2])

yy = int(sys.argv[3])
mm = int(sys.argv[4])
dd = int(sys.argv[5])
hhh= int(sys.argv[6])
mmm= int(sys.argv[7])

time_str='%04d-%02d-%02d %02d:%02d:00'%(yy,mm,dd,hhh,mmm)
time = Time(time_str)

target= SkyCoord(ra_t*u.deg, de_t*u.deg,frame="icrs")
altaz = LCO_Clay.altaz(time,target)
ha    = LCO_Clay.target_hour_angle(time,target)
st    = LCO_Clay.local_sidereal_time(time,kind='apparent')
pa    = LCO_Clay.parallactic_angle(time,target)

p_ang = 180 + pa.deg + 90 - altaz.alt.deg - 30 # Position Angle of the Slit

while(p_ang>180):
    p_ang = p_ang - 180
while(p_ang<0):
    p_ang = p_ang + 180

#if(p_ang>180):
#    p_ang = p_ang - 360


comment = ""
if(altaz.alt.deg<20):
    comment = "Below Elevation Limit!"
if(altaz.alt.deg<18):
    comment = "Below Elevation Limit! Not observable."
if(altaz.alt.deg<0):
    comment = "Below Horizon! Not observable."

print("#  Elevation(deg)  HourAng(hours)  ParAng(deg)  SidTime(hours)   PA(deg)")
print("%12.2f   %12.2f   %12.2f   %12.2f   %12.2f    %s"%(altaz.alt.deg,ha.hour,pa.deg,st.hour,p_ang,comment))



def main():
    pass  # nothing needed

if __name__ == "__main__":
    main()
