import grpc
import sys
from proto import restaurant_pb2
from proto import restaurant_pb2_grpc
from concurrent import futures

RESTAURANT_ITEMS_FOOD = ["chips", "fish", "burger", "pizza", "pasta", "salad"]
RESTAURANT_ITEMS_DRINK = ["water", "fizzy drink", "juice", "smoothie", "coffee", "beer"]
RESTAURANT_ITEMS_DESSERT = ["ice cream", "chocolate cake", "cheese cake", "brownie", "pancakes", "waffles"]


class Restaurant(restaurant_pb2_grpc.RestaurantServicer):

    # Logic goes here
    def FoodOrder(self, request, context):
        if all(x in RESTAURANT_ITEMS_FOOD for x in request.items):
            return restaurant_pb2.RestaurantResponse(orderID=request.orderID, status='ACCEPTED')
        else:
            return restaurant_pb2.RestaurantResponse(orderID=request.orderID, status='REJECTED')

    def DrinkOrder(self, request, context):
        if all(x in RESTAURANT_ITEMS_DRINK for x in request.items):
            if restaurant_pb2.RestaurantResponse.Status.ACCEPTED:
                return restaurant_pb2.RestaurantResponse(orderID=request.orderID, status='ACCEPTED')
        else:
            return restaurant_pb2.RestaurantResponse(orderID=request.orderID, status='REJECTED')

    def DessertOrder(self, request, context):
        if all(x in RESTAURANT_ITEMS_DESSERT for x in request.items):
            return restaurant_pb2.RestaurantResponse(orderID=request.orderID, status='ACCEPTED')
        else:
            return restaurant_pb2.RestaurantResponse(orderID=request.orderID, status='REJECTED')


def serve():
    # Logic goes here
    # Remember to start the server on localhost and a port defined by the first command line argument
    port = sys.argv[1]
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    restaurant_pb2_grpc.add_RestaurantServicer_to_server(Restaurant(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
