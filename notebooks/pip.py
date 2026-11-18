from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, initcap, when, avg, max, count

spark = SparkSession.builder \
    .appName("JsonProcessingApp") \
    .master("local[*]") \
    .getOrCreate()

file_path = r"D:\Pyspark\pyspark_json_project\data\employees_messy_100.json"

df = spark.read \
    .option("multiLine", "true") \
    .json(file_path)

df.show(10, truncate=False)

print("Total Records:", df.count())

df_cleaned = df.withColumn("name", initcap(trim(col("name"))))

df_filtered = df_cleaned.filter(col("salary").isNotNull() & (col("salary") > 0))

df_final = df_filtered.withColumn(
    "salary_category",
    when(col("salary") > 12000, "High")
    .otherwise("Standard")
)

df_final.select("id", "name", "department", "salary", "salary_category").show(10, truncate=False)

dept_summary = df_final.groupBy("department") \
    .agg(
        avg("salary").alias("avg_salary"),
        max("salary").alias("max_salary"),
        count("id").alias("employee_count")
    ) \
    .orderBy(col("avg_salary").desc())

print("--- Department Salary Summary ---")
dept_summary.show(truncate=False)