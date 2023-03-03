# GeoIP-Script-Python

This is a script that identifies country, city, country code and continent by IP address with Python

In this script, we first import the pygeoip module and open the GeoLiteCity.dat file using the pygeoip.GeoIP() constructor. We then prompt the user to enter the target IP address using the input() function.

We use the record_by_addr() method of the GeoIP object to look up the location information for the target IP address. If the address is found in the database, we extract the country, city, country code, and continent name from the record object and print them out. If the address is not found, we print an error message.

Finally, we close the GeoIP object using the close() method to free up system resources.

We need to add the GeoLiteCity.dat file to the folder. 

The file is added here as well and can be downloaded.
