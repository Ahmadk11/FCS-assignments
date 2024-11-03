#Project
class DeliverySystem:
    def __init__(self):
        self.drivers = {}
        self.cities = {}
        self.driver_id_counter = 1

    def add_driver(self, name, start_city):
        if start_city not in self.cities:
            add_city = input(f"{start_city} is not available. Do you want to add it to the database? (yes/no): ").strip().lower()
            if add_city == 'yes':
                self.add_city(start_city, [])
            else:
                print("Driver not added. Invalid start city.")
                return

        worker_id = f"ID{self.driver_id_counter:03}"
        self.drivers[worker_id] = {'name': name, 'start_city': start_city}
        print(f"Driver {name} added with ID {worker_id} from {start_city}.")
        self.driver_id_counter += 1

    def view_drivers(self):
        if not self.drivers:
            print("No drivers available.")
            return
        print("Drivers:")
        for worker_id, info in self.drivers.items():
            print(f"{worker_id}, {info['name']}, {info['start_city']}")

    def check_similar_drivers(self, start_city):
        similar_drivers = [info['name'] for info in self.drivers.values() if info['start_city'] == start_city]
        if similar_drivers:
            print(f"{start_city}: {', '.join(similar_drivers)}")
        else:
            print(f"No drivers found starting from {start_city}.")

    def add_city(self, city_name, reachable_cities):
        self.cities[city_name] = reachable_cities
        print(f"City {city_name} added with reachable cities: {', '.join(reachable_cities)}.")

    def view_cities(self):
        if not self.cities:
            print("No cities available.")
            return
        print("Cities (sorted Z to A):")
        for city in sorted(self.cities.keys(), reverse=True):
            print(city)

    def search_city(self, key):
        found_cities = [city for city in self.cities.keys() if key in city]
        if found_cities:
            print(f"Cities containing key {key}: {', '.join(found_cities)}")
        else:
            print(f"No cities found containing the key '{key}'.")

    def print_neighboring_cities(self, city_name):
        if city_name in self.cities:
            reachable = self.cities[city_name]
            print(f"Neighboring cities from {city_name}: {', '.join(reachable)}")
        else:
            print(f"{city_name} is not available in the database.")

    def print_drivers_delivering_to_city(self, city_name):
        if city_name not in self.cities:
            print(f"{city_name} is not available in the database.")
            return
        
        delivering_drivers = []
        for driver in self.drivers.values():
            if driver['start_city'] == city_name or city_name in self.cities.get(driver['start_city'], []):
                delivering_drivers.append(driver['name'])

        if delivering_drivers:
            print(f"Drivers delivering to {city_name}: {', '.join(delivering_drivers)}")
        else:
            print(f"No drivers found delivering to {city_name}.")

    def drivers_menu(self):
        while True:
            print("\nDrivers Menu:")
            print("1. View All Drivers")
            print("2. Add a Driver")
            print("3. Check Similar Drivers")
            print("4. Go Back to Main Menu")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.view_drivers()
            elif choice == '2':
                name = input("Enter driver name: ")
                start_city = input("Enter start city: ")
                self.add_driver(name, start_city)
            elif choice == '3':
                start_city = input("Enter the starting city to check for similar drivers: ")
                self.check_similar_drivers(start_city)
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def cities_menu(self):
        while True:
            print("\nCities Menu:")
            print("1. Show Cities")
            print("2. Search City")
            print("3. Print Neighboring Cities")
            print("4. Print Drivers Delivering to City")
            print("5. Go Back to Main Menu")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.view_cities()
            elif choice == '2':
                key = input("Enter a key to search for cities: ")
                self.search_city(key)
            elif choice == '3':
                city_name = input("Enter city name to find neighboring cities: ")
                self.print_neighboring_cities(city_name)
            elif choice == '4':
                city_name = input("Enter city name to find drivers delivering there: ")
                self.print_drivers_delivering_to_city(city_name)
            elif choice == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    def main_menu(self):
        while True:
            print("\nHello! Please enter:")
            print("1. To go to the drivers’ menu")
            print("2. To go to the cities’ menu")
            print("3. To exit the system")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.drivers_menu()
            elif choice == '2':
                self.cities_menu()
            elif choice == '3':
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    system = DeliverySystem()
    system.main_menu()