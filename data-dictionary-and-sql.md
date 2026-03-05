# Data Dictionary, SQL Queries, and Pseudocode

## BCC Events Locations Web Application

**Dataset:** Brisbane City Council Events Locations
**Source records:** 1,696 venue rows | 186 unique suburbs | 10 venue types
**Note:** Some venues have multiple venue types (comma-separated), requiring a many-to-many relationship handled through a junction table.

---

## 1. Data Dictionary

The original flat dataset is normalised into five relational tables. The **Suburbs**, **VenueTypes**, and **Venues** tables store core entity data, the **VenueTypeLink** junction table resolves the many-to-many relationship between venues and their types, and the **Users** table supports admin authentication.

### 1.1 Suburbs Table

Stores the 186 unique Brisbane suburbs referenced by venue records.

| Field      | Data Type    | Constraints               | Description                                      |
|------------|-------------|---------------------------|--------------------------------------------------|
| SuburbID   | INT         | PRIMARY KEY, AUTO_INCREMENT | Unique identifier for each suburb                |
| SuburbName | VARCHAR(50) | NOT NULL, UNIQUE           | Name of the suburb (e.g. "Chermside", "Aspley") |

### 1.2 VenueTypes Table

Stores the 10 distinct venue type categories used by Brisbane City Council.

| Field    | Data Type    | Constraints               | Description                                                        |
|----------|-------------|---------------------------|--------------------------------------------------------------------|
| TypeID   | INT         | PRIMARY KEY, AUTO_INCREMENT | Unique identifier for each venue type                             |
| TypeName | VARCHAR(50) | NOT NULL, UNIQUE           | Name of the venue type (e.g. "Park", "Library", "Swimming pool") |

### 1.3 Venues Table

Stores the 1,696 event venue records with location and address data.

| Field        | Data Type      | Constraints                          | Description                                          |
|-------------|---------------|--------------------------------------|------------------------------------------------------|
| VenueID     | INT           | PRIMARY KEY, AUTO_INCREMENT           | Unique identifier for each venue                     |
| VenueName   | VARCHAR(100)  | NOT NULL                              | Name of the venue (e.g. "7th Brigade Park, Chermside") |
| VenueAddress| VARCHAR(150)  | NOT NULL                              | Full street address of the venue                     |
| Latitude    | DECIMAL(10,7) | NOT NULL                              | GPS latitude coordinate (range -27.65 to -27.28)    |
| Longitude   | DECIMAL(10,7) | NOT NULL                              | GPS longitude coordinate (range 152.79 to 153.42)   |
| SuburbID    | INT           | NOT NULL, FOREIGN KEY REFERENCES Suburbs(SuburbID) | Links the venue to its suburb            |

### 1.4 VenueTypeLink Table (Junction Table)

Resolves the many-to-many relationship between venues and venue types. A venue can belong to multiple types (e.g. a park that is also a community garden), and each type can apply to many venues.

| Field   | Data Type | Constraints                                                    | Description                               |
|---------|----------|----------------------------------------------------------------|-------------------------------------------|
| VenueID | INT      | NOT NULL, FOREIGN KEY REFERENCES Venues(VenueID), COMPOSITE PK | Links to the venue record                 |
| TypeID  | INT      | NOT NULL, FOREIGN KEY REFERENCES VenueTypes(TypeID), COMPOSITE PK | Links to the venue type category       |

**Composite Primary Key:** (VenueID, TypeID) -- prevents duplicate assignments.

### 1.5 Users Table

Stores administrator accounts for the web application's content management features.

| Field        | Data Type    | Constraints               | Description                                          |
|-------------|-------------|---------------------------|------------------------------------------------------|
| UserID      | INT         | PRIMARY KEY, AUTO_INCREMENT | Unique identifier for each user                     |
| Username    | VARCHAR(50) | NOT NULL, UNIQUE           | Login username for the administrator                |
| PasswordHash| VARCHAR(255)| NOT NULL                   | Hashed password (never stored in plain text)        |
| Role        | VARCHAR(20) | NOT NULL, DEFAULT 'admin'  | User role for access control (e.g. "admin")         |
| CreatedDate | DATETIME    | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Date and time the account was created     |

