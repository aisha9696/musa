from .base import BaseController

from app.db import Database


class PagesController(BaseController):
    def home(self):
        body = '<h1>Cars Dealership</h1>'

        for car in Database.cars:
            body += (f'<div style="display: flex">'
                     f'<div style="margin-bottom: 20px">'
                     f'<img src="{car["image"]}" width="300" height="200" alt="car"></div>'
                     f'<p style="margin-top: 60px; margin-left: 30px;">'
                     f'<a href="/car?id={car["id"]}">'
                     f'{car["make"]} ({car["year"]})</a><br>'
                     f'${car["price"]}</p>'
                     f'</div>')

        body += f'<br><a href=/new>Place new advertisement</a>'

        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)

    def get_car(self):
        car = Database.find_by_id(self.request.post_id)
        body = (f'<h1>View advertisement</h1>'
                f'<img src="{car["image"]}" width="300" height="200" alt="car"><br>'
                f'${car["price"]}<br>'
                f'<b>Make: </b>{car["make"]}<br>'
                f'<b>Year: </b>{car["year"]}<br>'
                f'<b>Description: </b>{car["description"]}<br>'
                f'<b>Contacts: </b>{car["contacts"]}<br>'
                f'<a href="/">Return to home page</a>')
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body(body)

    def create_car_post(self):
        if self.request.method == 'GET':
            with open('static/create_car_post.html', 'r') as f:
                body = f.read()

            self.response.add_header('Content-Type', 'text/html')
            self.response.set_body(body)

        else:
            print(777, self.request.body)

            car = {
                'id': Database.cars[-1]['id'] + 1,
                'make': self.request.body['make'][0],
                'year': self.request.body['year'][0],
                'price': self.request.body['price'][0],
                'image': self.request.body['image'][0],
                'description': self.request.body['description'][0],
                'contacts': self.request.body['contacts'][0],
            }

            Database.add_car(car)

            self.response.set_status(301)
            self.response.add_header('Location', '/')

    def about(self):
        self.response.add_header('Content-Type', 'text/html')
        self.response.set_body('<h1>This is about</h1>')
