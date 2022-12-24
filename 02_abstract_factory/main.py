from factory.factory_creator import FactoryCreator

def main():
    factoryCreator = FactoryCreator()
    
    intelFactory = factoryCreator.create_factory("intel")
    amdFactory = factoryCreator.create_factory("amd")

    for factory in [intelFactory,amdFactory]:
        cpu = factory.create_processor()
        motherboard = factory.create_motherboard()
        fan = factory.create_fan()

        print(f'Socket Type Product CPU  = {cpu.get_socket_type()}')
        print(f'Socket Type Product Motherboard  = {motherboard.get_socket_type()}')
        print(f'Socket Type Product Fan  = {fan.get_socket_type()}')


if __name__ == '__main__':
    main()