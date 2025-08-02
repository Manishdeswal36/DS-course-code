Now we we constaints . 
we are study the 7 rules, conditon ,constratints in mysql 

1. Not null
2. Unique
3. primary key
4. auto increment 
5. check
6. default
7. foreign key


## not null 
jis column ka upar aap not null laga ho ga. uska andr aap null value nahi ho sakti . 
Deko aap not null us column par lagata ho jiski value ma aap null nahi rakna chata .
example irctc ki website ka database . ticket confirm hua aap pnr passenger name record ko empty nahi rak sakta tho aap pnr ko not null karoga.

## Unique 
apka column ma har value unique honi chaya .
Example aap ek website ka database . tho aap user email column par unique laga do ga. issa hoga kiya yadi two user ka email same hoga tho login ma dikkat aya gi .  lakin unique karna sa ya problme nahi aya gi . 

## primary key 
primary key ka use karka aap kisi bhi two rows ma diffferentiate kar paho .
Example student wala table ma roll number . 
primary key have two conditons 
- not null 
- unique (no duplicate)


## auto incremant 

deko apka paas ek data ha . 

 user id | name | email  |
 70          __         __
 71          __          __

deko aap name or email store kar raho ho . 
aap chata ho ki user_id apna aap increament ho jaya
varna aapko manually pichalag wal row ka number dekna hoga fir usam one ko increament karna hoga.

## check 
ya column par condition check laga deta ha . 
aap age column par check laga do ga 
Example age > 18
only adults aya bach nahi 
 user id | name | email  | age |
 70          __         __
 71          __          __


## default 

aap ek default value assign kar sakta ho har kisi ka liya 
example . registration date column usma hum current date ki vlaue dal dega . 

 user id | name | email  | age | registration date.
 70          __         __
 71          __          __


## foreign key 

student branch example 

 student                    branch
sid  name bid          bid  name hod
1  manish 2               1      cse
2   tansih   3              2       ece
3  himansu  1            3        me 

tho ya branch id ha jo dono table ko connect kar raha ha isko hi foreign key bolta ha . 


## pratice 

### not null 

we create a table of user in campusx database . 

```sql
CREATE TABLE users(
	user_id INTEGER NOT NULL,
	name VARCHAR(255) NOT NULL,
	email VARCHAR(255),
	password VARCHAR(255) 
)
```

value null nahi rahega kuch na kuch waha rahegi 
insert values in . 
deko majbori ma usna 0 interger value and empty string dal diya 
output .

<div class="table-responsive-md">
    <div style="position: relative;" class="data"><div class="cRsz" style="height: 66.8929px;"><div class="colborder" style="left: 64.881px;"></div><div class="colborder" style="left: 117.762px;"></div><div class="colborder" style="left: 240.952px;"></div><div class="colborder" style="left: 320.786px;"></div></div><table class="table table-striped table-hover table-sm table_results ajax w-auto pma_table" data-uniqueid="671199242">

      <thead><tr>

        <th class="draggable position-sticky text-end column_heading marker pointer" data-column="user_id" style="cursor: move;"><span>
          <a href="index.php?route=/sql&amp;db=campusx&amp;table=users&amp;sql_query=SELECT+%2A+FROM+%60users%60++%0AORDER+BY+%60users%60.%60user_id%60+ASC&amp;sql_signature=3b41d1e772b8d5adfe878cac7ff1c3879e1c6756d4f43cff77178a52b9caca5a&amp;session_max_rows=25&amp;is_browse_distinct=0" class="sortlink">user_id<input type="hidden" value="index.php?route=/sql&amp;db=campusx&amp;table=users&amp;sql_query=SELECT+%2A+FROM+%60users%60++%0AORDER+BY+%60users%60.%60user_id%60+ASC&amp;sql_signature=3b41d1e772b8d5adfe878cac7ff1c3879e1c6756d4f43cff77178a52b9caca5a&amp;session_max_rows=25&amp;is_browse_distinct=0"></a><input type="hidden" name="url-remove-order" value="index.php?route=/sql&amp;db=campusx&amp;table=users&amp;sql_query=SELECT+%2A+FROM+%60users%60&amp;sql_signature=a106a6e6fa08fc354b503822ae17edbcdc5620aba6965f411e5845be62ff9ff6&amp;session_max_rows=25&amp;is_browse_distinct=0&amp;discard_remembered_sort=1">
