-- Game Play Analysis I -> MySql

select 
  player_id, 
  MIN(event_date) as first_login 
from 
  activity 
group by 
  player_id;