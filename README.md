# Mapa Cieplików - McDonald's 2025

**Deployed at:** https://ciepliki.pages.dev

This project visualizes "Ciepliki" locations from the McDonald's promotional event. It handles approximately 1.1 million points using a binary data format and client-side clustering.

## Features

*   Renders ~1.1 million points in the browser.
*   Uses a binary format (.bin) to reduce file size.
*   Clustering implemented via Supercluster and Web Worker.
*   Geolocation support.
*   City search functionality.

## Setup & Usage

### 1. Prerequisites
*   Python 3.x

### 2. Download Data
You can either extract the `points_csv_archive.zip` file included in this repository or run the downloader script to fetch fresh data:
```bash
python3 download_all_points.py
```

### 3. Process Data
Convert CSV files into the binary format:
```bash
python3 convert_to_bin.py
```
This creates `points.bin`.

### 4. View Map
Open `index.html` in a web browser.

Note: A local server may be required due to CORS restrictions:
```bash
python3 -m http.server 8000
```
Then visit `http://localhost:8000`.

## Project Structure

*   `points_csv_archive.zip` - Archive containing the raw CSV data points.
*   `download_all_points.py` - Downloads raw CSV data.
*   `convert_to_bin.py` - Converts data to binary format.
*   `index.html` - Map interface.
*   `points.bin` - Binary coordinate data (generated).

## Disclaimer
This tool is for educational purposes only. It is not affiliated with McDonald's.