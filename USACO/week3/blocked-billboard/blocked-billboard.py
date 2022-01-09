import sys

sys.stdin = open('billboard.in', 'r')
sys.stdout = open('billboard.out', 'w')

# helper class
class Rect:
	"""
	Rectangle class
	"""

	def __init__(self, x1, y1, x2, y2):
		"""
		Initializer of Rectangle.
		:param x1: x of bottom left point
		:param y1: y of bottom left point
		:param x2: x of top right point
		:param y2: y of top right point
		"""
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2

	def area(self):

		"""
		Calculate the area of the rectangle
		:return: the area of the rectangle
		"""
		return (self.y2 - self.y1) * (self.x2 - self.x1)

	def intersection_area(self, rect):
		"""
		Calculate the area of intersection between the rectangle instance and the rect in the param.
		:param rect: the provided rectangle to calculate the area of intersection.
		:return: The area of intersection.
		"""
		x_overlap = max(0, min(self.x2, rect.x2) - max(self.x1, rect.x1))
		y_overlap = max(0, min(self.y2, rect.y2) - max(self.y1, rect.y1))
		return x_overlap * y_overlap

rects = []
for _ in range(3):
	x1, y1, x2, y2 = list(map(int, input().split()))
	rects.append(Rect(x1, y1, x2, y2))

print(rects[0].area() + rects[1].area() - rects[2].intersection_area(rects[0]) - rects[2].intersection_area(rects[1]))

