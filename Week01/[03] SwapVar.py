def convert_string_to_tuples(text_in):
  values = text_in.strip('()').split(', ')
  return tuple(map(float, values))

x, y = convert_string_to_tuples(input())
print(f"({y}, {x})")
