import numpy as np
import pandas as pd
import glob
import sys

# script designed to merge the picks from one directory in to a single csv file
# BST, 27NOV19

in_dir = "/media/btober/beefmaster/MARS/targ/supl/UAF/2019/picks/"
out_fname = "2019_combined.csv"

track = np.array([]).astype(str)
trace = np.array([]).astype(int)
lon = np.array([]).astype(np.float)
lat = np.array([]).astype(np.float)
alt = np.array([]).astype(np.float)
gndElev = np.array([]).astype(np.float)
srfIdx = np.array([]).astype(np.float)
srfTwtt = np.array([]).astype(np.float)
srfAmp = np.array([]).astype(np.float)
subsrfIdx = np.array([]).astype(np.float)
subsrfTwtt = np.array([]).astype(np.float)
subsrfAmp = np.array([]).astype(np.float)
subsrfElev = np.array([]).astype(np.float)
thick = np.array([]).astype(np.float)


for file in glob.glob(in_dir + "*pk.csv"):
    fname = file.split('/')[-1].rstrip("_pk.csv")
    print(fname)

    dat = np.genfromtxt(file, delimiter=",", dtype = None, names = True)

    track = np.append(track, np.repeat(fname,dat.shape[0]))
    trace = np.append(trace,dat["trace"].astype(int))
    lon = np.append(lon,dat["lon"])
    lat = np.append(lat,dat["lat"])
    alt = np.append(alt,dat["alt"])
    gndElev = np.append(gndElev,dat["gndElev"])
    srfIdx = np.append(srfIdx, dat["srfIdx"])
    srfTwtt = np.append(srfTwtt,dat["srfTwtt"])
    srfAmp = np.append(srfAmp,dat["srfAmp"])
    subsrfIdx = np.append(subsrfIdx,dat["subsrfIdx"])
    subsrfTwtt = np.append(subsrfTwtt,dat["subsrfTwtt"])
    subsrfAmp = np.append(subsrfAmp,dat["subsrfAmp"])
    subsrfElev = np.append(subsrfElev,dat["subsrfElev"])
    thick = np.append(thick,dat["thick"])


out = pd.DataFrame({"track": track, "trace": trace, "lon": lon, "lat": lat, "alt": alt, "gndElev": gndElev,
                    "srfIdx": srfIdx, "srfTwtt": srfTwtt, "srfAmp": srfAmp, 
                    "subsrfIdx": subsrfIdx, "subsrfTwtt": subsrfTwtt, 
                    "subsrfAmp": subsrfAmp, "subsrfElev": subsrfElev, "thick": thick})

out.to_csv(in_dir + out_fname, index=False)

print("Combined picks exported to:\t" + in_dir + out_fname)