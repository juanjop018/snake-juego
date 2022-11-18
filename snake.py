from turtle import Turtle #Importa la librertia Turtle.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)] #Guarda las direcciones dentro de una variable.
MOVE_DISTANCE = 20 #le da movimiento del objeto.
UP = 90 #le da el giro al objeto hacia arriba.
DOWN = 270 #le da el giro al objeto hacia abajo.
LEFT = 180 #le da el giro al objeto hacia izquierda.
RIGHT = 0 #le da el giro al objeto hacia derecha.

class Snake: 

    def __init__(self): 
        self.segments = [] #Guarda cada segmento.
        self.create_snake() #crea el objeto "snake".
        self.head = self.segments[0] #Guarda los 2 anteriores datos dentro del objeto.

    def create_snake(self): #
        for position in STARTING_POSITIONS: 
            self.add_segment(position) #Le da la posicion inicial al objeto.

    def add_segment(self, position): 
        new_segment = Turtle("square") #Le da deficion a la figura derl objeto.
        new_segment.color("white") #Le color del objeto.
        new_segment.penup() #Elimina el objeto.
        new_segment.goto(position) # Define la posicion del objeto.
        self.segments.append(new_segment) #Agrega todo lo anterior al objeto.

    def extend(self): #Le da la extencion de serpiente.
        self.add_segment(self.segments[-1].position()) #Le da un segmento a la cola de la serpiente.

    def move(self): #Le da el movimiento.
        for seg_num in range(len(self.segments)- 1, 0, -1): #La cantidad de segmentos que hay.
            new_x = self.segments[seg_num -1].xcor() #Agrega nuevos segmentos en los ejes x,y.
            new_y = self.segments[seg_num -1].ycor() #Agrega nuevos segmentos en los ejes x,y.
            self.segments[seg_num].goto(new_x,new_y) #Da el movimientos a los segmentos en los ejes x,y.
        self.head.forward(MOVE_DISTANCE) #Mueve la cabeza junto a los segmentos.

    def up(self): #Para que se mueva hacia arriba.
        if self.head.heading() != DOWN: 
            self.head.setheading(UP) 

    def down(self): #Para que se mueva hacia abajo.
        if self.head.heading() != UP: 
            self.head.setheading(DOWN) 

    def left(self): #Para que se mueva hacia la izquierda.
        if self.head.heading() != RIGHT: 
            self.head.setheading(LEFT) 

    def right(self): #Para que se mueva hacia la derecha.
        if self.head.heading() != LEFT: 
            self.head.setheading(RIGHT) 