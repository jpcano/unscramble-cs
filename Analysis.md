## Task0

**Description**: The problem involves accessing the first row in `text.csv` and the last row in `calls.csv` and printing the information.

**Approach**: Accessed the first and las row via list indexing.

**Complexity Analysis**:
- **Algorithm**: Direct list access via indexing.
- **Big O Notation**: $O(1)$ where $n$ is the number of elements in the array.
- **Justification**: The rows are accessed once; hence, the time complexity is constant.

## Task1

**Description**: The problem involves reading each one of the phone numbers and add them to a set of distinct numbers.

**Approach**: For each row in the csv files, we extract the two phone numbers and we add them to a set. The set is a custom data structure that stores the numbers without duplicates.

**Complexity Analysis**:
- **Algorithm**: A set data structure stores each one of the numbers found without duplication.
- **Big O Notation**: $O(2*(2n)^2/2)≈O(n^2)$ where $n$ is the number of calls and mesasges.
- **Justification**: The rows are accessed once, however for each number in the row we need to iterate each number stored in the set before insertion to verify that they are not already there.

## Task2

**Description**: The problem involves reading each on of the calls and storing the accumulated duration for each telephone number.

**Approach**: 

**Complexity Analysis**:
- **Algorithm**: We have a map-reduce algorithem to store and accumulate the duration for each telephone number.
- **Big O Notation**: $O(2*(2n)^2/2) + O(N)≈O(n^2)$
- **Justification**: The process of storing and accumulating has quadratic complexity as we have to search the correct number in the list before accumulatin the duration. Then he have a linear complexity algorithm to find the highest duration in the list. At the end the aproximated complexity is quadratic as the linear part is not dominating.

## Task3-A

**Description**: The problem involves finding all Bangalore's callers and for each one extract the code of the callee. Then storing the codes in a sorted list.

**Approach**: 

**Complexity Analysis**:
- **Algorithm**: We use the set data structure from Task1 to store unique codes. Then we use an in-place Timsort algorithm on the list of codes.
- **Big O Notation**: $O((2n)^2/2) + O(nlogn)≈O(n^2)$
- **Justification**: Finding a storing the unique codes is quadratic complexity. This dominates the Timsort algorithm that is linearithmic complexity.

## Task3-B

**Description**: This involved finding all the callers from Bangalore that called a number from Bangalore and compute the percentage.

**Approach**: 

**Complexity Analysis**:
- **Algorithm**: We use just a linear search to find the correct caller and callee.
- **Big O Notation**: $O(n)$
- **Justification**: The process of identify Bangalore numbers has to be done for each number in the call and therefore the complexity is linear. Computing the percentage is constant time so it is not dominating agains the linear complexity.

## Task4

**Description**:

**Approach**: 

**Complexity Analysis**:
- **Algorithm**: 
- **Big O Notation**: $O(n^2) + O(m^2)$
- **Justification**: The complexity is dominating by searching and storing all the numbers in both the texts and calls files. Identifing the marketers and sorting the final list have subquadratic complexity and therefore they do not dominate.

