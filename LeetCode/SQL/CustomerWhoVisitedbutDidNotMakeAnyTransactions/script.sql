-- Customer Who Visited but Did Not Make Any Transactions -> MySql

select 
  c.customer_id, 
  count(*) as count_no_trans 
from 
  (
    select 
      a.customer_id, 
      b.amount 
    from 
      visits a 
      left join transactions b on a.visit_id = b.visit_id 
    where 
      b.amount is null
  ) c 
group by 
  c.customer_id;