### Entity-Relationship Summary

```
Suburbs (1) ----< (M) Venues (M) >---- (M) VenueTypes
                              \                /
                               \--- VenueTypeLink ---/

Users (standalone - admin authentication)
```

- **Suburbs to Venues:** One-to-many (one suburb contains many venues)
- **Venues to VenueTypes:** Many-to-many via VenueTypeLink (a venue can have multiple types; a type can apply to many venues)
- **Users:** Independent table for admin login

---

## 2. SQL Queries

### 2.1 CREATE TABLE Statements

```sql
-- Create the Suburbs table
CREATE TABLE Suburbs (
    SuburbID   INT PRIMARY KEY AUTO_INCREMENT,
    SuburbName VARCHAR(50) NOT NULL UNIQUE
);

-- Create the VenueTypes table
CREATE TABLE VenueTypes (
    TypeID   INT PRIMARY KEY AUTO_INCREMENT,
    TypeName VARCHAR(50) NOT NULL UNIQUE
);

-- Create the Venues table with a foreign key to Suburbs
CREATE TABLE Venues (
    VenueID      INT PRIMARY KEY AUTO_INCREMENT,
    VenueName    VARCHAR(100) NOT NULL,
    VenueAddress VARCHAR(150) NOT NULL,
    Latitude     DECIMAL(10,7) NOT NULL,
    Longitude    DECIMAL(10,7) NOT NULL,
    SuburbID     INT NOT NULL,
    FOREIGN KEY (SuburbID) REFERENCES Suburbs(SuburbID)
);

-- Create the VenueTypeLink junction table
CREATE TABLE VenueTypeLink (
    VenueID INT NOT NULL,
    TypeID  INT NOT NULL,
    PRIMARY KEY (VenueID, TypeID),
    FOREIGN KEY (VenueID) REFERENCES Venues(VenueID),
    FOREIGN KEY (TypeID)  REFERENCES VenueTypes(TypeID)
);

-- Create the Users table for admin authentication
CREATE TABLE Users (
    UserID       INT PRIMARY KEY AUTO_INCREMENT,
    Username     VARCHAR(50) NOT NULL UNIQUE,
    PasswordHash VARCHAR(255) NOT NULL,
    Role         VARCHAR(20) NOT NULL DEFAULT 'admin',
    CreatedDate  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

### 2.2 SELECT All Venues in a Specific Suburb (JOIN)

```sql
SELECT v.VenueID, v.VenueName, v.VenueAddress, v.Latitude, v.Longitude,
       s.SuburbName
FROM Venues v
INNER JOIN Suburbs s ON v.SuburbID = s.SuburbID
WHERE s.SuburbName = 'Chermside';
```

### 2.3 SELECT Venues Filtered by Type (JOIN Through Junction Table)

```sql
SELECT v.VenueID, v.VenueName, v.VenueAddress, s.SuburbName
FROM Venues v
INNER JOIN VenueTypeLink vtl ON v.VenueID = vtl.VenueID
INNER JOIN VenueTypes vt ON vtl.TypeID = vt.TypeID
INNER JOIN Suburbs s ON v.SuburbID = s.SuburbID
WHERE vt.TypeName = 'Library';
```

### 2.4 Search Venues by Name (LIKE Query)

```sql
SELECT v.VenueID, v.VenueName, v.VenueAddress, s.SuburbName
FROM Venues v
INNER JOIN Suburbs s ON v.SuburbID = s.SuburbID
WHERE v.VenueName LIKE '%Brigade%';
```

### 2.5 COUNT Venues per Suburb (GROUP BY)

```sql
SELECT s.SuburbName, COUNT(v.VenueID) AS VenueCount
FROM Suburbs s
LEFT JOIN Venues v ON s.SuburbID = v.SuburbID
GROUP BY s.SuburbName
ORDER BY VenueCount DESC;
```

### 2.6 COUNT Venues per Type

```sql
SELECT vt.TypeName, COUNT(vtl.VenueID) AS VenueCount
FROM VenueTypes vt
LEFT JOIN VenueTypeLink vtl ON vt.TypeID = vtl.TypeID
GROUP BY vt.TypeName
ORDER BY VenueCount DESC;
```

### 2.7 INSERT a New Venue (Admin Feature)

```sql
-- Step 1: Insert the venue record (SuburbID must already exist)
INSERT INTO Venues (VenueName, VenueAddress, Latitude, Longitude, SuburbID)
VALUES ('New Community Centre', '10 Example Street, Paddington', -27.4598, 153.0137, 42);

