-- User Activity for the Past 30 Days I -> MySql

/*
Explanation: In subquery get all the activity between dates and then qroup by date along with count.
*/

select 
  a.activity_date as day, 
  count(a.user_id) as active_users 
from 
  (
    select 
      activity_date, 
      user_id 
    from 
      activity 
    where 
      activity_type in (
        'open_session', 'end_session', 'scroll_down', 'send_message'
      ) 
      and activity_date between DATE_SUB('2019-07-27', INTERVAL 29 Day) 
      and '2019-07-27' 
    group by 
      activity_date, 
      user_id
  ) a 
group by 
  a.activity_date 
order by 
  a.activity_date;