In that course we use the 3 softwares 

```mermaid
flowchart TD

    software -->xammp --> GUI

    software -->node1[mysql workbench] --> node3[code editor]

    software -->node2[sql notebook] --> note4[code + markdown ]
```

Today session is on xampp because we do a lot of GUI things 

you have to remember the hierarchy of databases isko hum bolta ha relationships database model

```mermaid
flowchart TD
	node_1[Database Server]-->node_2[DBMS] -->node3[Datbase]
	node3[Datbase] --> table1
	node3[Datbase] --> table2
	%%node3[Datbase] --> table3
	table1 --> rows
	table1 --> columns
	table2 --> node4[rows]
	table2 --> node5[columns]
```


