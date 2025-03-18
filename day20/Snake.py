from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
	segments:list[Turtle]

	def __init__(self):
		'''Initialize Snake with 3 segments'''
		self.segments = []
		self.__create_snake()

		self.head = self.segments[0]
		self.tail = self.segments[-1]

		self.head.color("red") ################ check
		self.tail.color("blue") ################ check

	def __create_segment(self):
		new_segment = Turtle("square")
		new_segment.color("white")
		new_segment.penup()
		return new_segment

	def __create_snake(self):
		for position in STARTING_POSITIONS:		
			new_segment = self.__create_segment()
			new_segment.goto(position)
			self.segments.append(new_segment)

	# Basic Movement Methods

	def __update_body(self):
		'''Make the snake body follow the head'''
		for seg_num in range(len(self.segments)-1, 0, -1):
			new_x = self.segments[seg_num-1].xcor()
			new_y = self.segments[seg_num-1].ycor()
			self.segments[seg_num].goto(new_x, new_y)   

	def move(self):
		'''Move the snake head forward by 20 steps'''
		self.__update_body()
		self.head.forward(20)

	#  Snake Controls

	def up(self):
		if self.head.heading() != DOWN:
			self.head.setheading(UP)
	def down(self):
		if self.head.heading() != UP:
			self.head.setheading(DOWN)
	def left(self):
		if self.head.heading() != RIGHT:		
			self.head.setheading(LEFT)
	def right(self):
		if self.head.heading() != LEFT:
			self.head.setheading(RIGHT)

	def eat(self):
		new_segment = self.__create_segment()
		new_segment.goto(self.tail.pos())

		print("Head: ", self.head.pos()) ################ check
		self.tail.color("white") ################ check

		self.segments.append(new_segment)
		self.tail = self.segments[-1]
		self.tail.color("blue") ################ check
		