# Airplane Wildlife Collisions Data Analysis

This project analyzes data from the FAA's Wildlife Strike Database. My goal was to provide information to pilots, airports, and their employees that informs their solutions for preventing collisions. I achieved this by determining when collisions occur and the conditions that they occur under. The projects' conclusions are in project.ipynb.

## Scope
The following columns from the dataset are used: INCIDENT_YEAR, INCIDENT_MONTH, SPECIES, SKY, TIME_OF_DAY, and PHASE_OF_FLIGHT.
The dataset was cleaned by removing rows with blank cells. This is perfomed by the load_data.py module.

## Running the project
The jupyter notebook, project.ipynb, has already been run and is ready to view. To run it again, the annual_collisions.py, avg_monthly_collisions.py, and load_data.py modules and the dataset are required. The dataset must include years 1990-2015, which is included in the latest dataset download. Instructions for accessing and exporting the dataset are below.

## Dataset access
To access the dataset, go to the address at the end of the citation and click the 'Download Excel' button under the 'Download the FAA Wildlife Strike Database' section. Once downloaded, the dataset must be converted into a csv. To do so, open the file, select the file tab, select save as, and select CSV UTF-8 from the drop down.

## References
Federal Aviation Administration (2025). FAA Wildlife Strike Database [DATASET]. https://wildlife.faa.gov/search
