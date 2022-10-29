-- Capital Gain/Loss -> MySql

/*
Explanation: Fetch the price for sell and buy seperately in subquery and subtract their values and 
fetch in another query.
*/

select 
  s.stock_name, 
  (
    select 
      sum(price) 
    from 
      stocks 
    where 
      operation = 'Sell' 
      and stock_name = s.stock_name
  ) - (
    select 
      sum(price) 
    from 
      stocks 
    where 
      operation = 'Buy' 
      and stock_name = s.stock_name
  ) as capital_gain_loss 
from 
  stocks s 
group by 
  s.stock_name;