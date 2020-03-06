import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import random
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("Object class one of 6, 15, 16, 42, 52, 53, 62, 64, 65, 67, 88, 90, 92, 95")
parser.parse_args()

usrinput = int(sys.argv[1])


t=pd.read_csv("./training_set.csv")
m=pd.read_csv("./training_set_metadata.csv")


n=m[m['target'] == usrinput]
classes=np.unique(n['object_id'],return_counts=True)
object=classes[0][random.randint(1,len(classes[1]))]

lightcurve = t.loc[t['object_id']==object]
mjdstart = lightcurve['mjd'].iloc[0]
u = lightcurve.loc[lightcurve['passband']==0]
g = lightcurve.loc[lightcurve['passband']==1]
r = lightcurve.loc[lightcurve['passband']==2]
i = lightcurve.loc[lightcurve['passband']==3]
z = lightcurve.loc[lightcurve['passband']==4]
y = lightcurve.loc[lightcurve['passband']==5]

header = m.loc[m['object_id']==object]
objclass = header['target'].iloc[0]
specz = header['hostgal_specz'].iloc[0]
photz = header['hostgal_photoz'].iloc[0]
gallat = header['gal_b'].iloc[0]




title = "Object number: " + str(object) + ", Object class: " + str(objclass) + "\n\n PhotZ = " + str(photz) + ", SpecZ = " + str(specz) + ", GalLat = " + str(gallat) + "deg"


plt.subplots_adjust(hspace=0)

ax1=plt.subplot (6,1,6)
plt.ylabel("Y")
plt.xlabel("MJD")
plt.errorbar(y['mjd']-mjdstart,y['flux'], yerr=y['flux_err'],fmt='o',color='y')

ax2=plt.subplot (6,1,5,sharex=ax1)
plt.ylabel("z")
plt.errorbar(z['mjd']-mjdstart,z['flux'], yerr=z['flux_err'],fmt='o',color='k')

ax3=plt.subplot (6,1,4,sharex=ax1)
plt.ylabel("i")
plt.errorbar(i['mjd']-mjdstart,i['flux'], yerr=i['flux_err'],fmt='o',color='m')

ax4=plt.subplot (6,1,3,sharex=ax1)
plt.ylabel("r")
plt.errorbar(r['mjd']-mjdstart,r['flux'], yerr=r['flux_err'],fmt='o',color='r')

ax5=plt.subplot (6,1,2,sharex=ax1)
plt.ylabel("g")
plt.errorbar(g['mjd']-mjdstart,g['flux'], yerr=g['flux_err'],fmt='o',color='g')

ax6=plt.subplot (6,1,1,sharex=ax1)
plt.title(title)
plt.ylabel("u")
plt.errorbar(u['mjd']-mjdstart,u['flux'], yerr=u['flux_err'],fmt='o',color='b')

plt.show()

