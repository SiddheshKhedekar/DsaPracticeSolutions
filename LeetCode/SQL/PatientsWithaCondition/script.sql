-- Patients With a Condition -> MySql

select 
  * 
from 
  patients 
where 
  conditions like 'DIAB1%' 
  or conditions like '% DIAB1%';