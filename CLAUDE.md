# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a Singapore wage analysis application that processes government wage data from Excel files (2021-2024) and provides both a Streamlit web dashboard and CLI tool for analyzing wage trends across occupations and industries.

## Commands

### Installation
```bash
pip install -r requirements.txt
```

### Running the Applications

**Streamlit Dashboard:**
```bash
streamlit run app.py
```

**CLI Tool:**
```bash
python wages_cli.py
```

### Testing & Development

No test framework is currently set up. When implementing tests, check for test scripts first.

## Architecture

### Data Processing Pipeline
1. **data_loader.py**: Core data loading module that:
   - Reads multiple Excel files (2021-2024 wage data)
   - Maps sheet names (T4, T4.1, etc.) to industry names
   - Cleans wage data (handles suppressed 's' values)
   - Returns unified DataFrame with standardized column names

2. **app.py**: Streamlit web dashboard with:
   - Interactive occupation search and comparison (up to 3)
   - Basic/Gross wage trend visualization using Plotly
   - Year-over-year growth rate calculations
   - CSV and PNG export functionality

3. **wages_cli.py**: Command-line interface with:
   - Fuzzy search for occupations
   - Radio list for industry selection
   - Tabulated data display
   - Matplotlib charts for wage trends

### Data Structure
Excel files contain wage percentile data (P25, Median, P75) for both Basic and Gross wages across:
- 14 industry categories (mapped from sheet names T4 to T4.14)
- Multiple occupations with SSOC codes
- Years 2021-2024

Key DataFrame columns after processing:
- Year, Industry, SSOC_Code, Occupation
- Basic_P25, Basic_Median, Basic_P75
- Gross_P25, Gross_Median, Gross_P75