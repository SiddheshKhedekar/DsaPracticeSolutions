-- Sales Analysis III -> MySql

/*
Explanation: First we get all the product id sold in the period greater or less than one we need to 
find. Then we select all the distinct product id between the dates we want to analyze. Finally we 
check that they are not in the result we already queried as subquery. Thing to remember is that 
between is inclusive.
*/

select 
  distinct p.product_id, 
  p.product_name 
from 
  product p 
  inner join sales s on p.product_id = s.product_id 
where 
  s.sale_date between '2019-01-01' 
  and '2019-03-31' 
  and p.product_id not in (
    select 
      p1.product_id 
    from 
      product p1 
      inner join sales s1 on p1.product_id = s1.product_id 
    where 
      s1.sale_date < '2019-01-01' 
      or s1.sale_date > '2019-03-31'
  );