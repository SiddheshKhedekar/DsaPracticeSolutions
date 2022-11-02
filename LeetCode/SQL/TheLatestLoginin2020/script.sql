-- The Latest Login in 2020 -> MySql

select 
  user_id, 
  MAX(time_stamp) as last_stamp 
from 
  logins 
where 
  time_stamp like '2020-%' 
group by 
  user_id;