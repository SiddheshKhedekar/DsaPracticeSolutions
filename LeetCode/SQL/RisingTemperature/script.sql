-- Rising Temperature -> MySql

select 
  w.id 
from 
  weather w, 
  weather h 
where 
  w.temperature > h.temperature 
  and w.recordDate = Date_add(h.recordDate, interval 1 day);