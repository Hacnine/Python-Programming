from operator import itemgetter, attrgetter
student_tuples = [
     ('john', 'A', 15),
     ('jane', 'B', 12),
     ('dave', 'B', 10),
 ]
sorted_tuple_itemgetter = sorted(student_tuples, key=itemgetter(1, 0), reverse=True)
# sorted_tuple_attrgetter = sorted(student_tuples, key=attrgetter('grade', 'age'))


print(sorted_tuple_itemgetter)

# my experiment:

'''
from operator import itemgetter, attrgetter
student_tuples = [
     ('A', 13),
     ('B', 12),
     ('B', 15),
 ]
sorted_tuple_itemgetter = sorted(student_tuples, key=itemgetter(1, 0), reverse=False)


for item in sorted_tuple_itemgetter:
    empty_str = ''
    for i in item:
        empty_str = empty_str + ' ' + str(i)
    print(empty_str)
    
'''