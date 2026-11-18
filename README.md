# 🚀 PySpark JSON Data Processing & ETL Pipeline

An end-to-end data engineering pipeline built with **PySpark** and **Docker** to ingest, clean, transform, and aggregate messy JSON datasets, simulating real-world data quality challenges.

---

## 🛠️ Project Architecture & Workflow

1. **Ingestion Layer**: Reads multi-line messy JSON data containing nulls, negative values, and whitespaces using PySpark.
2. **Data Cleaning & Validation**: 
   - Trims trailing/leading whitespaces from names (`trim`).
   - Standardizes string cases (`initcap`).
   - Filters out corrupt records, null salaries, and anomalous/negative values.
   - Categorizes salaries into `High` and `Standard` tiers using conditional logic (`when/otherwise`).
3. **Aggregation & Analytics**: Groups records by department to compute average salary, max salary, and total employee count.
4. **Containerization**: Fully dockerized environment with Python and OpenJDK (Java Runtime Environment) for portable, consistent execution.

---

## 📂 Project Structure

```text
pyspark_json_project/
│
├── data/
│   └── employees_messy_100.json   # Raw messy dataset (100+ records)
├── notebooks/
│   └── pip.py                     # Core PySpark ETL pipeline script
├── Dockerfile                     # Docker container configuration
├── requirements.txt               # Python dependencies (PySpark)
└── README.md                      # Project documentation
```

---

## 💻 Tech Stack

- **Python 3.10**
- **Apache Spark / PySpark 3.5**
- **Docker**
- **VS Code & Windows Terminal**

---

## ⚙️ Getting Started & Local Execution

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ahmed-ibrahim-EG/pyspark-json-pipeline.git
   cd pyspark-json-pipeline
   ```

2. **Run the script locally:**
   ```python
   python notebooks/pip.py
   ```

---

## 🐳 Running with Docker

1. **Build the Docker image:**
   ```bash
   docker build -t pyspark-json-app .
   ```

2. **Run the container:**
   ```bash
   docker run --rm pyspark-json-app
   ```

---

## 👨‍💻 Author
**Ahmed Ibrahim**  
*Freelance Junior Data Engineer | Computer Science Student at Alexandria University*