# Factory Method

*Factory Method* adalah salah satu dari *creational design pattern* yang dimana kita membuat objek tidak secara langsung tetapi melalui sebuah *interface* atau *class*. 

## Kapan Factory Method Digunakan ?
Sebagai contoh kasusnya, misal kita membuat sebuah aplikasi untuk jasa pengantaran barang yang dimana pada saat itu hanya menggunakan kendaraan bermotor saja sebagai mode transportasinya. Tetapi seiring berkembangnya bisnis dan pasar ternyata dibutuhkan mode transportasi lainnya, seperti menggunakan mobil dan juga truk.

Namun, karena kita tidak antisipasi hal ini pada akhirnya kita harus mengubah banyak sekali perubahan sesuai dengan bisnis logic-nya seperti perhitungan biaya pengiriman, maksimal berat barang yang dapat dibawa, dsb. Dimana kasus terburuknya kita harus implementasi banyak kondisi if,else untuk setiap variant objek yang berlaku. Kelemahan lainnya adalah setiap ada penambahan mode transportasi baru maka diperlukan perubahan yang signifikan lagi dan membuat code base menjadi semakin kompleks dan sangat sulit sekali pada saat debuging pada saat terjadi error. 

![alt text](/01_factory_method/img/factory-method-01.png)

Salah satu solusi yang dapat digunakan adalah dengan menerapkan *factory method*. Konsepnya adalah, pertama kita pisahkan terlebih dahulu objek yang memiliki business logic yang mirip, pada kasus ini adalah variant dari mode transportasi yaitu, `Motorcycle`, `Car` dan `Truck`. 
Setiap objek dinyatakan dalam bentuk class yang dimana masing-masing memiliki interface fungsi yang sama artinya, jika menambahkan fungsi baru di `Motorcycle` maka wajib menambahkan juga di `Car` ataupun `Truck`. Dengan cara ini juga kita telah menerapkan *Sin­gle Respon­si­bil­i­ty Prin­ci­ple* yang dimana dapat lebih memudahkan kita pada saat proses testing.

Tahap selanjutnya adalah pembuatan `factory` class. `Factory` berfungsi untuk menghasilkan variant objek. Pada kasus ini direpresentasikan oleh `Transporation` class yang memiiki fungsi `create_transporation()` untuk menghasilkan objek.

## Implementasi Python
Berikut adalah implementasi *factory method* menggunakan python.

### Car Transporation
```python
# transporation/car.py

from typing import List

class CarTransportation:
    def __init__(self):
        self.PRICE_PER_KM = 200
        self.MAX_WEIGHT = 50
        self.MAX_WIDTH_IN_CM = 30
        self.MAX_LENGTH_IN_CM = 30
        self.MAX_HEIGHT_IN_CM = 30

    def calculate_cost(self, distance_in_km:int) -> int:
        cost = self.PRICE_PER_KM * distance_in_km
        return cost
    
    def get_max_weight(self) -> int:
        return self.MAX_WEIGHT

    def get_max_dimension(self) -> List[int]:
        return [self.MAX_WIDTH_IN_CM, self.MAX_LENGTH_IN_CM, self.MAX_HEIGHT_IN_CM]

```

### Motorcycle Transportation
```python
# transporation/motorcycle.py

from typing import List

class MotorycleTransportation:
    def __init__(self):
        self.PRICE_PER_KM = 75
        self.MAX_WEIGHT = 10
        self.MAX_WIDTH_IN_CM = 10
        self.MAX_LENGTH_IN_CM = 10
        self.MAX_HEIGHT_IN_CM = 10

    def calculate_cost(self, distance_in_km:int) -> int:
        cost = self.PRICE_PER_KM * distance_in_km
        return cost
    
    def get_max_weight(self) -> int:
        return self.MAX_WEIGHT

    def get_max_dimension(self) -> List[int]:
        return [self.MAX_WIDTH_IN_CM, self.MAX_LENGTH_IN_CM, self.MAX_HEIGHT_IN_CM]
```

### Truck Transportation
```python
# transporation/truck.py

from typing import List

class TruckTransportation:
    def __init__(self):
        self.PRICE_PER_KM = 300
        self.MAX_WEIGHT = 100
        self.MAX_WIDTH_IN_CM = 100
        self.MAX_LENGTH_IN_CM = 100
        self.MAX_HEIGHT_IN_CM = 100

    def calculate_cost(self, distance_in_km:int) -> int:
        cost = self.PRICE_PER_KM * distance_in_km
        return cost
    
    def get_max_weight(self) -> int:
        return self.MAX_WEIGHT

    def get_max_dimension(self) -> List[int]:
        return [self.MAX_WIDTH_IN_CM, self.MAX_LENGTH_IN_CM, self.MAX_HEIGHT_IN_CM]
```


###  Factory Transportation
```python
# transporation/__int__.py
from typing import Union
from .motorcycle import MotorycleTransportation
from .car import CarTransportation
from .truck import TruckTransportation

class FactoryTransportation:
    def __init__(self):
        self.transporation_list = {
            "motorcycle": MotorycleTransportation,
            "car": CarTransportation,
            "truck": TruckTransportation
        }

    def create_transporation(self, name:str) -> Union[MotorycleTransportation, CarTransportation, TruckTransportation]:
        if name in self.transporation_list.keys():
            return self.transporation_list[name]()
        else:
            raise Exception('f transportation with {name} name not supported!')
```

###  Main
```python
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
```

## Kelebihan dan Kekurangan Factory Method
[✅] Single Responsibility Principle : Pembuatan objek tersentraliasi dalam satu `factory` class sehingga lebih mudah untuk di-maintain. </br>

[✅] Open/Closed Principle : Kita dapat lebih mudah untuk menambahkan variant objek baru tanpa harus terlalu takut penambahkan  tersebut dapat merusak variant objek yang lain. </br>

[❌] Kode akan semakin kompleks apabila terdapat penambahan banyak variant objek baru karena kita harus menyamakan interface sesuai dengan variant objek yang lain. </br>


