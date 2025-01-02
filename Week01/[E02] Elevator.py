class Elevator:
  def __init__(self, max_floor):
    self.current_floor = 1
    self.max_floor = max_floor

  def go_to_floor(self, floor):
    self.current_floor = floor

  def report_current_floor(self):
    return self.current_floor

maximum = Elevator(int(input()))

while True :
    current = input()
    if current == "Done" :
        print(maximum.report_current_floor())
        break

    current = int(current)

    if current > maximum.max_floor :
        print("Invalid Floor!")
        continue
    maximum.go_to_floor(current)