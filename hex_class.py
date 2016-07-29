import turtle
import math

class Hexagon():
 
    sides = 6
    side_length = 30
    angle = 60
    radius = math.sqrt(side_length ** 2 - (side_length / 2) ** 2)

    def __init__(self, turtle, position): 
        self.a = turtle
        self.start_hex = [position[0], position[1]] #set start point of the hexagon
        self.played = False
        
        self.centre_x = self.start_hex[0] + Hexagon.radius
        self.centre_y = self.start_hex[1] + Hexagon.side_length / 2
        self.centre = self.centre_x, self.centre_y
        
        self.draw_hexagon()
        
    def draw_hexagon(self): #draw one hexagon
        self.a.goto(self.start_hex)
        self.a.pendown()
        self.a.setheading(270) #begins facing 'south'
        for i in range(Hexagon.sides):
            self.a.fd(Hexagon.side_length)
            self.a.lt(Hexagon.angle)
        self.a.penup()
   
    def is_selected(self, click):  #checks if clicked within radius
        num1 = (click[0] - self.centre_x) ** 2
        num2 = (click[1] - self.centre_y) ** 2
        distance = math.sqrt(num1 + num2)
        return distance <= Hexagon.radius
    
    def fill_cell(self, moves): #draws filled hexagon, colour determined by turn
        """if moves / 2 == 0:
            self.a.color("black")
        else:
            self.a.color("gray")"""
        self.a.color("black")
        self.a.begin_fill()
        self.draw_hexagon()
        self.a.end_fill()
        self.played = True
            

class Board():
    
    diameter = Hexagon.radius * 2

    def __init__ (self, turtle, board_size, starting_position):
        self.a = turtle
        self.board_size = board_size
        self.start = starting_position
        self.moves = 0
        self.board = []
        self.draw_board()
    
    def draw_board(self):
        for i in range(self.board_size):
            row = []
            for j in range(self.board_size):
                row.append(Hexagon(self.a, self.start))
                self.start[0] += Board.diameter
            self.start[0] -= Board.diameter * (self.board_size - 1) + Hexagon.radius
            self.start[1] -= Hexagon.side_length + (Hexagon.side_length / 2)
            self.a.goto(self.start)
            self.board.append(row)

    def select(self, x, y):
        print("hi")
        for row in self.board:
            for cell in row:
                if cell.is_selected((x, y)) is True and not cell.played:
                    cell.fill_cell(self.moves)
                    self.moves += 1

def main():   
    screen = turtle.Screen()
    a = turtle.Turtle()
    a.speed(0)     

    board_size = 5
    starting_position = [0, 0]
    board = Board(a, board_size, starting_position)
    
    screen.onclick(board.select)
    
    turtle.done()

main()