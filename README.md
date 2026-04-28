# python-module

A small Python project demonstrating finance calculations, CSV data processing, object-oriented design, API integration, decorators, and FastAPI endpoints.

## Overview

This repository contains learning examples across several Python concepts:

- `main.py` - a simple entry point that prints a greeting.
- `1_market_cap/` - market capitalization calculation.
- `2_ratios/` - functional CSV ratio calculation.
- `3_classes/` - class-based CSV ratio calculation.
- `4_apis/` - GitHub profile analyzer using the GitHub REST API.
- `5_decorator/` - comparing a timed function decorator with a plain implementation.
- `6_fastapi/` - FastAPI examples for a random joke endpoint and a GROQ-powered joke generator.

## Requirements

- Python 3.13 or newer
- Dependencies are listed in `pyproject.toml`

## Installation

1. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install the package and dependencies:

```bash
pip install -e .
```

3. Install optional runtime tools if needed:

```bash
pip install uvicorn
```

## Project Structure

- `main.py`
- `pyproject.toml`
- `1_market_cap/market_cap.py`
- `2_ratios/calc_ratios.py`
- `2_ratios/in.csv`
- `2_ratios/out.csv`
- `3_classes/calc_ratios.py`
- `4_apis/github_analyzer.py`
- `5_decorator/with_decorator.py`
- `5_decorator/without_decorator.py`
- `6_fastapi/1_get_joke.py`
- `6_fastapi/2_generate_joke.py`

## Usage Examples

### Run the main script

```bash
python main.py
```

### Market capitalization

```bash
python 1_market_cap/market_cap.py
```

This module calculates market cap as `price_per_share * total_shares`.

### Ratio calculation with CSV

```bash
python 2_ratios/calc_ratios.py
```

Reads `2_ratios/in.csv`, computes `price_to_book_ratio` and `pe_ratio`, then writes results to `2_ratios/out.csv`.

### Ratio calculation using a class

```bash
python 3_classes/calc_ratios.py
```

Implements the same ratio processing using `RatioCalculator` and object-oriented structure.

### GitHub API example

```bash
python 4_apis/github_analyzer.py
```

Enter a GitHub username when prompted to fetch profile statistics from the GitHub API.

### Decorators and timing

```bash
python 5_decorator/with_decorator.py
```

Compares a loop-based sum with a formula-based sum while measuring execution time via a decorator.

## FastAPI Examples

### Random Joke API

Run the joke endpoint:

```bash
uvicorn "6_fastapi.1_get_joke:app" --reload --port 8000
```

Open `http://127.0.0.1:8000/joke` in a browser or use:

```bash
curl http://127.0.0.1:8000/joke
```

### GROQ Joke Generator

Set the environment variable and run:

```bash
set GROQ_API_KEY=your_api_key
uvicorn "6_fastapi.2_generate_joke:app" --reload --port 8001
```

Request a joke by topic:

```bash
curl "http://127.0.0.1:8001/joke?topic=python"
```

## Notes

- `2_ratios/calc_ratios.py` and `3_classes/calc_ratios.py` demonstrate two styles of CSV processing.
- `4_apis/github_analyzer.py` uses the `requests` package and handles HTTP status codes.
- `6_fastapi/2_generate_joke.py` requires `GROQ_API_KEY` and optionally `GROQ_MODEL`.

## License

This repository is provided as a learning example.
