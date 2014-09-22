
import pandas as pd
import re

# Reading in the file
with open('sampling_grid.kml') as f:
  text = "\n".join(f.readlines())

# Grabbing the coordinates
coords_text = re.findall(r'<coordinates>(.*?)</coordinates>', text)

# Converting to dictionary for use in pandas
coordinates = {"Longitude":[], "Latitude":[]}
for coord in coords_text:
  xy = coord.split(",")
  lon = float(xy[0])
  lat = float(xy[1])
  coordinates["Longitude"].append(lon)
  coordinates["Latitude"].append(lat)

# Writing to a  dataframe
coordinates = pd.DataFrame(coordinates)
coordinates.to_csv("UberPickupCoords.csv")
