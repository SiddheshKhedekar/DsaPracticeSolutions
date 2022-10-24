-- Fix Names in a Table -> MySql

/*
Explanation: As per intution I needed to ensure the first character was in upper case and the rest of string was lower case. The solution I implemented made use of upper and lower functions for this purpose. I used the substring function to seperate the two parts of the string that I wanted in lowercase and uppercase and concatenated them together again. Thing to remember is that substring starts from 1.
*/

select 
  user_id, 
  concat(
    upper(
      substring(name, 1, 1)
    ), 
    lower(
      substring(name, 2)
    )
  ) as name 
from 
  users 
order by 
  user_id;