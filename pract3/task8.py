import matplotlib.pyplot as plt
import csv

class Star(object):
    """about stars"""
    count_star = 0
    def __init__(self, number, name, x_cord, y_cord, radius, descript):
        """Constructor"""
        Star.count_star += 1
        self.__number = number
        self.__name = name
        self.__x_cord = x_cord
        self.__y_cord = y_cord
        self.__radius = radius
        self.__descript = descript

    def get_name(self):
        return self.__name
    def set_name(self, n):
        self.__name = n
    def get_x_cord(self):
        return self.__x_cord
    def get_y_cord(self):
        return self.__y_cord
    def get_radius(self):
        return self.__radius
    def set_radius(self, r):
        self.__radius = r
    def get_descript(self):
        return self.__descript
    def set_descript(self, d):
        self.__descript = d

with open('data/Planets.csv', encoding='utf8') as f:
    spisok = list(csv.reader(f, delimiter='\n'))

def draw(stars):
    # print(Star.count_star)
    x_cords = []
    y_cords = []
    s = []
    fig, axs = plt.subplots(figsize=(12, 8))
    fig.patch.set_facecolor('black')
    for i in range(len(stars)):
        x_cords.append(stars[i].get_x_cord())
        y_cords.append(stars[i].get_y_cord())
        s.append(stars[i].get_radius() * 0.0009)
    axs.scatter(x_cords, y_cords, c=['0.7'], s=s, alpha = 0.7)
    axs.axis('off')
    plt.title('Elite (1984)', fontsize=15)
    for i in range(len(stars)):
        plt.text(stars[i].get_x_cord(), stars[i].get_y_cord(), stars[i].get_name(), color='white', fontsize=stars[i].get_radius()*0.0014, alpha=0.48)

    plt.show()


def main():
    stars = []
    for i in range(len(spisok)):
        if spisok[i][0][0] == '#':
            number = int(spisok[i][0][1:spisok[i][0].find('.')])
            name = str(spisok[i][0][spisok[i][0].find('.')+2:spisok[i][0].find('(')-1])
            x_cord = int(spisok[i][0][spisok[i][0].find('(')+1:spisok[i][0].find(',')])
            y_cord = int(spisok[i][0][spisok[i][0].find(',') + 1:spisok[i][0].find(')')])
            radius = int(spisok[i][0][spisok[i][0].rfind('Radius')+7:spisok[i][0].rfind('km')-1])

        elif (i+1)%3==0:
            descript = spisok[i][0]
            #print(number, name, x_cord, y_cord, radius, descript)
            new_star = Star(number, name, x_cord, y_cord, radius, descript)
            stars.append(new_star)
    draw(stars)

if __name__ == '__main__':
    main()