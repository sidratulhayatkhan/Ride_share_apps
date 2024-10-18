from ride import Ride,RideRequest,RideMatching,RideSharing
from user import Rider,Driver
from vehicle import Car,Bike

niye_jao= RideSharing("Niye Jao")
rahim = Rider("Rahim Uddin","rahim1@gmail.com",56743,"Mohakhali",1200)
niye_jao.add_rider(rahim)
kolimuddin=Driver("Kolim Uddin","kolimuddin@gmail.com",452114,"Gulshan")
niye_jao.add_driver(kolimuddin)
rahim.request_ride(niye_jao,"Uttara","car")

kolimuddin.reach_destination(rahim.current_ride)
# print(niye_jao)
rahim.show_current_ride()