<input type="hidden" name="url-add-order" value="index.php?route=/sql&amp;db=campusx&amp;table=users&amp;sql_query=SELECT+%2A+FROM+%60users%60++%0AORDER+BY+%60users%60.%60user_id%60+ASC&amp;sql_signature=3b41d1e772b8d5adfe878cac7ff1c3879e1c6756d4f43cff77178a52b9caca5a&amp;session_max_rows=25&amp;is_browse_distinct=0">
        
  </span></th>
  <th class="draggable position-sticky column_heading marker pointer" data-column="name" style="cursor: move;"><span>
          <a href="index.php?route=/sql&amp;db=campusx&amp;table=users&amp;sql_query=SELECT+%2A+FROM+%60users%60++%0AORDER+BY+%60users%60.%60name%60+ASC&amp;sql_signature=5e69fde95ca1f0daa2de0fb48a3aa0c96a721e8ba9152bb807eb8933e405bd45&amp;session_max_rows=25&amp;is_browse_distinct=0" class="sortlink">name<input type="hidden" value="index.php?route=/sql&amp;db=campusx&amp;table=users&amp;sql_query=SELECT+%2A+FROM+%60users%60++%0AORDER+BY+%60users%60.%60name%60+ASC&amp;sql_signature=5e69fde95ca1f0daa2de0fb48a3aa0c96a721e8ba9152bb807eb8933e405bd45&amp;session_max_rows=25&amp;is_browse_distinct=0"></a><input type="hidden" name="url-remove-order" value="index.php?route=/sql&amp;db=campusx&amp;table=users&amp;sql_query=SELECT+%2A+FROM+%60users%60&amp;sql_signature=a106a6e6fa08fc354b503822ae17edbcdc5620aba6965f411e5845be62ff9ff6&amp;session_max_rows=25&amp;is_browse_distinct=0&amp;discard_remembered_sort=1">
<input type="hidden" name="url-add-order" value="index.php?route=/sql&amp;db=campusx&amp;table=users&amp;sql_query=SELECT+%2A+FROM+%60users%60++%0AORDER+BY+%60users%60.%60name%60+ASC&amp;sql_signature=5e69fde95ca1f0daa2de0fb48a3aa0c96a721e8ba9152bb807eb8933e405bd45&amp;session_max_rows=25&amp;is_browse_distinct=0">
        
  </span></th>
  <th class="draggable position-sticky column_heading marker pointer" data-column="email" style="cursor: move;"><span>
          <a href="index.php?route=/sql&amp;db=campusx&amp;table=users&amp;sql_query=SELECT+%2A+FROM+%60users%60++%0AORDER+BY+%60users%60.%60email%60+ASC&amp;sql_signature=c33abf13e2d985062c5c9119c104d1cdd7392366968ac594e7015509d0450cc0&amp;session_max_rows=25&amp;is_browse_distinct=0" class="sortlink">email<input type="hidden" value="index.php?route=/sql&amp;db=campusx&amp;table=users&amp;sql_query=SELECT+%2A+FROM+%60users%60++%0AORDER+BY+%60users%60.%60email%60+ASC&amp;sql_signature=c33abf13e2d985062c5c9119c104d1cdd7392366968ac594e7015509d0450cc0&amp;session_max_rows=25&amp;is_browse_distinct=0"></a><input type="hidden" name="url-remove-order" value="index.php?route=/sql&amp;db=campusx&amp;table=users&amp;sql_query=SELECT+%2A+FROM+%60users%60&amp;sql_signature=a106a6e6fa08fc354b503822ae17edbcdc5620aba6965f411e5845be62ff9ff6&amp;session_max_rows=25&amp;is_browse_distinct=0&amp;discard_remembered_sort=1">
<input type="hidden" name="url-add-order" value="index.php?route=/sql&amp;db=campusx&amp;table=users&amp;sql_query=SELECT+%2A+FROM+%60users%60++%0AORDER+BY+%60users%60.%60email%60+ASC&amp;sql_signature=c33abf13e2d985062c5c9119c104d1cdd7392366968ac594e7015509d0450cc0&amp;session_max_rows=25&amp;is_browse_distinct=0">
        
  </span></th>
  <th class="draggable position-sticky column_heading marker pointer" data-column="password"><span>
          <a href="index.php?route=/sql&amp;db=campusx&amp;table=users&amp;sql_query=SELECT+%2A+FROM+%60users%60++%0AORDER+BY+%60users%60.%60password%60+ASC&amp;sql_signature=1d1a52e3adc9eb1f27a7b15dfae4345eb2a0b215b6e779857c93af7cfecde194&amp;session_max_rows=25&amp;is_browse_distinct=0" class="sortlink">password<input type="hidden" value="index.php?route=/sql&amp;db=campusx&amp;table=users&amp;sql_query=SELECT+%2A+FROM+%60users%60++%0AORDER+BY+%60users%60.%60password%60+ASC&amp;sql_signature=1d1a52e3adc9eb1f27a7b15dfae4345eb2a0b215b6e779857c93af7cfecde194&amp;session_max_rows=25&amp;is_browse_distinct=0"></a><input type="hidden" name="url-remove-order" value="index.php?route=/sql&amp;db=campusx&amp;table=users&amp;sql_query=SELECT+%2A+FROM+%60users%60&amp;sql_signature=a106a6e6fa08fc354b503822ae17edbcdc5620aba6965f411e5845be62ff9ff6&amp;session_max_rows=25&amp;is_browse_distinct=0&amp;discard_remembered_sort=1">
