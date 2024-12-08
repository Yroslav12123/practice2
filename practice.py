superheroes = {
    'batman': 'The dark knight!',
    'Wonder Women': 'The Amazon Princess'
}

def guess_hero(superhero):
     text = superheroes.get(superhero, 'unknown')
     print(text)
guess_hero('batman')\

def guess_hero(superhero):
    match superhero:
        case 'batman':
            print('The dark knight!')
        case 'Wonder Woman':
            print('The Amazon Princess')
        case _:
            print('unknown')
result = guess_hero(4)
print(result)

def http_error(code):
    match code:
        case 400:
            return "bad request"
        case 401 | 403:
            return "Not Allowed"
        case 404:
            return "Not Found"
        case 418:
            return "Im a teapot"
        case _:
            return "somethings wrong with the internet connection"
res_400 = http_error(400)
print('400', res_400)
res_500 = http_error(500)
print('500', res_500)
res_418 = http_error(418)
print('418', res_418)
res_401 = http_error(401)
print('401', res_401)
res_403 = http_error(403)
print('403', res_403)

def procces_data(data_size):
    match data_size:
        case 0:
            print('theres not data at all')
        case n if n < 10:
            print('theres some data, but not enough')
        case n if 10 <= n <=100:
            print('data avalible but not enough')
        case n:
            print('enough data, size:', n)

procces_data(0)
procces_data(7)
procces_data(11)
procces_data(1000)
from enum import IntEnum

class action(IntEnum):
    START = 0
    MIGRATE = 1

def start():
    print('starting')

def migrate():
    print('migrating')

def run_action(action):
    match action:
        case action.START:
            start()
        case action.MIGRATE:
            migrate()
        case _:
            print('unknown command')
run_action(action.MIGRATE)
run_action(action.START)

from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

print(Point(2, 3))

def comment_point(point):
    match point:
        case Point(0, 0):
            print('point at the center!')
        case Point(0, y):
            print("On x axis, y =", y)
        case _:
            print('not a point')
comment_point(123)
comment_point(Point(0, 7))