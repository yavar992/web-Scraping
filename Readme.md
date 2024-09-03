# Web Scraping Project

This project scrapes car information from the ZigWheels website, specifically for cars priced under 50 lakhs. It extracts car names, prices, and ratings, and saves the data to CSV and Excel files. 

Additionally, it includes a script named `Imdb25.py` for scraping the top 25 IMDb movies.

## Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`
- `pandas`

## Setup
1. Install dependencies:
    ```bash
    pip install requests beautifulsoup4 pandas
    ```

2. Run the scripts:
    ```bash
    python webScrapping.py
    python Imdb25.py
    ```

## Docker
A Dockerfile is included for containerization. Build and run the Docker container using the following commands:
```bash
docker build -t webscrapping .
docker run -it --rm webscrapping
