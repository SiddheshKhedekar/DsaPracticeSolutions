-- Swap Salary -> MySql

/*
Explanation: The ^ operator works as xor operator. The ascii function returns the ascii value and the char function converts it back to original character. In this way it is possible to swap the genders for the salary.
*/

update 
  salary 
set 
  sex = char(
    ASCII(sex) ^ ASCII('f') ^ ASCII('m')
  );