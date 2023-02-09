# Zipcode App

Enter the city name and output the zipcode of this city


Build the docker image:
    
    cd zipcode-app
    docker build -t zipcode-app .

Run the docker container:
    
    docker run -p 5001:5000 zipcode-app
    

# Weather App

Enter the city name and output the weather of the city


Build the docker image:

    cd weather-app
    docker build -t weather-app .

Run the docker container:
    
    docker run -p 5002:5000 weather-app

#Integration - connect two services

client.py is used to connect these two microservices. 
It takes a zipcode as input and returns the weather for that zipcode.


## Output

### build images and run containers



### run client.py




