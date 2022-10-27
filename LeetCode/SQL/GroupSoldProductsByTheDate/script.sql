-- Group Sold Products By The Date -> MySql

/*
Explanation: The group concat function helps in transforming record values into a single field.
*/

select 
  sell_date, 
  count(distinct product) as num_sold, 
  group_concat(distinct product) as products 
from 
  activities 
group by 
  sell_date;