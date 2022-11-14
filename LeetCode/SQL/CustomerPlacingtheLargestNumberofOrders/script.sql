-- Customer Placing the Largest Number of Orders -> MySql

select 
  o.customer_number 
from 
  (
    select 
      customer_number, 
      count(order_number) as co 
    from 
      orders 
    group by 
      customer_number
  ) o 
where 
  o.co = (
    select 
      max(c.co) 
    from 
      (
        select 
          customer_number, 
          count(order_number) as co 
        from 
          orders 
        group by 
          customer_number
      ) c
  );