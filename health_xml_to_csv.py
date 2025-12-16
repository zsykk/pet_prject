import xml.etree.ElementTree as ET
import csv
import pandas as pd

# Convert XML file to csv file
XML_FILE = "export.xml"
CSV_FILE = "health_data.csv"

tree = ET.parse(XML_FILE)
root = tree.getroot()

with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    # CSV 表头
    writer.writerow([
        "type",
        "value",
        "unit",
        "startDate",
        "endDate",
        "sourceName"
    ])

    for record in root.findall("Record"):
        writer.writerow([
            record.attrib.get("type"),
            record.attrib.get("value"),
            record.attrib.get("unit"),
            record.attrib.get("startDate"),
            record.attrib.get("endDate"),
            record.attrib.get("sourceName"),
        ])

print("Done! CSV saved as health_data.csv")


# Save daily walk data
df = pd.read_csv("health_data.csv")
