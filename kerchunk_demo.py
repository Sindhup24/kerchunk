import fsspec
import xarray as xr
import zarr
import matplotlib.pyplot as plt

# Open the reference file
fs = fsspec.filesystem("reference", fo="reference.json")
mapper = fs.get_mapper("")

# Consolidate metadata (recommended for efficiency)
zarr.consolidate_metadata(mapper)

# Access the dataset
ds = xr.open_dataset(mapper, engine="zarr", consolidated=True, decode_times=False)

# Print dataset information
print(ds)

# Example of accessing and plotting data
# Accessing 'uwind' variable
uwind = ds['uwind'].isel(time=0)

# Plot the 'uwind' variable for the first time slice
uwind.plot()
plt.title('U-Wind at Time=0')
plt.show()
