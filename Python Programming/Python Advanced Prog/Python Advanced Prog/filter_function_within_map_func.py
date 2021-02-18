from functools import reduce

num_list = [2, 3, 4, 5, 6]
filter_func_within_map = list(map(lambda number: number + number, filter(lambda number: number > 3, num_list)))
print(filter_func_within_map)

map_func_within_filter = list(filter(lambda number: number > 6, map(lambda number: number + number, num_list)))
print(map_func_within_filter)

map_and_filter_within_reduce = reduce(lambda number, number2: number*number2,
                                      map(lambda number:  number + number, num_list),
                                      filter(lambda number: number > 4, num_list))

