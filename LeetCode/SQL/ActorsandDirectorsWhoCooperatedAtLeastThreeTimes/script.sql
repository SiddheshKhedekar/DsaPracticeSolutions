-- Actors and Directors Who Cooperated At Least Three Times -> MySql

select 
  a.actor_id, 
  a.director_id 
from 
  (
    select 
      actor_id, 
      director_id, 
      count(timestamp) as countt 
    from 
      actordirector 
    group by 
      actor_id, 
      director_id
  ) a 
where 
  countt >= 3;