import logging
import time

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def extract():
    logging.info("Starting Extract step...")
    time.sleep(2)

    data = [
        {"id": 1, "name": "Alice", "salary": 5000},
        {"id": 2, "name": "Bob", "salary": 7000},
        {"id": 3, "name": "Charlie", "salary": 9000}
    ]
    print("created sample dataframe")
    logging.info(f"Extracted {len(data)} records")
    return data


def transform(data):
    logging.info("Starting Transform step...")
    time.sleep(2)

    for row in data:
        row["salary"] = row["salary"] * 1.10

    logging.info("Salary increased by 10%")
    return data


def load(data):
    logging.info("Starting Load step...")
    time.sleep(2)

    for row in data:
        logging.info(row)

    logging.info("Load completed successfully")


def main():
    logging.info("===== ETL Started =====")

    data = extract()
    data = transform(data)
    load(data)

    logging.info("===== ETL Finished =====")


if __name__ == "__main__":
    main()