hum database to create karna aor usko delete karna sikaga . 
kyuki phala aap database banta ho fir uska andr tables banta ho 

1. Create
2. Drop

```sql
CREATE DATABASE campusx
```
deko aap keywords ko capital letters ma likta ho aor entity ko small case ma likta ha . ya par `CREATE` `DATABASE` `databasename`

```sql
DROP DATABASE campusx
```

yadi apko database ko delete karna ha tho 
lakin a better verison is


```sql
CREATE DATABASE if NOT EXISTS campusx
```
simple english meaning database ko banana agar campusx database  exist nahi karta 

```sql
DROP DATABASE if EXISTS campusx
```