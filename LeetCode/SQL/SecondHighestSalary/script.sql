-- Second Highest Salary -> MySql

/*
Explanation: Here only one value is to be fetched achieved by limit 1 and that is the second in 
descending order which is obtained by setting offset to 1. The nested query returns null when data 
is insufficient.
*/

Select 
  (
    Select 
      distinct salary 
    from 
      Employee 
    order by 
      salary desc 
    LIMIT 
      1 OFFSET 1
  ) As SecondHighestSalary;