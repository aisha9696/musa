class Database:
    cars = [
        {
            'id': 1,
            'make': 'Mercedes Benz',
            'year': '2002',
            'price': '6000',
            'image': 'https://s.aolcdn.com/commerce/autodata/images/20MBGEA1.jpg',
            'description': 'C230 Sports Coupe, a car designed to attract first-time '
                           'Mercedes buyers with its combination of style, space, '
                           'and a very complete equipment package',
            'contacts': 'Please contact by email sale@carsale.com or phone 555 555 555',
        },
        {
            'id': 2,
            'make': 'BMW',
            'year': '2022',
            'price': '35000',
            'image': 'https://avatars.mds.yandex.net/get-verba/1540742/2a00000180d7fa047e2e09e71e665301c310/cattouchret',
            'description': 'BMW M3',
            'contacts': 'Please contact by email sale@carsale.com or phone 555 555 555',
        },
        {
            'id': 3,
            'make': 'Subaru',
            'year': '2004',
            'price': '5000',
            'image': 'https://a.d-cd.net/9IxdNGiurR4XMLM196S6Um8DFho-1920.jpg',
            'description': 'Subaru Forester (SG)',
            'contacts': 'Please contact by email sale@carsale.com or phone 555 555 555',
        },
    ]

    @classmethod
    def add_car(cls, car):
        cls.cars.append(car)

    @classmethod
    def find_by_id(cls, id):
        for car in cls.cars:
            if car["id"] == id:
                return car
