"""
script to update old NOSEpick csv pick files to match output from newer version
Brandon S. Tober
24SEP2020
"""
### imports ###
import glob
import pandas as pd
import numpy as np

in_path = "/path/to/pick/files/"
in_path="/home/btober/Desktop/test/"

for f in glob.glob(in_path + "*.csv"):
  print(f)
  df = pd.read_csv(f,delimiter=",",index_col=False,header=0)
  df_out = pd.DataFrame({"trace": df["trace"], "lon": df["lon"], "lat": df["lat"], "alt": df["alt"], "gndElev": df["elev_gnd"],
                         "srfIdx": np.nan, "srfTwtt": df["twtt_surf"], "srfAmp": df["surf_amp"], 
                         "subsrfIdx": np.nan, "subsrfTwtt": df["twtt_bed"], "subsrfAmp": df["subsurf_amp"], 
                         "subsrfElev": df["elev_bed"], "thick": df["thick"]})

  df_out.to_csv(f.rstrip(".csv") + "_new.csv", index=False)