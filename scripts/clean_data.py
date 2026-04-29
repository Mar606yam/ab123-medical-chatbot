# Import required Spark libraries
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, trim, regexp_replace

def main():
    # STEP 1: Initialize Spark Session
    # The appName will appear in the EMR console for tracking
    spark = SparkSession.builder \
        .appName("MedicalDataCleaning") \
        .get_all()

    # STEP 2: Define S3 Paths
    # Replace ab123-medical-chatbot with your actual S3 bucket name
    input_path = "s3://ab123-medical-chatbot/raw-data/medical_data_combined.json"
    output_path = "s3://ab123-medical-chatbot/processed-data/cleaned_medical_data"

    # STEP 3: Load Data from S3
    # Spark reads JSON Lines format efficiently in parallel
    print("Reading data from S3...")
    df = spark.read.json(input_path)

    # STEP 4: Data Cleaning Pipeline
    # 1. Remove null/empty values to ensure model quality
    # 2. Trim whitespace and convert text to lowercase for consistency
    # 3. Remove special characters that might confuse the LLM
    print("Starting cleaning process...")
    
    cleaned_df = df.dropna() \
        .withColumn("instruction", trim(col("instruction"))) \
        .withColumn("output", trim(col("output"))) \
        .filter((col("instruction") != "") & (col("output") != ""))

    # STEP 5: Save Processed Data back to S3
    # We save as Parquet or JSON. JSON is easier for the next Fine-tuning step.
    print(f"Saving cleaned data to: {output_path}")
    cleaned_df.write.mode("overwrite").json(output_path)

    print("Spark Job Completed Successfully!")
    spark.stop()

if __name__ == "__main__":
    main()