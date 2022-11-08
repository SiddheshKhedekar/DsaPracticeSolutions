-- Combine Two Tables -> MySql

Select 
  firstName, 
  lastName, 
  city, 
  state 
FROM 
  person p 
  left outer JOIN address a ON p.personId = a.personId;