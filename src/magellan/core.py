__author__ = "Carlos Contreras Velasquez"
__email__ = "ccontreras@carnegiescience.edu"
from astropy.coordinates import Angle
from astropy import units as u



#  DEG -> EQU

def ra_equ2deg(ra):
    rah,ram,ras=ra.replace(':',' ').split()
    rah,ram,ras=float(rah),float(ram),float(ras)
    ra_deg = (rah+ram/60+ras/3600)*15
    return(ra_deg)


def dec_equ2deg(de):
    if(de[0]=='-'):
        sign=-1
    else:
        sign=1
    ded,dem,des=de.replace(':',' ').split()
    ded,dem,des=abs(float(ded)),float(dem),float(des)
    dec_deg = sign*(ded+dem/60+des/3600)
    return(dec_deg)


#  EQU -> DEG 

def ra_deg2equ(ra_deg):
    right_ascension = Angle(ra_deg,unit=u.deg)
    ra=right_ascension.to_string(unit=u.hourangle,sep=':',precision=2)
    return(ra) # string

    
def dec_deg2equ(dec_deg):
    declination = Angle(dec_deg,unit=u.deg)
    dec=declination.to_string(unit=u.deg,sep=':',precision=2)
    return(dec) # string



