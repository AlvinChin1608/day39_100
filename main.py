# 4. pass the data back to main, so you can print data in main
from data_manager import DataManager

# Create a DataManager instance to interact with the Google Sheet
data_manager = DataManager()

# Retrieve destination data from the Google Sheet
sheet_data = data_manager.get_destination_data()
print(sheet_data)

#  5. In main.py check if sheet_data contains any values for the "iataCode" key.
# Check if the IATA Codes column is empty in the Google Sheet

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()

    # Iterate through each city in the destination data
    # and fetch the corresponding IATA code using the FlightSearch class
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row['city'])
    print(f"sheet_data:\n {sheet_data}")

    # Update the Google Sheet with the new IATA codes
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

