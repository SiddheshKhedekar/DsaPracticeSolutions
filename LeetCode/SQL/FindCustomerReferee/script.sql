-- Find Customer Referee -> MySql

select 
  name 
from 
  customer 
where 
  referee_id is null 
  or referee_id != 2;