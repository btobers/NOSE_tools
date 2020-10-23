"""
script to update old NOSEpick csv pick files to match output from newer version
Brandon S. Tober
24SEP2020
"""
### imports ###
import glob
import pandas as pd
import numpy as np

in_path = "/media/btober/beefmaster/MARS/targ/supl/UAF/2016/picks/"

for f in glob.glob(in_path + "*.csv"):
  df_out = None
  print(f)
  df = pd.read_csv(f,delimiter=",",index_col=False,header=0)
  
  # determine if df has alt or elev_air
  if "alt" in df.keys():
    alt = df["alt"]
  else:
    alt = df["elev_air"]

  # determine if input df has amp data
  if "surf_amp" in df.keys():
    srfAmp = df["surf_amp"]
    subsrfAmp = df["subsurf_amp"]
  else:
    srfAmp = np.nan
    subsrfAmp = np.nan

  if "subsrfElev" in df.keys():
    continue


  try:
    df_out = pd.DataFrame({"trace": df["trace"], "lon": df["lon"], "lat": df["lat"], "alt": alt, "gndElev": df["elev_gnd"],
                          "srfIdx": np.nan, "srfTwtt": df["twtt_surf"], "srfAmp": srfAmp, 
                          "subsrfIdx": np.nan, "subsrfTwtt": df["twtt_bed"], "subsrfAmp": subsrfAmp, 
                          "subsrfElev": df["elev_bed"], "thick": df["thick"]})
  except Exception as err:
    print(err)

  df_out.to_csv(f, index=False)