-- Step 2: Link the venue to its type(s) using the junction table
INSERT INTO VenueTypeLink (VenueID, TypeID)
VALUES (LAST_INSERT_ID(), 3);
```

### 2.8 UPDATE Venue Details

```sql
UPDATE Venues
SET VenueName    = 'Updated Venue Name',
    VenueAddress = '99 New Address Street, Ashgrove',
    Latitude     = -27.4450,
    Longitude    = 152.9880
WHERE VenueID = 15;
```

### 2.9 DELETE a Venue

```sql
-- Step 1: Remove junction table links first (referential integrity)
DELETE FROM VenueTypeLink
WHERE VenueID = 15;

-- Step 2: Delete the venue record
DELETE FROM Venues
WHERE VenueID = 15;
```

### 2.10 SELECT with ORDER BY (Alphabetical, by Suburb)

```sql
-- Order venues alphabetically by name
SELECT v.VenueID, v.VenueName, v.VenueAddress, s.SuburbName
FROM Venues v
INNER JOIN Suburbs s ON v.SuburbID = s.SuburbID
ORDER BY v.VenueName ASC;

-- Order venues by suburb name, then by venue name within each suburb
SELECT v.VenueID, v.VenueName, v.VenueAddress, s.SuburbName
FROM Venues v
INNER JOIN Suburbs s ON v.SuburbID = s.SuburbID
ORDER BY s.SuburbName ASC, v.VenueName ASC;
```

### 2.11 Admin Login Query (SELECT User by Username)

```sql
SELECT UserID, Username, PasswordHash, Role
FROM Users
WHERE Username = 'admin_user';
```

---

## 3. Pseudocode

### 3.1 Search Algorithm

User enters a search term and the system filters venues by matching the term against venue name, suburb, or venue type.

```
FUNCTION SearchVenues(searchTerm)
    SET results TO empty list

    QUERY database:
        SELECT VenueID, VenueName, VenueAddress, SuburbName, TypeName
        FROM Venues
        JOIN Suburbs ON Venues.SuburbID = Suburbs.SuburbID
        JOIN VenueTypeLink ON Venues.VenueID = VenueTypeLink.VenueID
        JOIN VenueTypes ON VenueTypeLink.TypeID = VenueTypes.TypeID
        WHERE VenueName LIKE "%" + searchTerm + "%"
           OR SuburbName LIKE "%" + searchTerm + "%"
           OR TypeName LIKE "%" + searchTerm + "%"

    FOR EACH row in query results
        IF row.VenueID is NOT already in results THEN
            ADD row to results
        END IF
    END FOR

    RETURN results
END FUNCTION
```

### 3.2 Sort Algorithm

Sort the current list of venues alphabetically by name or by suburb name.

```
FUNCTION SortVenues(venueList, sortField)
    IF sortField = "name" THEN
        SORT venueList BY VenueName in ascending order
    ELSE IF sortField = "suburb" THEN
        SORT venueList BY SuburbName in ascending order, THEN BY VenueName in ascending order
    END IF

    RETURN venueList
END FUNCTION
```

### 3.3 Authentication Algorithm

Admin login with username and password validation using hashed password comparison.

```
FUNCTION AuthenticateUser(inputUsername, inputPassword)
    QUERY database:
        SELECT UserID, Username, PasswordHash, Role
        FROM Users
        WHERE Username = inputUsername

    IF no record found THEN
        DISPLAY "Invalid username or password"
        RETURN false
    END IF

    SET storedHash TO query result PasswordHash

    SET inputHash TO HashPassword(inputPassword)

    IF inputHash = storedHash THEN
        CREATE session for user with UserID and Role
        DISPLAY "Login successful"
        RETURN true
    ELSE
        DISPLAY "Invalid username or password"
        RETURN false
    END IF
END FUNCTION
```

### 3.4 Filter Algorithm

Multi-criteria filtering allowing the user to filter venues by suburb AND/OR venue type simultaneously.

```
FUNCTION FilterVenues(selectedSuburb, selectedType)
    SET baseQuery TO "SELECT v.VenueID, v.VenueName, v.VenueAddress,
                      s.SuburbName, vt.TypeName
                      FROM Venues v
                      JOIN Suburbs s ON v.SuburbID = s.SuburbID
                      JOIN VenueTypeLink vtl ON v.VenueID = vtl.VenueID
                      JOIN VenueTypes vt ON vtl.TypeID = vt.TypeID"
    SET conditions TO empty list

    IF selectedSuburb is NOT empty THEN
        ADD "s.SuburbName = selectedSuburb" to conditions
    END IF

    IF selectedType is NOT empty THEN
        ADD "vt.TypeName = selectedType" to conditions
    END IF

    IF conditions is NOT empty THEN
        APPEND " WHERE " + JOIN conditions WITH " AND " TO baseQuery
    END IF

    APPEND " ORDER BY v.VenueName ASC" TO baseQuery

    EXECUTE baseQuery
    RETURN query results
END FUNCTION
```

### 3.5 CRUD Operations

#### Add Venue (Create)

```
FUNCTION AddVenue(name, address, latitude, longitude, suburbName, typeNames)
    CHECK user is logged in as admin
    IF NOT admin THEN
        DISPLAY "Access denied"
        RETURN
    END IF

    VALIDATE that name, address, latitude, longitude are not empty
    IF validation fails THEN
        DISPLAY "All fields are required"
        RETURN
    END IF

    QUERY database to find SuburbID for suburbName
    IF suburb not found THEN
        INSERT new suburb into Suburbs table
        SET suburbID TO new suburb's ID
    ELSE
        SET suburbID TO existing suburb's SuburbID
    END IF

    INSERT INTO Venues (VenueName, VenueAddress, Latitude, Longitude, SuburbID)
    VALUES (name, address, latitude, longitude, suburbID)

    SET newVenueID TO last inserted ID

    FOR EACH typeName IN typeNames
        QUERY database to find TypeID for typeName
        INSERT INTO VenueTypeLink (VenueID, TypeID) VALUES (newVenueID, TypeID)
    END FOR

    DISPLAY "Venue added successfully"
END FUNCTION
```

#### Edit Venue (Update)

```
FUNCTION EditVenue(venueID, newName, newAddress, newLatitude, newLongitude, newSuburb, newTypes)
    CHECK user is logged in as admin
    IF NOT admin THEN
        DISPLAY "Access denied"
        RETURN
    END IF

    VALIDATE that all required fields are not empty
    IF validation fails THEN
        DISPLAY "All fields are required"
        RETURN
    END IF

    QUERY database to find SuburbID for newSuburb

    UPDATE Venues
    SET VenueName = newName, VenueAddress = newAddress,
        Latitude = newLatitude, Longitude = newLongitude,
        SuburbID = suburbID
    WHERE VenueID = venueID

    DELETE FROM VenueTypeLink WHERE VenueID = venueID

    FOR EACH typeName IN newTypes
        QUERY database to find TypeID for typeName
        INSERT INTO VenueTypeLink (VenueID, TypeID) VALUES (venueID, TypeID)
    END FOR

    DISPLAY "Venue updated successfully"
END FUNCTION
```

#### Delete Venue

```
FUNCTION DeleteVenue(venueID)
    CHECK user is logged in as admin
    IF NOT admin THEN
        DISPLAY "Access denied"
        RETURN
    END IF

    DISPLAY "Are you sure you want to delete this venue?"

    IF user confirms THEN
        DELETE FROM VenueTypeLink WHERE VenueID = venueID
        DELETE FROM Venues WHERE VenueID = venueID
        DISPLAY "Venue deleted successfully"
    ELSE
        DISPLAY "Deletion cancelled"
    END IF
END FUNCTION
```
