def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))

print("Original dictionary elements:")
print(colors:= {'Red': 1, 'Green': 3, 'Black': 5, 'White': 2, 'Pink': 4})

print("\nSort (ascending) dictionary elements by value:")
print(sort_dict_by_value(colors))

print("\nSort (descending) dictionary elements by value:")
print(sort_dict_by_value(colors, True),'\n')

# or by operator module
import operator
print(dict(sorted(colors.items(),key=operator.itemgetter(1))))
print(dict(sorted(colors.items(),key=operator.itemgetter(1),reverse=True)))
