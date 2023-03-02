import pygeoip

# Open the GeoIP database
geoip = pygeoip.GeoIP('GeoLiteCity.dat')

# Prompt the user to enter the target IP address
target_ip = input("Enter the IP address of the target: ")

# Look up the location information for the target IP address
record = geoip.record_by_addr(target_ip)

# Print the location information for the target IP address
if record:
    country = record.get('country_name')
    city = record.get('city')
    country_code = record.get('country_code')
    continent = record.get('continent')

    print("IP address: {}".format(target_ip))
    print("Country: {}".format(country))
    print("City: {}".format(city))
    print("Country code: {}".format(country_code))
    print("Continent: {}".format(continent))

else:
    print("The IP address could not be found in the database.")

# Close the GeoIP database
geoip.close()
