import csv
import struct
import glob
import os

output_file = 'points.bin'
input_pattern = 'points_*.csv'

data = bytearray()
count = 0

min_lat, max_lat = 90.0, -90.0
min_lng, max_lng = 180.0, -180.0

files = glob.glob(input_pattern)
files.sort()

if not files:
    print("No input CSV files found.")
    exit()

print(f"Found {len(files)} files: {files}")

for input_file in files:
    print(f"Processing {input_file}...")
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            try:
                header = next(reader)
                try:
                    float(header[1])
                    f.seek(0)
                    reader = csv.reader(f)
                except ValueError:
                    pass
            except StopIteration:
                continue

            for row in reader:
                if len(row) >= 3:
                    try:
                        lat = float(row[1])
                        lng = float(row[2])
                        
                        if lat < min_lat: min_lat = lat
                        if lat > max_lat: max_lat = lat
                        if lng < min_lng: min_lng = lng
                        if lng > max_lng: max_lng = lng

                        data.extend(struct.pack('ff', lat, lng))
                        count += 1
                    except ValueError:
                        continue
    except Exception as e:
        print(f"Error reading {input_file}: {e}")

if not data:
    print("No valid data found.")
    exit()

with open(output_file, 'wb') as f:
    f.write(data)

print(f"\nSuccessfully converted {count} total points to binary.")
print(f"File size: {len(data) / 1024 / 1024:.2f} MB")
print(f"Bounds: Lat {min_lat:.2f}-{max_lat:.2f}, Lng {min_lng:.2f}-{max_lng:.2f}")