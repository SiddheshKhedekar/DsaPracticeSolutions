-- Tree Node -> MySql

/*
Explanation: Need to implement a nested if and subquery to first check if p_id -> Null then it is 
root in else check if id in all p_id from table and set to inner if true else it is leaf.
*/

select 
  id, 
  if(
    p_id is null, 
    'Root', 
    if(
      id in (
        select 
          p_id 
        from 
          tree
      ), 
      'Inner', 
      'Leaf'
    )
  ) as type 
from 
  tree 
order by 
  id;