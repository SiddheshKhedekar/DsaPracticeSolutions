-- Top Travellers -> MySql

/*
Explanation: The fundamental logic of the query is obtainable by left join on id then grouping 
name,id and finally ordering by distance, name. However a case that can be missed is one where user 
has not travelled at all and query will return null which is not acceptable hence we need to apply 
if null and substitute it with 0.
*/

select 
  u.name, 
  ifnull(
    sum(r.distance), 
    0
  ) as travelled_distance 
from 
  users u 
  left join rides r on u.id = r.user_id 
group by 
  u.name, 
  u.id 
order by 
  travelled_distance desc, 
  u.name asc;