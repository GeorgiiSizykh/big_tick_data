# Analysis of High-Frequency Crypto Trade Data (BTC/USDT)

This project demonstrates efficient processing and analysis of a large tick-level trade dataset for BTC/USDT. The main goal is to showcase skills in handling large datasets that do not fit into RAM and to perform foundational quantitative market microstructure analysis.

### Key Tasks
- **Data Aggregation:** Loading and aggregating over 100 million trades into 1-minute OHLCV bars using chunk-based processing in pandas.
- **Volatility and Volume Analysis:** Investigating the relationship between trading volume and price volatility on the 1-minute timeframe.
- **Market Activity Segmentation:** Dividing the data into high- and low-activity periods based on volume and comparing their volatility.

---

## Technologies Used
- **Python 3**
- **Libraries:** pandas, numpy, matplotlib, seaborn, pyarrow, hashlib

---

## Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/GeorgiiSizykh/big_tick_data
cd big_tick_data
```

### 2. Create and Activate a Virtual Environment (Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download Data
- Download the monthly BTC/USDT tick trade archive from [Binance Data Vision](https://data.binance.vision/?prefix=data/spot/monthly/trades/BTCUSDT/), e.g., `BTCUSDT-trades-2025-05.zip` and the corresponding `.CHECKSUM` file.
- Create a `raw_data` folder in the project root and place both files there.

### 5. Verify Data Integrity (Optional)
To verify the downloaded file, use the script:
```bash
python check_hash.py raw_data/BTCUSDT-trades-2025-05.zip raw_data/BTCUSDT-trades-2025-05.zip.CHECKSUM
```

### 6. Run the Analysis
1. Unzip `BTCUSDT-trades-2025-05.zip` into the `raw_data` folder to get the raw CSV file.
2. Launch Jupyter Notebook or JupyterLab:
```bash
jupyter lab
```
3. Open and run the `ticks_analysis.ipynb` notebook. It will:
   - Process the data in memory-efficient chunks and aggregate it into minute bars.
   - Save the results as a Parquet file for further analysis.
   - Perform exploratory analysis: visualization, volatility calculation, segmentation by volume, and more.

---

## Project Structure
- `ticks_analysis.ipynb` — main notebook with data processing and analysis code.
- `check_hash.py` — script for verifying the checksum of the downloaded archive.
- `requirements.txt` — minimal list of required libraries.
- `raw_data/` — folder for raw data cinluding downloaded archives and checksum files.
- `processed_data/` — folder for processed data (parquet files).


---

## Key Skills and Takeaways
- **Big Data Processing:** Using pandas chunking to work with files that do not fit into memory.
- **Aggregation and Resampling:** Converting tick data into structured time series (OHLCV bars).
- **Feature Engineering:** Creating new features (e.g., intrabar volatility, segmentation by volume).
- **Visualization and Analysis:** Exploring market patterns such as the relationship between volume and volatility.
- **Reproducibility:** The project is structured for easy repetition of all analysis steps.

---

## Contact
If you have questions or suggestions about the project, feel free to reach out!