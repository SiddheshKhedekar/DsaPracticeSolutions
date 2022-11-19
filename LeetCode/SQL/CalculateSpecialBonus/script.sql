-- Calculate Special Bonus -> MySql

select 
  * 
from 
  (
    select 
      employee_id, 
      salary as bonus 
    from 
      employees 
    where 
      name not like 'M%' 
      and employee_id % 2 != 0 
    union 
    select 
      employee_id, 
      0 as bonus 
    from 
      employees 
    where 
      name like 'M%' 
      or employee_id % 2 = 0
  ) e 
order by 
  e.employee_id;