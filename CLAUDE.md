# Ecommerce Data Platform

An end-to-end data engineering project built on the [Brazilian E-commerce dataset (Olist)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), covering ingestion, transformation, and visualisation using modern data stack tools.


## Tech Stack

- **Storage:** AWS S3
- **Data Warehouse:** Snowflake
- **Transformation:** dbt
- **Visualisation:** Looker Studio
- **Language:** Python 3.10+
- **Package manager:** uv

## Project Structure

```
ecommerce-data-platform/
├── data/                       # Raw CSV files (gitignored)
├── ingestion/                  # Python scripts: local CSVs → S3
├── snowflake/                  # Snowflake scripts
├── dbt/                        # dbt project
├── looker/                     # Looker Studio assets
├── .env                        # Local credentials (gitignored) — includes S3 bucket name, region and AWS credentials
└── CLAUDE.md
```

## Dataset

9 CSV files from the Olist Brazilian E-commerce dataset located in `data/`. Source: [Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).

- `olist_orders_dataset.csv` — core orders table
- `olist_order_items_dataset.csv` — items within each order
- `olist_customers_dataset.csv` — customer details
- `olist_products_dataset.csv` — product catalogue
- `olist_sellers_dataset.csv` — seller details
- `olist_order_payments_dataset.csv` — payment methods and values
- `olist_order_reviews_dataset.csv` — customer review scores
- `olist_geolocation_dataset.csv` — Brazilian zip code coordinates
- `product_category_name_translation.csv` — Portuguese to English category names

## Python Environment

This project uses [uv](https://github.com/astral-sh/uv) for package management. Use `uv add` to install packages, `uv run` to execute scripts, and `uv sync` to recreate the environment after cloning. Project config is in `pyproject.toml` and `.python-version`.

## Python Best Practices

- Write simple, readable code — prefer clarity over cleverness
- One function, one responsibility — keep functions small and focused
- Use descriptive variable and function names — code should read like plain English
- Avoid deeply nested logic — flatten with early returns where possible
- Handle errors explicitly — never silently swallow exceptions
- Use type hints for function signatures
- Add docstrings to all functions explaining what they do, their inputs and outputs
- Log meaningful messages at each step — avoid silent scripts

## Conventions

- Credentials always come from `.env` via `python-dotenv`
- Never use positional references ($1, $2, $3) in SQL — always use explicit column names with aliases

## Ground Rules

- Always propose a plan and wait for approval before writing any code
- Never commit to Git without explicit instruction
- Never modify `.env` or `.gitignore`
- Never commit the `data/` folder or any CSV files
