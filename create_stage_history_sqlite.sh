#!/bin/bash

# Name of the SQLite database file
DATABASE_FILE="eskom_stages.sqlite"
# Path to the CSV file
CSV_FILE="out.csv"
# Table name in SQLite database
TABLE_NAME="stage"

# Create a new SQLite database and table with the appropriate schema
sqlite3 $DATABASE_FILE <<EOF
-- Drop the table if it already exists
DROP TABLE IF EXISTS $TABLE_NAME;
-- Create a new table with the correct column types
CREATE TABLE $TABLE_NAME (
    id INTEGER PRIMARY KEY,
    created_at DATE,
    stage FLOAT,
    year_week TEXT,
    year_month TEXT,
    year TEXT,
    month TEXT,
    week TEXT,
    year_month_day TEXT
);
EOF

# Import CSV data into the SQLite database table
sqlite3 -csv $DATABASE_FILE ".import $CSV_FILE $TABLE_NAME"

echo "CSV file imported successfully into SQLite database."

