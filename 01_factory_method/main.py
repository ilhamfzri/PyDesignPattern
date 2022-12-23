from transportation import FactoryTransportation

def main():
    transportation = FactoryTransportation()

    car = transportation.create_transporation("car")
    motorcycle = transportation.create_transporation("motorcycle")
    truck = transportation.create_transporation("truck")

    distance = 40
    cost_using_car = car.calculate_cost(distance)
    cost_using_motorcycle = motorcycle.calculate_cost(distance)
    cost_using_truck = truck.calculate_cost(distance)

    print(f'Cost using motorcycle = {cost_using_motorcycle}')
    print(f'Cost using car = {cost_using_car}')
    print(f'Cost using truck = {cost_using_truck}')

    print(f'Maximum car payload weight = {car.get_max_weight()}')
    print(f'Maximum motorcycle payload weight = {motorcycle.get_max_weight()}')
    print(f'Maximum truck payload weight = {truck.get_max_weight()}')

    print(f'Maximum car payload dimension (w,l,h) = {car.get_max_dimension()}')
    print(f'Maximum motorcycle payload dimension (w,l,h) = {motorcycle.get_max_dimension()}')
    print(f'Maximum truck payload dimension (w,l,h)  = {truck.get_max_dimension()}')

if __name__ == '__main__':
    main()