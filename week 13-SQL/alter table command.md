The __Alter Table__  statement in sql is used to modify the structure of an existing table . some of the things that  be done using the alter table statement inculde

1. Add columns
2. Delete columns
3. Modify columns 

## add the column 

example if you want to add password column 

```sql
-- ALTER TABLE customers ADD COLUMN column_name datatype constraint
ALTER TABLE customers ADD COLUMN password VARCHAR(20) NOT NULL
```

 also agar aap chaho tho ksis specidfic postion by column add kar sakta ho . 
 example huma surname column add karane ha 
```sql
-- ALTER TABLE customers ADD COLUMN column_name datatype constraint you can add after and before the column_name 
ALTER TABLE customers ADD COLUMN surname VARCHAR(20) NOT NULL AFTER name 
```

add multiples columns  we need to need  two columns 
- the pan card or joining date 

```SQL
ALTER TABLE customers
ADD COLUMN pan_card VARCHAR(16) AFTER name,
ADD COLUMN joining_date DATETIME DEFAULT CURRENT_TIMESTAMP
```

tho aap kab bhi kitna columns add kar sakta ho 

## delete 

delete the column using alter command 
example we want to delete the pan card columns

delete single column

```sql
-- ALTER TABLE table_name DROP column_name 
ALTER TABLE customers DROP pan_card
```

delete multiple column 
example we delete the password and joining date column

```sql
ALTER TABLE customers
DROP COLUMN password,
DROP COLUMN joining_date
```

## modify 
example aap existing column ko change kar sakta ho . 
example ya logical nahi chalo surname column ko integer bana deta ha 

modify single column 

```sql
ALTER TABLE customers MODIFY COLUMN surname INTEGER 
```
you modify also multiple columns 