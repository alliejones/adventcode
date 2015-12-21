import re

class Reindeer:
    def __init__(self, name, speed, flying_time, rest_time):
        self.name = name
        self.speed = int(speed)
        self.flying_time = int(flying_time)
        self.rest_time = int(rest_time)
        self.timer = int(flying_time)
        self.state = 'flying'
        self.distance = 0
        self.score = 0

    def tick(self):
        if self.timer == 0:
            if self.state == 'flying':
                self.state = 'resting'
                self.timer = self.rest_time
            else:
                self.state = 'flying'
                self.timer = self.flying_time

        if self.state == 'flying':
            self.distance += self.speed

        self.timer -= 1


def read_input():
    data = []
    with open('ex14-input.txt') as file:
        for line in file:
            matches = re.finditer('(\w+) can fly (\d+) km/s for (\d+) .* (\d+)', line)
            [data.append(m.groups()) for m in matches]
    return data

def create_reindeer(data):
    return [Reindeer(*r) for r in data]

def get_deer_in_lead(reindeer):
    max_dist = max([r.distance for r in reindeer])
    return [r for r in reindeer if r.distance == max_dist]

def race(time):
    for t in xrange(time):
        [r.tick() for r in reindeer]
        for d in get_deer_in_lead(reindeer):
            d.score += 1
    for d in get_deer_in_lead(reindeer):
        d.score += 1

# reindeer = create_reindeer([('Dancer', 16, 11, 162), ('Comet', 14, 10, 127)])
reindeer = create_reindeer(read_input())
race(2503)
print max([r.score for r in reindeer])
