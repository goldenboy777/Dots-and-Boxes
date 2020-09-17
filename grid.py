import pygame


letterX=pygame.image.load('x.png')
letterO=pygame.image.load('o.png')

class Grid:
	def __init__(self):
		self.grid_points=[(100,100), (100,200),(100,300),(100,400),(100,500), 
						  (200,100),(200,200),(200,300),(200,400),(200,500),
						  (300,100),(300,200),(300,300),(300,400),(300,500),
						  (400,100),(400,200),(400,300),(400,400),(400,500),
						  (500,100),(500,200),(500,300),(500,400),(500,500)]
		self.grid_points_value=[[False for x in range(5)] for y in range(5)]
		self.grid=[[0 for x in range(4)] for y in range(4)]
		self.search_dira = [(0,-100),(-100,0),(0,100),(100,0)]
		self.top=[[False for x in range(4)] for y in range(4)]
		self.bottom=[[False for x in range(4)] for y in range(4)]
		self.left=[[False for x in range(4)] for y in range(4)]
		self.right=[[False for x in range(4)] for y in range(4)]
		self.switch=True
		self.player="X"
		#top=8 bottom=4 left=1 right=2
		self.count=0


	def draw(self,surface):
		for points in self.grid_points:
		 pygame.draw.circle(surface, (255,0,0), (points[0],points[1]), 10, 0)

		for y in range(len(self.grid)):
			for x in range(len(self.grid[y])):
				if self.grid[x][y] == 'X':
					surface.blit(letterX,((y+1)*100,(x+1)*100))
				elif self.grid[x][y] == 'O':
					surface.blit(letterO,((y+1)*100,(x+1)*100))

	def is_within_bounds_points(self,x,y):
		return x>=100 and x <= 500 and y>=100 and y<=500


	def walls_value(self,x1,y1,x2,y2):
		print(x1,y1,x2,y2)
		print(self.player)
		
		turn = 0
		if(x1==x2):
			ycor1=min(y1,y2)
			xcor1=x1
			xcor2=xcor1-1
			if(xcor1>=0 and xcor1<=3 and not self.top[xcor1][ycor1]):
				self.top[xcor1][ycor1]=True
			if(xcor2>=0 and xcor2<=3 and not self.bottom[xcor2][ycor1]):
				self.bottom[xcor2][ycor1]=True
			if(xcor1>=0 and xcor1<=3 and self.left[xcor1][ycor1] and self.right[xcor1][ycor1] and self.top[xcor1][ycor1] and self.bottom[xcor1][ycor1] and self.grid[xcor1][ycor1]==0) :
				self.grid[xcor1][ycor1]=self.player
				turn=1
			if( xcor2>=0 and xcor2<=3 and self.left[xcor2][ycor1] and self.right[xcor2][ycor1] and self.top[xcor2][ycor1] and self.bottom[xcor2][ycor1] and self.grid[xcor2][ycor1]==0) :
				self.grid[xcor2][ycor1]=self.player
				turn=1
		if(y1==y2):
			xcor1=min(x1,x2)
			ycor1=y1
			ycor2=ycor1-1
			if(ycor1>=0 and ycor1<=3 and not self.left[xcor1][ycor1]):
				self.left[xcor1][ycor1]=True
			if(ycor2>=0 and ycor2<=3 and not self.right[xcor1][ycor2]):
				self.right[xcor1][ycor2]=True
			if(ycor1>=0 and ycor1<=3 and self.left[xcor1][ycor1] and self.right[xcor1][ycor1] and self.top[xcor1][ycor1] and self.bottom[xcor1][ycor1] and self.grid[xcor1][ycor1]==0) :
				self.grid[xcor1][ycor1]=self.player
				turn=1
			if(ycor2>=0 and ycor2<=3 and self.left[xcor1][ycor2] and self.right[xcor1][ycor2] and self.top[xcor1][ycor2] and self.bottom[xcor1][ycor2] and self.grid[xcor1][ycor2]==0) :
				self.grid[xcor1][ycor2]=self.player
				turn=1


		if turn==1:
		    self.switch=False
		else:
			self.switch=True


		if(self.switch):
			if self.player=='X':
				self.player='O'
			else:
				self.player='X'
				

		self.print_grid()
		


	def check(self,x,y,surface):
		for index, (dirx,diry) in enumerate(self.search_dira):
			if self.is_within_bounds_points(x+dirx,y+diry):
				if self.grid_points_value[(x+dirx)//100-1][(y+diry)//100-1]:
					xx=x+dirx
					yy=y+diry
					pygame.draw.line(surface,(0,0,255),(yy,xx),(y,x),2)
					if self.count==2:
						self.walls_value(xx//100-1,yy//100-1,x//100-1,y//100-1)
						self.reset(surface)
						self.count=0


	def selected(self,x,y,surface):
		for points in self.grid_points:
			if ((x-points[0])*(x-points[0])+(y-points[1])*(y-points[1])) <=20 and not self.grid_points_value[points[1]//100-1][points[0]//100-1]:
				self.count+=1
				pygame.draw.circle(surface, (0,0,255), (points[0],points[1]), 20, 1)
				self.grid_points_value[points[1]//100-1][points[0]//100-1]=True
				self.check(points[1],points[0],surface)
				if self.count==2:
					self.reset(surface)
					self.count=0

	def reset(self,surface):
		self.grid_points_value=[[False for x in range(5)] for y in range(5)]
		for x,y in self.grid_points:
			pygame.draw.circle(surface, (0,0,0), (x,y), 20, 1)

	def print_grid(self):
		print(self.grid)
