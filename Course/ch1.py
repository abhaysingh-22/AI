raw_spice_data = bytearray(b'abhay')
# raw_spice_data.replace(b'abhay', b'cinnamon')       this will show the original byte string i.e  bytearray(b'abhay') not the replaced one
raw_spice_data = raw_spice_data.replace(b'abhay', b'cinnamon')
print(f"Byte: {raw_spice_data}")