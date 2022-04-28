Python NumPy for Beginners: NumPy Specialization for Data Science (Python for Beginners in Data Science and Data Analysis Book 1)

# 1. Introduction 
"The word NumPy is a portmanteau of two words: Numerical and Python. " (%7)

"The NumPy library stores data in the formk of NumPy arrays, which provide extremely fast and memory-efficient data storage. Many advanced data science and machine learning libraries require data to be in the form of NumPy arrays before it can be processed. " (ibid)

Advantages of NumPy array over standard Python lists : 
- "faster for insertion, deletion, updating, and reading of data. " (ibid)
- "contains advanced broadcasting functionalities compared with regular Python arrays.
- come with a lot of methods that support advanced arithmetic and linear algebra options.
- provides advanced multi-dimensional array slicing capabilities."

# 2. NumPy Basics

## NumPy Arrays
"The NumPy library supports all the default Python data types in addition to some of its intrinsic data types." (%38)

To see the data type of a Numpy array : `dtypeprperty`


```
from random import random
import numpy as np 

random_array = np.array([10, 12, 14, 16, 20, 26])

print(random_array)
print(random_array.dtype)
print(random_array.dtype.itemsize)
```
Return :
```
[10 12 14 16 20 26]
int32
4 //bytes, so 32 bits
```

### Types
"The Python NumPy library supports the following data types including the default Python types.

 • i – integer

 • b – boolean

 • u – unsigned integer

 • f – float

 • c – complex float

 • m – timedelta

 • M – datetime

 • o – object

 • S – string

 • U – Unicode string

 • V – fixed chunk of memory for other type ( void )" (ibid)

We can specify the type : 

```
my_array = np.array(["1990-10-04", "1989-05-06", "1990-11-04"], dtype = "M")

```
Or like this :

```
my_array3 = my_array.astype("M")
```

### Creating a NumPy Arrays

Uni-dimensional array : 
```
import numpy as np

nums_list = [ 10 , 12 , 14 , 16 , 20 ]

nums_array = np.array(nums_list)

type (nums_array)
``` (%39)

```
Multi-dimensional NumPy array

row1 = [ 10 , 12 , 13 ]

row2 = [ 45 , 32 , 16 ]

row3 = [ 45 , 32 , 16 ]

nums_2d = np.array([row1, row2, row3])

nums_2d.shape
``` (ibid)
Output : 
```
(3, 3)
```


Using arrange() method : create a NumPy Array where the lower bound is the first parameter and the upper bound is the seconed parameter. [lower_bound, upper_bound[
    - A third parameter 








```

```
```
```
