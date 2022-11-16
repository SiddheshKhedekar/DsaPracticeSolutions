-- Employees Earning More Than Their Managers -> MySql

Select 
  e1.Name As Employee 
from 
  Employee e1 
  Inner Join Employee e2 On e1.ManagerId = e2.Id 
where 
  e2.Salary < e1.salary;