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

t = int(input())
for _ in range(t):
  room_rect = Rect([0, 0] + list(map(int, input().split())))
  table_1 = Rect(list(map(int, input().split())))
  table_2_width, table_2_height = list(map(int, input().split()))

  table_1_left_size = table_1.x1
  table_1_bottom_size = table_1.y1
  table_1_right_size = room_rect.x2 - table_1.x2
  table_1_top_size = room_rect.y2 - table_1.y2

  if (
    table_2_width <= table_1_left_size or
    table_2_width <= table_1_right_size or
    table_2_height <= table_1_top_size or
    table_2_height <= table_1_bottom_size
  ):
    print(0)
    continue

  if (
      table_2_width > table_1_left_size + table_1_right_size and
      table_2_height > table_1_top_size + table_1_bottom_size
  ):
    print(-1)
    continue

  move_up_distance = float('inf')
  move_down_distance = float('inf')
  move_left_distance = float('inf')
  move_right_distance = float('inf')

  if table_1_bottom_size + table_1_top_size >= table_2_height:
    move_up_distance = table_2_height - table_1_bottom_size
    move_down_distance = table_2_height - table_1_top_size
  if table_1_right_size + table_1_left_size >= table_2_width:
    move_left_distance = table_2_width - table_1_right_size
    move_right_distance = table_2_width - table_1_left_size

  min_distance = min(
    move_up_distance,
    move_down_distance,
    move_left_distance,
    move_right_distance,
  )

  print(min_distance)