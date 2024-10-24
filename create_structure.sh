#!/bin/bash

# Create the folder structure
mkdir -p project-management-tools-automation/automation
mkdir -p project-management-tools-automation/data
mkdir -p project-management-tools-automation/notebooks
mkdir -p project-management-tools-automation/tests
mkdir -p project-management-tools-automation/docker

# Create the necessary files
touch project-management-tools-automation/automation/data_collection.py
touch project-management-tools-automation/automation/reporting.py
touch project-management-tools-automation/automation/config.py
touch project-management-tools-automation/automation/__init__.py

touch project-management-tools-automation/data/raw_data.json
touch project-management-tools-automation/data/processed_data.csv

touch project-management-tools-automation/notebooks/automation_tests.ipynb

touch project-management-tools-automation/tests/test_data_collection.py
touch project-management-tools-automation/tests/test_reporting.py

touch project-management-tools-automation/docker/Dockerfile

# Additional files
touch project-management-tools-automation/README.md
touch project-management-tools-automation/requirements.txt
touch project-management-tools-automation/.gitignore
