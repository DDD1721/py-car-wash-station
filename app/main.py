class Car:
    def __init__(self, comfort_class, clean_mark, brand):
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self, distance_from_city_center, clean_power, average_rating, count_of_ratings):
        self.distance_from_city_center = distance_from_city_center
        self.clean_power = clean_power
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars):
        income = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                wash_cost = self.calculate_washing_price(car)
                income += wash_cost
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car):
        return round(
            car.comfort_class * (self.clean_power - car.clean_mark) * self.average_rating / self.distance_from_city_center,
            1
        )

    def wash_single_car(self, car):
        if car.clean_mark < self.clean_power:
            car.clean_mark = self.clean_power

    def rate_service(self, new_rating):
        total_rating = self.average_rating * self.count_of_ratings
        total_rating += new_rating
        self.count_of_ratings += 1
        self.average_rating = round(total_rating / self.count_of_ratings, 1)


# Example usage
bmw = Car(3, 3, 'BMW')
audi = Car(4, 9, 'Audi')
mercedes = Car(7, 1, 'Mercedes')

wash_station = CarWashStation(6, 8, 3.9, 11)

income = wash_station.serve_cars([bmw, audi, mercedes])
print(income)  # Expected output: 41.7
print(bmw.clean_mark)  # Expected output: 8
print(audi.clean_mark)  # Expected output: 9
print(mercedes.clean_mark)  # Expected output: 8

ford = Car(2, 1, 'Ford')
wash_cost = wash_station.calculate_washing_price(ford)
print(wash_cost)  # Expected output: 9.1
print(ford.clean_mark)  # Expected output: 1

wash_station.rate_service(5)
print(wash_station.count_of_ratings)  # Expected output: 12
print(wash_station.average_rating)  # Expected output: 4.0
