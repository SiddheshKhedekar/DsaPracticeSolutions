-- Delete Duplicate Emails -> MySql

/*
Explanation: We need to delete the specific entries that have email duplicate while ensuring that 
the duplicate record with least id is not deleted and all remaining records are unique. This can be 
ensured by joining the table on itself (p,d) where email is the same and delete the records p where 
p->id is greater than d->id.
*/

delete p 
from 
  person p, 
  person d 
where 
  p.email = d.email 
  and p.id > d.id;