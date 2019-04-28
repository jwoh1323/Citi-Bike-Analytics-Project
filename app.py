import urllib.request
import os
import time



def percentage(a, b, c):

	per = 100.0 * a * b / c

	if per > 100:

		per = 100

	print('%.2f%%' % per)



#https://s3.amazonaws.com/tripdata/201306-citibike-tripdata.zip

url_1 = "https://s3.amazonaws.com/tripdata/"

url_2 = "-citibike-tripdata"

extension = ".zip"



for year in range(2013, 2014):

    for month in range(7, 13):

        url = url_1 + str(year) + str(month).zfill(2) + url_2 + extension

        filename = "citibike-tripdata"+ str(year) + str(month).zfill(2) + extension

        path = os.path.join("/Users/jwoh1/Desktop/Data Analytics Bootcamp/Homework/15/Resoruces", filename)

        print(url)

        urllib.request.urlretrieve(url, path, percentage)

        time.sleep(5)