<input type="hidden" name="url-add-order" value="index.php?route=/sql&amp;db=campusx&amp;table=users&amp;sql_query=SELECT+%2A+FROM+%60users%60++%0AORDER+BY+%60users%60.%60password%60+ASC&amp;sql_signature=1d1a52e3adc9eb1f27a7b15dfae4345eb2a0b215b6e779857c93af7cfecde194&amp;session_max_rows=25&amp;is_browse_distinct=0">
        
  </span></th>

      
<td class="d-print-none"><span></span></td>

        </tr>
      </thead>

      <tbody>
        <tr><td data-decimals="0" data-type="int" class="text-end data not_null text-nowrap"><span>1</span></td>
<td data-decimals="0" data-type="string" data-originallength="6" class="data not_null text pre_wrap"><span>manish</span></td>
<td data-decimals="0" data-type="string" data-originallength="16" class="data text pre_wrap"><span>manish@gmail.com</span></td>
<td data-decimals="0" data-type="string" data-originallength="4" class="data text pre_wrap"><span>1234</span></td>
</tr>
<tr><td data-decimals="0" data-type="int" class="text-end data not_null text-nowrap"><span>0</span></td>
<td class="data not_null text text-nowrap"><span></span></td>
<td data-decimals="0" data-type="string" class="data text null"><span>
    <em>NULL</em>
</span></td>
<td data-decimals="0" data-type="string" class="data text null"><span>
    <em>NULL</em>
</span></td>
</tr>

      </tbody>
    </table><div class="cPointer" style="visibility: hidden;"></div><div class="cCpy" style="display: none;"></div><div class="cEdit" style="display: none;"><input class="edit_box" rows="1"><div class="edit_area"></div></div><div class="cEdit" style="display: none;"><textarea class="edit_box" rows="1"></textarea><div class="edit_area"></div></div></div>
  </div>



### unique

aap ek sath multiple constanitn laga sakta ho not null and unique

```sql
CREATE TABLE users(
	user_id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255)  NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
)
```

jab mena insert ma dubara same email id enter karna ki koshish kari tho usna karna hi nahi diya 

### another method of constraint 

```sql 
CREATE TABLE users(
	user_id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255)  NOT NULL,
    password VARCHAR(255) NOT NULL,
--  CONSTRAINT table-name_column-name_constraint-you-apply   constraint_name (column name)
    CONSTRAINT users_email_unique  UNIQUE (email)
)
```

Question hum itna lamba syntax ya nomecaltaure kyu follow kar raha ha .



deko huma chata ha kabhi bhi hamra table  user ka name or email same nahi hona chaya 
example two user  ha unka name  ram and ram@gmail.com nahi ho sakta

```sql
CREATE TABLE users(
	user_id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255)  NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
)
```
deko ab name and email unique ban gaya . lakin huma name or email ka combination ko unique bana ha . 


```sql 
CREATE TABLE users(
	user_id INTEGER NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255)  NOT NULL,
    password VARCHAR(255) NOT NULL,
--  CONSTRAINT table-name_column-name_constraint-you-apply   constraint_name (column names)
    CONSTRAINT users_email_unique  UNIQUE (name,email)
)
```

benefits
deko aap kitna bhi column name ko ya add kar paha raha ho 
chalo yaar humna constraint lagaya tha usko delete kar deta ha 
in future ma feature laya ki email repat ho saktahi just remove constraint in the code

deko yadi aap table ko delete karoga tho data bhi delete ho jayega .

### Primary key

user_ida acha column ma jisa hum primary key bana sakta ha .
first method 

```sql
CREATE TABLE users(
	user_id INTEGER NOT NULL PRIMARY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255)  NOT NULL,
    password VARCHAR(255) NOT NULL,

    CONSTRAINT users_email_unique  UNIQUE (name,email)
)
```

second method aap constraint ban kar sakta ho 

```sql
CREATE TABLE users(
	user_id INTEGER NOT NULL ,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255)  NOT NULL,
    password VARCHAR(255) NOT NULL,
--  CONSTRAINT table-name_column-name_constraint-you-apply   constraint_name (column name)
    CONSTRAINT users_email_unique  UNIQUE (name,email),
    CONSTRAINT user_pk PRIMARY KEY (user_id)
)
```

What if you are in situation ki ek column apka primary key nahi ban pa raha 
example user_id or name ka combination banega apka primary key basically composite key

