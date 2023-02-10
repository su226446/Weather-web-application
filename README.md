# Zipcode App

Enter the city name and output the zipcode of this city


Build the docker image:
    
    cd zipcode-app
    docker build -t zipcode-app .

Run the docker container:
    
    docker run -p 5001:5000 zipcode-app
    
<img width="417" alt="WechatIMG473" src="https://user-images.githubusercontent.com/62046854/217986257-8e0f5f48-ae86-43db-98a6-050b14ed7349.png">
    

# Weather App

Enter the city name and output the weather of the city


Build the docker image:

    cd weather-app
    docker build -t weather-app .

Run the docker container:
    
    docker run -p 5002:5000 weather-app
    
 
<img width="468" alt="WechatIMG472" src="https://user-images.githubusercontent.com/62046854/217986285-b5cc70dd-3dd3-42ad-b4ed-2b03762a0a45.png">


# Integration - connect two services

client.py is used to connect these two microservices. 
It takes a zipcode as input and returns the weather for that zipcode.
