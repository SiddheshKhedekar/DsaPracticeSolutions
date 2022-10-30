-- Market Analysis I -> MySql

/*
Explanation: The year function implemented here checks if the order date matches the one as 
specified in the requirement and is alternative to checking between dates.
*/

select 
  u.user_id as buyer_id, 
  u.join_date, 
  count(o.buyer_id) as orders_in_2019 
from 
  users u 
  left join orders o on u.user_id = o.buyer_id 
  and year(o.order_date) = 2019 
group by 
  u.user_id 
order by 
  u.user_id;