first wala not work 
```sql 
CREATE TABLE users(
	user_id INTEGER NOT NULL PRIMARY,
    name VARCHAR(255) NOT NULL PRIMARY, ,
    email VARCHAR(255)  NOT NULL,
    password VARCHAR(255) NOT NULL,

    CONSTRAINT users_email_unique  UNIQUE (name,email)
)
```
iska matalb user_id and user ka name dono alag alg primary key ha 

lakin huma tho unka combined ko key bana ha 
now it's  work 

```sql
CREATE TABLE users(
	user_id INTEGER NOT NULL ,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255)  NOT NULL,
    password VARCHAR(255) NOT NULL,
--  CONSTRAINT table-name_column-name_constraint-you-apply   constraint_name (column name)
    CONSTRAINT users_email_unique  UNIQUE (name,email),
    CONSTRAINT user_pk PRIMARY KEY (user_id,name )
)
```

second benefit is we give name to our constraint  hum chaya tho isa future ma hata sakta ha warna hama table ko delete karna padta . aor data loos ho jata 


###  auto increment

```sql
CREATE TABLE users(
	user_id INTEGER PRIMARY KEY AUTO_INCREMENT ,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255)  NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
)
```


### check 
condition apply karta ha on column 
we need to create a new table  
student_id,name,age ,

```sql
CREATE TABLE students (
	student_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL ,
    age INTEGER CHECK (age > 6 and age < 25)
)
```

second methods 

```sql 
CREATE TABLE students (
	student_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL ,
    age INTEGER CHECK (age > 6 and age < 25),

	CONSTRAINT student_age_check  CHECK (age > 6 and age < 25)
)
```


### Default 
yadi aap column ma values nahi doga tho vo default value set kar dega
example gender ha usma male and female agar selected nahi kar tho app others dena chata ho . 
```SQL
CREATE TABLE ticket (
	ticket_id INTEGER PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    travel_date DATETIME DEFAULT CURRENT_TIMESTAMP
)
```

DEFAULT ma aap koi bhi data type integer ,string,boolean set kar sakta ho .


### foreign key 
we make two tables 
cid  stands for customer id 
cutsomer                        orders
cid,name email         order id ,cid,date 
pk                               pk          fk

jiski waja en dono tables ma relation ban jaya ga.

```SQL
CREATE TABLE customers (
	cid INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE
)
```

```sql
CREATE TABLE orders (
	order_id INTEGER PRIMARY KEY AUTO_INCREMENT ,
    cid INTEGER NOT NULL,
    order_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT order_fk FOREIGN KEY (cid) REFERENCES customers(cid)
)
```

now now you if you try to delete the customer table 

```sql 
DROP TABLE customers
```

**MySQL said:** Cannot delete or update a parent row: a foreign key constraint fails`

because customers order id par depend karta ha . 


there are many benefits I add some customers and order 
yadi aap orders  ma customer id click karoga  tho aap customer tak pauch sakta ho .
tho aap refrence dekar sidha customer ma ja sakta ho  

# Refrence action 
deko yadi two tables relation ma ha yadi aap kisi ek table ma delete ya update karoga tho dursa ma kiya hoga.

if two tables are connected by a foreign key  delete ya update karna par dursa table kasa respond karega. usko bolt ha referential action . 

1. Restrict
2. Cascade
3. Set Null
4. Set Default 

### Restrict 
Restrcit  = apna deka delete karna hi nahi dega .
example two tables ha 
customers                      orders
sumit                        2  sumit 2 
				 3  sumit 2 	

### Cascade 
deko yadi apna esa Cascade mode kar diya tho vo apko delete bhi kar dega and update(modify) bhi karna dega 
example yadi mena casacade mode ha 
aor customers table  ma sumit row ko delete kiya tho order table ma bhi vo delete ho jayega . 

yadi mena  customer table ma sumit ki id ko 2 sa 20 kiya tho orders ma bhi change ho jaygea 20 ho jayeg ga
customers                      orders
sumit                        2  sumit 20
				 3  sumit 20	

how to set in cascade  what is the code of it. 

```sql
CREATE TABLE orders (
	order_id INTEGER PRIMARY KEY AUTO_INCREMENT ,
    cid INTEGER NOT NULL,
    order_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT order_fk FOREIGN KEY (cid) REFERENCES customers(cid)
	ON DELETE CASCADE
	ON UPDATE CASCADE
)
```
### Set Null
example yadi aap customers ma sumit row ko delete karega tho orders table ma null aa jayega . 

```SQL
CREATE TABLE orders (
	order_id INTEGER PRIMARY KEY AUTO_INCREMENT ,
    cid INTEGER NOT NULL,
    order_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT order_fk FOREIGN KEY (cid) REFERENCES customers(cid)
	ON DELETE SET NULL 
	ON UPDATE SET NULL
)
```

### default 
example yadi aap customers ma sumit row ko delete karega tho orders table ma sabhi jaga 0 aa jayega . 



