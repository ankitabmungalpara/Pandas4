"""

Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
 

Write a solution to find the second highest distinct salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

The result format is in the following example.
 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+

"""

# This function finds the second highest salary from the given employee DataFrame.  
# It removes duplicate salaries, checks if there are at least two unique values, and sorts them in descending order.  
# Finally, it extracts and returns the second highest salary while renaming the column appropriately.  

import pandas as pd
import numpy as np

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    # 1. Drop any duplicate salaries.
    employee = employee.drop_duplicates(["salary"])
    
    # 2. If there are less than two unique salaries, return `np.NaN`.
    if len(employee["salary"].unique()) < 2:
        return pd.DataFrame({"SecondHighestSalary": [np.NaN]})
    
    # 3. Sort the table by `salary` in descending order.
    employee = employee.sort_values("salary", ascending=False)
    
    # 4. Drop the `id` column.
    employee.drop("id", axis=1, inplace=True)
    
    # 5. Rename the `salary` column.
    employee.rename({"salary": "SecondHighestSalary"}, axis=1, inplace=True)
    
    # 6, 7. Return the second highest salary.
    return employee.head(2).tail(1)
