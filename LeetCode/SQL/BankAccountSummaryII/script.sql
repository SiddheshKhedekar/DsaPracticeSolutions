-- Bank Account Summary II -> MySql

select 
  * 
from 
  (
    select 
      a.name, 
      sum(b.amount) as balance 
    from 
      users a 
      inner join transactions b on a.account = b.account 
    group by 
      a.account
  ) c 
where 
  c.balance > 10000;