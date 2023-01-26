from datetime import datetime

weather_collection = "weather"
earthquake_collection = "earthquake"
aggregate_collection = "aggregate"


def fetch_data(mongo_helper, weather_api, earthquake_api, is_yesterday=False):
    earthquake_data = earthquake_api.fetch_yesterday_data() if is_yesterday else earthquake_api.fetch_monthly_data()

    for earthquake in earthquake_data:
        date_from_timestamp = datetime.fromtimestamp(earthquake["properties"]["time"] / 1000)

        weather_data = weather_api.weather_information(
            earthquake["geometry"]["coordinates"][1],
            earthquake["geometry"]["coordinates"][0],
            date_from_timestamp.strftime("%Y-%m-%d"))

        if weather_data is not None:
            weather_data["earthquake_id"] = earthquake["id"]
            weather_data["yesterday"] = is_yesterday
            print(str(earthquake["geometry"]["coordinates"][1]) + " " + str(earthquake["geometry"]["coordinates"][0]))
            print(weather_data)
            mongo_helper.add(weather_collection, [weather_data])
    # Store data in the database
    mongo_helper.add(earthquake_collection, earthquake_data)
