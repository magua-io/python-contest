# helper class
class Rect:
	"""
	Rectangle class
	"""

	def __init__(self, rect):
		"""
		Initializer of Rectangle.
		:param rect: list of points, [bottom_left_x, bottom_left_y, top_right_x, top_right_y]
		"""
		self.x1 = rect[0]
		self.y1 = rect[1]
		self.x2 = rect[2]
		self.y2 = rect[3]

	def area(self):

		"""
		Calculate the area of the rectangle
		:return: the area of the rectangle
		"""
		return (self.y2 - self.y1) * (self.x2 - self.x1)

	def intersection_rect(self, rect):
		bottom_left_x = max(self.x1, rect.x1)
		bottom_left_y = max(self.y1, rect.y1)
		top_right_x = min(self.x2, rect.x2)
		top_right_y = min(self.y2, rect.y2)
		if top_right_x > bottom_left_x and top_right_y > bottom_left_y:
			return Rect([bottom_left_x, bottom_left_y, top_right_x, top_right_y])
		else:
			return Rect([0,0,0,0])

	def intersection_area(self, rect):
		"""
		Calculate the area of intersection between the rectangle instance and the rect in the param.
		:param rect: the provided rectangle to calculate the area of intersection.
		:return: The area of intersection.
		"""
		x_overlap = max(0, min(self.x2, rect.x2) - max(self.x1, rect.x1))
		y_overlap = max(0, min(self.y2, rect.y2) - max(self.y1, rect.y1))
		return x_overlap * y_overlap

white_paper = Rect(list(map(int, input().split())))
black_paper_1 = Rect(list(map(int, input().split())))
black_paper_2 = Rect(list(map(int, input().split())))

# calculate white_paper_area
white_area = white_paper.area()

# calculate the intersection area between white_paper and black_paper_1
black_paper_1_intersect_white_paper_rect = white_paper.intersection_rect(black_paper_1)

black_paper_1_intersect_white_paper_area = black_paper_1_intersect_white_paper_rect.area()
if black_paper_1_intersect_white_paper_area == white_area:
	print("NO")
	exit(0)

# calculate the intersection area between white_paper and black_paper_2
black_paper_2_intersect_white_paper_rect = white_paper.intersection_rect(black_paper_2)
black_paper_2_intersect_white_paper_area = black_paper_2_intersect_white_paper_rect.area()
if black_paper_2_intersect_white_paper_area == white_area:
	print("NO")
	exit(0)

# intersection area among white_paper, black_paper_1 and black_paper2
black_paper_1_intersect_black_paper_2_rect = black_paper_1_intersect_white_paper_rect.intersection_rect(black_paper_2_intersect_white_paper_rect)
black_paper_1_intersect_black_paper_2_area = black_paper_1_intersect_black_paper_2_rect.area()
covered_area = black_paper_1_intersect_white_paper_area + black_paper_2_intersect_white_paper_area - black_paper_1_intersect_black_paper_2_area

if covered_area == white_area:
  print("NO")
else:
  print("YES")
