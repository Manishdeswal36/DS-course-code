agar aap chaho tho aap apna constraints ma bhi operation kar sakta ho 
apna constraint ko create kiya aap usma bhi add,delete ,edit kar sakta ho

you also do in Constraints 

- add
- delete
- edit 

we call the age column in customer 

```SQL
ALTER TABLE customers ADD age INTEGER NOT NULL
 
```

## add the constraints 
customer ka age 13 sa badi honi chaya
```sql
ALTER TABLE customers ADD CONSTRAINT customers_age_check CHECK (age > 13)
```

## edit the constaint 

example muja age 13 sa muja 6 karna ha 
To modify an existing `CHECK` constraint, the typical approach involves dropping the existing constraint and then adding a new one with the desired definition.

Here's how you would correct the syntax: Drop the existing constraint.

## delete the constraints 

Code

``` sql
    ALTER TABLE customers DROP CONSTRAINT customers_age_check;
```

- **Add the new constraint with the modified condition:**

Code

```sql
    ALTER TABLE customers ADD CONSTRAINT customers_age_check CHECK (age > 20);
```

ki age uski 20 sa badi ha .