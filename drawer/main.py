from src.image import Image, to_color
from src.vector import Vector2D as Vector
from src.shapes import Line, Circle

def generate_img_1a(C=400):
    '''Image "Linie pola ekektr wokół punktowego ładunku dodatniego"'''
    image = Image((C*2, C*2), line_width=3)
    image.draw_circle(Circle((C, C), int(C*0.4)), fill=[190,0,0], width=10)
    image.draw_line(Line((C,int(C+(C*0.1))),(C,int(C-(C*0.1)))), fill=[190,0,0])
    image.draw_line(Line((int(C+(C*0.1)),C),(int(C-(C*0.1)),C)), fill=[190,0,0])
    for deg in range(0, 360, 360//12):
        prevector = Vector.from_rotation((C,C), deg, int(C*0.95))
        prevector = Vector.from_reversed(prevector)
        prevector.scale(0.45)
        vector = Vector.from_reversed(prevector)
        vector.round()
        image.draw_vector(vector)
    image.save('img/img_1a.png')

def generate_img_1b(C=400):
    '''Image "Linie pola ekektr wokół punktowego ładunku ujemnego"'''
    image = Image((C*2, C*2), line_width=3)
    image.draw_circle(Circle((C, C), int(C*0.4)), fill=[0,0,190], width=10)
    image.draw_line(Line((int(C+(C*0.1)),C),(int(C-(C*0.1)),C)), fill=[0,0,190])
    for deg in range(0, 360, 360//12):
        prevector = Vector.from_rotation((C,C), deg, int(C*0.95))
        vector = Vector.from_reversed(prevector)
        vector.scale(0.45)
        vector.round()
        image.draw_vector(vector)
    image.save('img/img_1b.png')

def generate_img_2a(C=400):
    '''Image "Linie pola ekektr wokół 2 punktowych ładunków różnoimiennych"'''
    image = Image((C*4, C*2), line_width=3)
    # pos
    image.draw_circle(Circle((C, C), int(C*0.4)), fill=[190,0,0], width=10)
    image.draw_line(Line((C,int(C+(C*0.1))),(C,int(C-(C*0.1)))), fill=[190,0,0])
    image.draw_line(Line((int(C+(C*0.1)),C),(int(C-(C*0.1)),C)), fill=[190,0,0])
    # neg
    image.draw_circle(Circle((3*C, C), int(C*0.4)), fill=[0,0,190], width=10)
    image.draw_line(Line((int(3*C+(C*0.1)),C),(int(3*C-(C*0.1)),C)), fill=[0,0,190])
    # straight vectors
    image.draw_vector(Vector((int(C*1.5), C)            ,(int(C*0.4), 0)))
    image.draw_vector(Vector((int(C*1.5), int(C*1.2))   ,(int(C*0.4), 0)))
    image.draw_vector(Vector((int(C*1.5), int(C*0.8))   ,(int(C*0.4), 0)))
    image.draw_vector(Vector((int(C*2.1), C)            ,(int(C*0.4), 0)))
    image.draw_vector(Vector((int(C*2.1), int(C*1.2))   ,(int(C*0.4), 0)))
    image.draw_vector(Vector((int(C*2.1), int(C*0.8))   ,(int(C*0.4), 0)))
    # slightly curved vectors
    image.draw_vector(Vector((int(C*1.5), int(C*1.4))   ,(int(C*0.4), int(C*0.05))))
    image.draw_vector(Vector((int(C*2.1), int(C*1.45))  ,(int(C*0.4), int(C*-0.05))))
    image.draw_vector(Vector((int(C*1.5), int(C*0.6))   ,(int(C*0.4), int(C*-0.05))))
    image.draw_vector(Vector((int(C*2.1), int(C*0.55))  ,(int(C*0.4), int(C*0.05))))
    # curved 3-part vectors
    image.draw_vector(Vector((int(C*1.1), int(C*1.5))   ,(int(C*0.4), int(C*0.1))))
    image.draw_vector(Vector((int(C*1.8), int(C*1.65))  ,(int(C*0.4), 0)))
    image.draw_vector(Vector((int(C*2.5), int(C*1.6))   ,(int(C*0.4), int(C*-0.1))))
    image.draw_vector(Vector((int(C*1.1), int(C*0.5))   ,(int(C*0.4), int(C*-0.1))))
    image.draw_vector(Vector((int(C*1.8), int(C*0.35))  ,(int(C*0.4), 0)))
    image.draw_vector(Vector((int(C*2.5), int(C*0.4))   ,(int(C*0.4), int(C*0.1))))
    image.save('img/img_2a.png')

def generate_img_2b(C=400):
    '''Image "Linie pola ekektr wokół 2 punktowych ładunków jednoimiennych"'''
    image = Image((C*4, C*2), line_width=3)
    # left
    image.draw_circle(Circle((C, C), int(C*0.4)), fill=[190,0,0], width=10)
    image.draw_line(Line((C,int(C+(C*0.1))),(C,int(C-(C*0.1)))), fill=[190,0,0])
    image.draw_line(Line((int(C+(C*0.1)),C),(int(C-(C*0.1)),C)), fill=[190,0,0])
    # right
    image.draw_circle(Circle((3*C, C), int(C*0.4)), fill=[190,0,0], width=10)
    image.draw_line(Line((3*C,int(C+(C*0.1))),(3*C,int(C-(C*0.1)))), fill=[190,0,0])
    image.draw_line(Line((int(3*C+(C*0.1)),C),(int(3*C-(C*0.1)),C)), fill=[190,0,0])
    # vertical
    image.draw_line(Line((2*C, 0),(2*C,2*C)), width=1)
    # vectors
    image.draw_vector(Vector((int(C*1.5), int(C*1.1)),(int(C*0.25), int(C*0.3))))
    image.draw_vector(Vector((int(C*1.5), int(C*0.9)),(int(C*0.25), -int(C*0.3))))
    image.draw_vector(Vector((int(C*1.8), int(C*1.5)),(0, int(C*0.4))))
    image.draw_vector(Vector((int(C*1.8), int(C*0.5)),(0, -int(C*0.4))))
    image.draw_vector(Vector((int(C*2.5), int(C*1.1)),(-int(C*0.25), int(C*0.3))))
    image.draw_vector(Vector((int(C*2.5), int(C*0.9)),(-int(C*0.25), -int(C*0.3))))
    image.draw_vector(Vector((int(C*2.2), int(C*1.5)),(0, int(C*0.4))))
    image.draw_vector(Vector((int(C*2.2), int(C*0.5)),(0, -int(C*0.4))))
    #
    image.draw_vector(Vector((int(C*1.4), int(C*1.25)),(int(C*0.20), int(C*0.40))))
    image.draw_vector(Vector((int(C*1.4), int(C*0.75)),(int(C*0.20), -int(C*0.40))))
    image.draw_vector(Vector((int(C*2.6), int(C*1.25)),(-int(C*0.20), int(C*0.40))))
    image.draw_vector(Vector((int(C*2.6), int(C*0.75)),(-int(C*0.20), -int(C*0.40))))
    #
    image.draw_vector(Vector((int(C*1.2), int(C*1.4)),(int(C*0.1), int(C*0.5))))
    image.draw_vector(Vector((int(C*1.2), int(C*0.6)),(int(C*0.1), -int(C*0.5))))
    image.draw_vector(Vector((int(C*2.8), int(C*1.4)),(-int(C*0.1), int(C*0.5))))
    image.draw_vector(Vector((int(C*2.8), int(C*0.6)),(-int(C*0.1), -int(C*0.5))))
    image.save('img/img_2b.png')

def generate_img_3a(C=400):
    '''Image "Pole elektryczne pomiędzy odładami kondensatora płaskiego"'''
    image = Image((C*2, C*2), line_width=3)
    image.draw_line(Line((int(C*2/3), int(C*0.5)),(int(C*2/3), int(C*1.5))),\
        fill=[190,0,0], width=10)
    image.draw_line(Line((int(C*2/3), C),(int(C*1/3), C)), fill=[190,0,0], width=3)
    image.draw_point((int(C*1/3), int(C)), fill=[190,0,0], width=10)
    image.draw_line(Line((int(C*4/3), int(C*0.5)),(int(C*4/3), int(C*1.5))),\
        fill=[0,0,190], width=10)
    image.draw_line(Line((int(C*4/3), C),(int(C*5/3), C)), fill=[0,0,190], width=3)
    image.draw_point((int(C*5/3), int(C)), fill=[0,0,190], width=10)
    len = 2/3 - 2*(0.75 - 2/3)
    image.draw_vector(Vector((int(C*0.75), int(C*0.6)),(int(C*len), 0)))
    image.draw_vector(Vector((int(C*0.75), int(C*0.8)),(int(C*len), 0)))
    image.draw_vector(Vector((int(C*0.75), int(C*1)),(int(C*len), 0)))
    image.draw_vector(Vector((int(C*0.75), int(C*1.2)),(int(C*len), 0)))
    image.draw_vector(Vector((int(C*0.75), int(C*1.4)),(int(C*len), 0)))
    image.save('img/img_3a.png')

def generate_img_5a(C=400):
    '''Image "Symbol ogólny kondensatora"'''
    image = Image((int(C*2), int(C*2)), line_width=6)
    image.draw_line(Line((int(C*5/6), int(C*0.5)),(int(C*5/6), int(C*1.5))))
    image.draw_line(Line((int(C*7/6), int(C*0.5)),(int(C*7/6), int(C*1.5))))
    image.draw_line(Line((int(C*5/6), int(C*1)),(int(C*1/4), int(C*1))))
    image.draw_line(Line((int(C*7/6), int(C*1)),(int(C*7/4), int(C*1))))
    image.draw_point((int(C*1/4), int(C*1)), width=20)
    image.draw_point((int(C*7/4), int(C*1)), width=20)
    image.save('img/img_5a.png')

def generate_img_5b(C=400):
    '''Image "Symbol kondensatora regulowanego"'''
    image = Image((int(C*2), int(C*2)), line_width=6)
    image.draw_line(Line((int(C*5/6), int(C*0.5)),(int(C*5/6), int(C*1.5))))
    image.draw_line(Line((int(C*7/6), int(C*0.5)),(int(C*7/6), int(C*1.5))))
    image.draw_line(Line((int(C*5/6), int(C*1)),(int(C*1/4), int(C*1))))
    image.draw_line(Line((int(C*7/6), int(C*1)),(int(C*7/4), int(C*1))))
    image.draw_point((int(C*1/4), int(C*1)), width=20)
    image.draw_point((int(C*7/4), int(C*1)), width=20)
    image.draw_vector(Vector((int(C*0.5), int(C*1.5)),(int(C*1), -int(C*1))), width=8)
    image.save('img/img_5b.png')

def generate_img_5c(C=400):
    '''Image "Symbol kondensatora elektrolitycznego"'''
    image = Image((int(C*2), int(C*2)), line_width=6)
    image.draw_line(Line((int(C*5/6), int(C*0.5)),(int(C*5/6), int(C*1.5))))
    image.draw_line(Line((int(C*7/6), int(C*0.5)),(int(C*7/6), int(C*1.5))))
    image.draw_line(Line((int(C*8/6), int(C*0.5)),(int(C*8/6), int(C*1.5))))
    image.draw_line(Line((int(C*7/6), int(C*0.5)),(int(C*8/6), int(C*0.5))))
    image.draw_line(Line((int(C*7/6), int(C*1.5)),(int(C*8/6), int(C*1.5))))
    image.draw_line(Line((int(C*5/6), int(C*1)),(int(C*1/4), int(C*1))))
    image.draw_line(Line((int(C*8/6), int(C*1)),(int(C*7/4), int(C*1))))
    image.draw_point((int(C*1/4), int(C*1)), width=20, fill=[0,0,190])
    image.draw_point((int(C*7/4), int(C*1)), width=20, fill=[190,0,0])
    image.save('img/img_5c.png')

def generate_img_8a(C=400):
    '''Image "Węzeł z pięcioma prądami"'''
    image = Image((int(C*2), int(C*2)), line_width=6, vector_arrow_size=30)
    image.draw_point((C,C), width=20)
    out_param_list = [
        (0 , [190,0,0]),
        (40, [190,0,0]),
        (320, [190,0,0]),
    ]
    in_param_list = [
        (140, [0,20,190]),
        (180, [0,20,190]),
        (220, [0,20,190]),
    ]
    for rotation, arrow_color in out_param_list:
        vector = Vector.from_rotation((C,C), rotation, int(C*0.5))
        vector2 = Vector.from_rotation((C,C), rotation, int(C*0.5))
        vector2.scale(1.3)
        line = Line.from_vector(vector2)
        image.draw_line(line)
        image.draw_vector(vector, arrow_color=arrow_color)
    for rotation, arrow_color in in_param_list:
        vector = Vector.from_rotation((C,C), rotation, int(C*0.5))
        vector = Vector.from_reversed(vector)
        vector.scale(1-(1/1.3))
        vector2 = Vector.from_rotation((C,C), rotation, int(C*0.5))
        vector2.scale(1.3)
        line = Line.from_vector(vector2)
        image.draw_line(line)
        image.draw_vector(vector, arrow_color=arrow_color)
    image.save('img/img_8a.png')


if __name__ == '__main__':
    #generate_img_1a()
    #generate_img_1b()
    #generate_img_2a()
    #generate_img_2b()
    #generate_img_3a()
    #generate_img_5a()
    #generate_img_5b()
    #generate_img_5c()
    generate_img_8a()

    # Templates
    # image.draw_vector(Vector((int(C*1), int(C*1)),(int(C*1), int(C*1))))
    # image.draw_line(Line((int(C*1), int(C*1)),(int(C*1), int(C*1))))
