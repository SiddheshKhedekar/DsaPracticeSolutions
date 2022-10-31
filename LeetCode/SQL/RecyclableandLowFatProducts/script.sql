-- Recyclable and Low Fat Products -> MySql

select 
  product_id 
from 
  products 
where 
  low_fats = 'Y' 
  and recyclable = 'Y';