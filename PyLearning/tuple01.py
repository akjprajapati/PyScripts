#NameTuple

from collections import namedtuple
Scores = namedtuple('Scores', 'name marks')
result = Scores('AKumar', 73 )

# We get a nice string repr for free:
print (result.name)

# Like tuples, namedtuples are immutable:
