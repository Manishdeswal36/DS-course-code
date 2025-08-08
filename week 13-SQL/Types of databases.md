


# Types of Databases

### 1. Relational Databases (SQL Databases)

* Store data in **tables (rows and columns)**.
* Tables can be linked using **relationships**.

```mermaid
erDiagram
    STUDENTS ||--o{ MARKS : "has"
    
    STUDENTS {
        string Name
        string Gender
        int Age
        string Course
    }

    MARKS {
        string StudentName
        int Marks
    }
```

Examples: **MySQL, PostgreSQL, Oracle, Microsoft SQL Server**

---

### 2. NoSQL Databases

* Handle large amounts of **unstructured or semi-structured data** (documents, images, videos).
* Example: **MongoDB**.

---

### 3. Columnar Databases

* Store data **by columns instead of rows**, making them efficient for analytics and aggregations (e.g., calculating averages).
* Examples: **Amazon Redshift, Google BigQuery**.


make them well sutied for data warehousing or analyatical applications 

#### store in memory 
 Take a sample table how it stored in row database and column database

| Name              | Branch   | marks |
| :---------------- | :------: | ----: |
| Ram               |   cse    | 75    |
| krisna            |   ece    | 85    |
| ...               |  ...     | ...   |

##### row database
```mermaid
flowchart TB
    subgraph Row1["Row 1"]
        A1["Name: Ram"] --> A2["Branch: CSE"] --> A3["Marks: 75"]
    end
    
    subgraph Row2["Row 2"]
        B1["Name: Krishna"] --> B2["Branch: ECE"] --> B3["Marks: 85"]
    end

    Row1 --> Row2

```

##### column  database
Example in column database How it stored in memroy 


```mermaid
flowchart LR
    subgraph Column1["Column: Name"]
        C1["Ram"] --> C2["Krishna"]
    end

    subgraph Column2["Column: Branch"]
        D1["CSE"] --> D2["ECE"]
    end

    subgraph Column3["Column: Marks"]
        E1["75"] --> E2["85"]
    end

    Column1 --> Column2 --> Column3

```

Example when you given calcualte the mean 
tho relational databse har raw ko memory ko load karega fir usma sa marks column ka mena leag
lakin wahi apka column database har ek column ka data memory ma load karega fir uska mean calcuate karega . this is memroy efficntent and faster . 
make a block of database 
```mermaid
flowchart TD
    subgraph A["Relational DB"]
        A1["Type: OLTP"]
        A2["Storage: Rows"]
        A3["Use Case: Website"]
    end

    subgraph B["Columnar DB"]
        B1["Type: OLAP"]
        B2["Storage: Columns"]
        B3["Use Case: Analytics"]
    end

    A --- B

```



---

### 4. Graph Databases

* Store **nodes and edges** for relationships (social networks, knowledge graphs).
* Examples: **Neo4j, Amazon Neptune**.

---

### 5. Key-Value Databases

* Store data as **key-value pairs** (useful for caching and quick lookups).
* Examples: **Redis, Amazon DynamoDB**.

---

### Which Database to Learn as a Data Scientist?

Priority:

1. **Relational Databases (SQL)**
2. **Columnar Databases** (for analytics)
3. **Basic NoSQL knowledge**

---

# Relational Databases (SQL Databases)

* Based on the **relational model**.
* Data is stored in **tables** (relations).

### Common Terminology

* **Table = Relation**
* **Column = Attribute**
* **Row = Tuple**
* **Number of Columns = Cardinality**
* **Number of Rows = Degree**
* **Domain = The allowed set of values for a column**

---

