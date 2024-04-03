place_name = "My house"
place_desc = "no description yet"
place_nb_rooms = 4
place_nb_bath = 0
place_max_guests = -3
place_price = 100
place_lat = -120.12
place_lon = 0.41921928

city_id = "1"
user_id = "1"

print("create Place city_id=\"{}\" user_id=\"{}\" name=\"{}\" description=\"{}\" number_rooms={} number_bathrooms={} max_guest={} price_by_night={} latitude={} longitude={}".format(city_id, user_id, place_name.replace(" ", "_"), place_desc.replace(" ", "_"), place_nb_rooms, place_nb_bath, place_max_guests, place_price, place_lat, place_lon))
