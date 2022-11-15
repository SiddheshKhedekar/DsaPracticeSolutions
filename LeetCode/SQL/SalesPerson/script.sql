-- Sales Person -> MySql

select 
  name 
from 
  salesperson 
where 
  name not in (
    select 
      s.name 
    from 
      salesperson s 
      left outer join orders o on s.sales_id = o.sales_id 
      left outer join company c on c.com_id = o.com_id 
    where 
      c.name = 'RED'
  );