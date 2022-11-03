-- Employees With Missing Information -> MySql

select 
  e.employee_id 
from 
  employees e 
  left outer join salaries s on e.employee_id = s.employee_id 
where 
  name is null 
  or salary is null 
union 
select 
  s.employee_id 
from 
  employees e 
  right outer join salaries s on e.employee_id = s.employee_id 
where 
  name is null 
  or salary is null 
order by 
  1;