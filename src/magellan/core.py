
def ra2deg(ra):
    rah,ram,ras=ra.replace(':',' ').split()
    rah,ram,ras=float(rah),float(ram),float(ras)
    ra_deg = (rah+ram/60+ras/3600)*15
    return(ra_deg)


def dec2deg(de):
    if(de[0]=='-'):
        sign=-1
    else:
        sign=1
    ded,dem,des=de.replace(':',' ').split()
    ded,dem,des=abs(float(ded)),float(dem),float(des)
    dec_deg = sign*(ded+dem/60+des/3600)
    return(dec_deg)
