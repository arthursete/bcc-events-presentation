# Digital Solutions IA1 — Technical Proposal
## BCC Events Finder: A Web Application for Brisbane City Council Event Venues

---

# 1. Introduction

## Introduction to the Presentation

This technical proposal presents the design and planning of **BCC Events Finder**, a purpose-built web application that transforms the Brisbane City Council Events Locations dataset into an accessible, user-friendly venue discovery platform. The application addresses a clear gap in the current open data ecosystem: while Brisbane City Council publishes comprehensive venue data through their Open Data Portal, this information is presented in a raw, technical format that is inaccessible to everyday residents and visitors.

This proposal will be presented as a multimodal slideshow with annotated wireframes, data dictionary tables, pseudocode algorithms, and SQL query demonstrations. The presentation is targeted at Brisbane City Council stakeholders — including data managers, IT decision-makers, and community engagement officers — using appropriate technical language.

## Constraints

### Time Constraints
- The project proposal must be completed within approximately 15 hours of class time
- Final submission due 06/03/2026
- Draft submission required by Term 1 Week 4

### Data Constraints
- The dataset is sourced from Brisbane City Council's Open Data Portal in CSV/Excel format
- The dataset contains 1,696 venue location records across 186 suburbs
- Data includes 8 fields: Venue Name, Venue Address, Venue Type, Latitude, Longitude, Suburb, suburb_list, and geolocation
- Some venues have multiple venue types stored as comma-separated values, requiring normalisation
- The dataset is static (venue locations) and does not include live event scheduling data

### Legal Constraints
- The dataset is published under a **Creative Commons Attribution 4.0 (CC BY 4.0)** licence, permitting free reuse with attribution
- Admin user credentials must be stored securely using password hashing (never plain text)
- The application must comply with the Australian Privacy Act 1988 regarding any personal data collected through admin accounts
- Brisbane City Council must be attributed as the data source

## Prescribed and Self-Determined Criteria

### Prescribed Criteria (from Task Sheet)
- The solution must be a **web application**
- It must allow users to **access and filter** the BCC Events Locations dataset
- It must present data in an **easy-to-understand format**
- It must allow effective **searching** of the dataset
- It must include **administrative privileges** where relevant
- The proposal must be presented as a **multimodal presentation** for a technical audience

### Self-Determined Criteria

**Personal Impact:**
- The application should empower individual residents to discover venues in their own suburb, encouraging personal engagement with community spaces and reducing the barrier to participation in local events

**Social Impact:**
- By making venue data accessible to all users regardless of technical ability, the application promotes social inclusion and community connectedness. Accessibility features (clear labels, high contrast, logical navigation) ensure users with disabilities can access the information

**Economic Impact:**
- A user-friendly venue discovery platform can boost local economic activity by driving foot traffic to community venues, markets, and cultural centres. Tourism visitors can more easily find attractions, benefiting local businesses in those areas

---

# 2. User Story

## 2.1 Description of Web Application

**BCC Events Finder** is a proposed web application that provides Brisbane residents and visitors with an intuitive way to discover, search, and filter the 1,696 event venue locations maintained by Brisbane City Council. The application transforms raw open data into a visually engaging, easy-to-navigate experience.

### Key Features for Users (Public):
- **Home page** with a prominent search bar and quick filter buttons for venue types
- **Browse/search page** with sidebar filters for suburb (186 options) and venue type (10 categories), sort options, and paginated results
- **Venue detail page** showing full venue information including address, type, suburb, and a map placeholder displaying GPS coordinates
- **Related venues** section showing other venues in the same suburb

### Key Features for Admins:
- **Secure login** with username and password authentication (hashed passwords)
- **Dashboard** showing statistics (total venues, suburbs, venue types) and a searchable venue management table
- **Add/Edit venue form** with fields for venue name, address, suburb (dropdown), venue type (multi-select checkboxes), latitude, and longitude
- **Delete venue** functionality with confirmation prompt

### Proposed Software Stack:
| Component | Technology | Justification |
|---|---|---|
| Frontend | HTML, CSS, JavaScript | Standard web technologies; accessible in all browsers |
| Backend | Python (Flask) | Lightweight framework suitable for data-driven apps; widely taught |
| Database | SQLite | File-based relational database; no server setup required; ideal for the dataset size |
| Mapping | Leaflet.js (future) | Open-source mapping library compatible with the lat/long data |

## 2.2 Existing Solution

### Brisbane City Council Open Data Portal (data.brisbane.qld.gov.au)

The existing solution is the **Brisbane City Council Open Data Portal**, powered by the Opendatasoft platform. This is the council's official data publishing website where they host 384+ datasets, including the Events Locations dataset.

The portal provides multiple views of the data:
- **Table view**: A paginated spreadsheet showing all 1,696 records with raw field values
- **Map view**: An interactive Leaflet.js map with venue markers and geographic shape-drawing tools for spatial filtering
- **Analyse view**: A basic chart builder for creating simple visualisations
- **Export/API**: Download options in CSV, JSON, Excel, and GeoJSON formats

**UI Components Used:**
| Component | Description |
|---|---|
| Top Navigation Bar | Links to Home, Stories, Data, Visualise, API, About |
| Search Bar | Text-based keyword search across datasets and within datasets |
| Theme Filters | Category filters on the catalogue page (Arts, Parks, Transport, etc.) |
| Dataset Cards | Title, publisher, and update timestamp for each dataset |
| Data Table | Paginated, sortable spreadsheet-style table |
| Interactive Map | Leaflet.js map with markers and shape-drawing spatial filters |
| Filter Sidebar | Faceted filter panel with active filter display |
| Download Buttons | Export in multiple formats |

### Pros of Existing Solution
1. **Comprehensive raw data access** — Full dataset available for download in multiple formats
2. **API access** — Programmatic access for developers via the Opendatasoft Explore API
3. **Geographic visualisation** — Built-in map view with coordinate plotting
4. **Open licence** — CC BY 4.0 allows free reuse
5. **Daily updates** — Event datasets refreshed daily from Trumba Calendar API
6. **Multiple export formats** — CSV, JSON, Excel, GeoJSON

### Cons of Existing Solution
1. **Not designed for general public** — The portal is a data catalogue for developers and researchers, not a venue discovery tool for everyday users
2. **No suburb-based browsing** — Users cannot simply type a suburb name and see all nearby venues in a friendly layout
3. **No user-friendly venue type filtering** — Filters show raw field values rather than visual categories with icons
4. **No integration between location and event data** — Venue locations and event schedules are in separate datasets that require manual cross-referencing
5. **Raw data presentation** — Shows latitude/longitude, database field names, and unformatted text with no contextual information
6. **No personalisation** — No saved favourites, recommendations, or accessibility preferences
7. **Poor mobile experience** — The desktop-focused data exploration interface does not work well on mobile devices
8. **No proximity search** — Users cannot search by distance from their current location
9. **Overwhelming for non-technical users** — API documentation, JSON schemas, and metadata clutter the interface
10. **Limited event data** — Trumba API cap restricts results to 1,000–2,000 upcoming events

---

# 3. Data Story

## 3.1 Sample Data

### Dataset Overview
| Property | Detail |
|---|---|
| **Source** | Brisbane City Council Open Data Portal (data.brisbane.qld.gov.au) |
| **Dataset Name** | Brisbane City Council Events Locations |
| **File Format** | CSV / Excel (.xlsx) |
| **Licence** | Creative Commons Attribution 4.0 (CC BY 4.0) |
| **Total Records** | 1,696 venue locations |
| **Total Columns** | 8 fields |
| **Unique Suburbs** | 186 |
| **Unique Venue Types** | 10 |
| **Accessibility** | Publicly available; no authentication required to download |
| **Security** | Read-only public dataset; admin features in the proposed app will use hashed password authentication |

### Dataset Columns
| Column | Data Type | Example |
|---|---|---|
| Venue Name | Text | "7th Brigade Park, Chermside" |
| Venue address | Text | "7th Brigade Park, 21 Kittyhawk Drive, Chermside" |
| Venue type | Text (may be comma-separated) | "Park" or "Community Garden,Park" |
| Latitude | Decimal | -27.3794 |
| Longitude | Decimal | 153.0303 |
| Suburb | Text | "Chermside" |
| suburb_list | Text | "C, Chermside" |
| geolocation | Text | "-27.3794, 153.0303" |

### Sample Data (First 5 Records)

| Venue Name | Venue Address | Venue Type | Lat | Long | Suburb |
|---|---|---|---|---|---|
| 'Grow for Life' Community Garden | 41 Abbeville St, Upper Mt Gravatt | Community Garden, Non-Council venue | -27.544 | 153.089 | Upper Mt Gravatt |
| 7th Brigade Park, Chermside | 21 Kittyhawk Drive, Chermside | Park | -27.379 | 153.030 | Chermside |
| A.J. Jones Recreation Reserve | 247 Cornwall St, Greenslopes | Park | -27.503 | 153.044 | Greenslopes |
| A.R.C. Hill Park, Virginia | 93 Goss Road, Virginia | Park | -27.384 | 153.056 | Virginia |
| Abbeville Street Park | 41 Abbeville St, Upper Mount Gravatt | Community Garden, Park | -27.545 | 153.090 | Upper Mt Gravatt |

### Venue Type Distribution
| Venue Type | Approximate Count |
|---|---|
| Park | ~1,200+ (majority) |
| Library | ~33 |
| Community Hall | ~50 |
| Swimming Pool | ~24 |
| Community Garden | ~40 |
| General Council venue | ~30 |
| Non-Council venue | ~20 |
| Golf course | ~10 |
| Light up asset | ~15 |
| Mobile library | ~5 |

**Note:** Some venues have multiple types (e.g., "Community Garden, Park"), requiring a many-to-many relationship in the normalised database.

## 3.2 Data Dictionary

The original flat dataset is normalised into **five relational tables** to eliminate redundancy and support efficient querying.

### Table 1: Suburbs
Stores the 186 unique Brisbane suburbs.

| Field | Data Type | Constraints | Description |
|---|---|---|---|
| SuburbID | INT | PRIMARY KEY, AUTO_INCREMENT | Unique identifier for each suburb |
| SuburbName | VARCHAR(50) | NOT NULL, UNIQUE | Name of the suburb (e.g. "Chermside") |

### Table 2: VenueTypes
Stores the 10 venue type categories.

| Field | Data Type | Constraints | Description |
|---|---|---|---|
| TypeID | INT | PRIMARY KEY, AUTO_INCREMENT | Unique identifier for each type |
| TypeName | VARCHAR(50) | NOT NULL, UNIQUE | Name of the venue type (e.g. "Park") |

### Table 3: Venues
Stores the 1,696 venue records with location data.

| Field | Data Type | Constraints | Description |
|---|---|---|---|
| VenueID | INT | PRIMARY KEY, AUTO_INCREMENT | Unique identifier for each venue |
| VenueName | VARCHAR(100) | NOT NULL | Name of the venue |
| VenueAddress | VARCHAR(150) | NOT NULL | Full street address |
| Latitude | DECIMAL(10,7) | NOT NULL | GPS latitude (-27.65 to -27.28) |
| Longitude | DECIMAL(10,7) | NOT NULL | GPS longitude (152.79 to 153.42) |
| SuburbID | INT | FK REFERENCES Suburbs(SuburbID) | Links venue to its suburb |

### Table 4: VenueTypeLink (Junction Table)
Resolves the many-to-many relationship between venues and types.

| Field | Data Type | Constraints | Description |
|---|---|---|---|
| VenueID | INT | FK REFERENCES Venues(VenueID), COMPOSITE PK | Links to the venue |
| TypeID | INT | FK REFERENCES VenueTypes(TypeID), COMPOSITE PK | Links to the type |

### Table 5: Users
Stores admin accounts for content management.

| Field | Data Type | Constraints | Description |
|---|---|---|---|
| UserID | INT | PRIMARY KEY, AUTO_INCREMENT | Unique identifier |
| Username | VARCHAR(50) | NOT NULL, UNIQUE | Admin login username |
| PasswordHash | VARCHAR(255) | NOT NULL | Hashed password (never plain text) |
| Role | VARCHAR(20) | NOT NULL, DEFAULT 'admin' | Access control role |
| CreatedDate | DATETIME | NOT NULL, DEFAULT CURRENT_TIMESTAMP | Account creation date |

### Entity-Relationship Diagram

```
Suburbs (1) ────< (M) Venues (M) >──── (M) VenueTypes
                              \                /
                               \── VenueTypeLink ──/

Users (standalone — admin authentication)
```

- **Suburbs to Venues:** One-to-many (one suburb contains many venues)
- **Venues to VenueTypes:** Many-to-many via VenueTypeLink junction table
- **Users:** Independent table for admin login

---

# 4. Proposed Solution

## 4.1 HCI (Human-Computer Interaction)

### Wireframes
Full annotated wireframes are provided in the accompanying file: **wireframes.html**

The prototype includes 6 pages:
1. **Home Page** — Navigation bar, hero section with search bar, venue type filter buttons, featured venue cards
2. **Browse/Search Results** — Sidebar with suburb dropdown and venue type checkboxes, sortable paginated results grid
3. **Venue Detail** — Breadcrumb navigation, venue information table, map placeholder with coordinates, related venues
4. **Admin Login** — Centered login card with username/password fields
5. **Admin Dashboard** — Statistics cards, searchable venue management table with Edit/Delete actions
6. **Admin Add/Edit Venue Form** — Form with all venue fields including multi-select venue type checkboxes

### Design Principles Applied

| Principle | Application |
|---|---|
| **Contrast** | Dark navigation bar against light content creates visual separation; blue primary buttons contrast with white backgrounds; red delete buttons differentiate destructive actions from safe ones |
| **Alignment** | Left-aligned form labels above inputs for fast vertical scanning; consistent table column alignment; two-column form layout for related fields |
| **Repetition** | Consistent venue card design (image, name, suburb, type badge, link) across all listing pages; identical stat card structure on admin dashboard; same navigation bar on every page |
| **Proximity** | Related filter controls grouped together in the sidebar; venue details and map placed side by side; suburb and venue type form fields adjacent; statistics cards clustered as a summary row |
| **Visual Hierarchy** | Large hero heading draws attention first; venue name uses largest heading on detail page; stat values use large bold text on dashboard; breadcrumbs in smaller text for secondary navigation |

### Usability Principles Applied

| Principle | Feature |
|---|---|
| **Consistent navigation** | Same navigation bar on every public page; distinct admin navigation on all admin pages |
| **Prominent search** | Search bar placed in the hero section of the home page — the primary user task is immediately accessible |
| **User feedback** | Results count ("Showing 1,696 of 1,696 venues") keeps users informed of filter results |
| **Breadcrumb navigation** | Shows users their location in the site hierarchy and enables easy backtracking |
| **Pagination** | Breaks 1,696 results into manageable pages to prevent information overload |
| **Related content** | Venue detail page shows other venues in the same suburb for further discovery |
| **Placeholder guidance** | Form inputs include example values (e.g., "-27.3794") to guide correct data entry |
| **Accessibility** | Required fields marked with asterisks and legend; clear labels on all inputs for screen readers; high contrast text throughout |
| **Destructive action differentiation** | Red delete button visually warns of permanent action vs. blue edit button |

## 4.2 Algorithms

### SQL Queries

**Create Tables:**
```sql
CREATE TABLE Suburbs (
    SuburbID   INT PRIMARY KEY AUTO_INCREMENT,
    SuburbName VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE VenueTypes (
    TypeID   INT PRIMARY KEY AUTO_INCREMENT,
    TypeName VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Venues (
    VenueID      INT PRIMARY KEY AUTO_INCREMENT,
    VenueName    VARCHAR(100) NOT NULL,
    VenueAddress VARCHAR(150) NOT NULL,
    Latitude     DECIMAL(10,7) NOT NULL,
    Longitude    DECIMAL(10,7) NOT NULL,
    SuburbID     INT NOT NULL,
    FOREIGN KEY (SuburbID) REFERENCES Suburbs(SuburbID)
);

CREATE TABLE VenueTypeLink (
    VenueID INT NOT NULL,
    TypeID  INT NOT NULL,
    PRIMARY KEY (VenueID, TypeID),
    FOREIGN KEY (VenueID) REFERENCES Venues(VenueID),
    FOREIGN KEY (TypeID)  REFERENCES VenueTypes(TypeID)
);

CREATE TABLE Users (
    UserID       INT PRIMARY KEY AUTO_INCREMENT,
    Username     VARCHAR(50) NOT NULL UNIQUE,
    PasswordHash VARCHAR(255) NOT NULL,
    Role         VARCHAR(20) NOT NULL DEFAULT 'admin',
    CreatedDate  DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
```

**Select venues in a specific suburb (JOIN):**
```sql
SELECT v.VenueID, v.VenueName, v.VenueAddress, v.Latitude, v.Longitude,
       s.SuburbName
FROM Venues v
INNER JOIN Suburbs s ON v.SuburbID = s.SuburbID
WHERE s.SuburbName = 'Chermside';
```

**Select venues filtered by type (JOIN through junction table):**
```sql
SELECT v.VenueID, v.VenueName, v.VenueAddress, s.SuburbName
FROM Venues v
INNER JOIN VenueTypeLink vtl ON v.VenueID = vtl.VenueID
INNER JOIN VenueTypes vt ON vtl.TypeID = vt.TypeID
INNER JOIN Suburbs s ON v.SuburbID = s.SuburbID
WHERE vt.TypeName = 'Library';
```

**Search venues by name (LIKE):**
```sql
SELECT v.VenueID, v.VenueName, v.VenueAddress, s.SuburbName
FROM Venues v
INNER JOIN Suburbs s ON v.SuburbID = s.SuburbID
WHERE v.VenueName LIKE '%Brigade%';
```

**Count venues per suburb (GROUP BY):**
```sql
SELECT s.SuburbName, COUNT(v.VenueID) AS VenueCount
FROM Suburbs s
LEFT JOIN Venues v ON s.SuburbID = v.SuburbID
GROUP BY s.SuburbName
ORDER BY VenueCount DESC;
```

**Insert a new venue (Admin):**
```sql
INSERT INTO Venues (VenueName, VenueAddress, Latitude, Longitude, SuburbID)
VALUES ('New Community Centre', '10 Example Street, Paddington', -27.4598, 153.0137, 42);

INSERT INTO VenueTypeLink (VenueID, TypeID)
VALUES (LAST_INSERT_ID(), 3);
```

**Update venue details:**
```sql
UPDATE Venues
SET VenueName = 'Updated Venue Name',
    VenueAddress = '99 New Address Street, Ashgrove'
WHERE VenueID = 15;
```

**Delete a venue (with referential integrity):**
```sql
DELETE FROM VenueTypeLink WHERE VenueID = 15;
DELETE FROM Venues WHERE VenueID = 15;
```

### Pseudocode

**Search Algorithm:**
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

**Filter Algorithm (Multi-Criteria):**
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

**Sort Algorithm:**
```
FUNCTION SortVenues(venueList, sortField)
    IF sortField = "name" THEN
        SORT venueList BY VenueName in ascending order
    ELSE IF sortField = "suburb" THEN
        SORT venueList BY SuburbName in ascending order,
            THEN BY VenueName in ascending order
    END IF

    RETURN venueList
END FUNCTION
```

**Authentication Algorithm:**
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

**Add Venue (CRUD - Create):**
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

**Delete Venue (CRUD - Delete):**
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

## 4.3 Navigation

### Site Map / User Flow

```
PUBLIC USER FLOW:
                    ┌──────────────┐
                    │   HOME PAGE  │
                    │  (Search +   │
                    │   Filters)   │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              v            v            v
    ┌─────────────┐ ┌───────────┐ ┌──────────┐
    │   BROWSE /  │ │   ABOUT   │ │  ADMIN   │
    │   SEARCH    │ │   PAGE    │ │  LOGIN   │
    │  RESULTS    │ └───────────┘ └────┬─────┘
    └──────┬──────┘                    │
           │                           v
           v                    ┌──────────┐
    ┌─────────────┐             │  ADMIN   │
    │   VENUE     │             │DASHBOARD │
    │   DETAIL    │             └────┬─────┘
    │  (+ Related │                  │
    │   Venues)   │         ┌────────┼────────┐
    └─────────────┘         v        v        v
                        ┌──────┐ ┌──────┐ ┌──────┐
                        │ ADD  │ │ EDIT │ │DELETE│
                        │VENUE │ │VENUE │ │VENUE│
                        └──────┘ └──────┘ └──────┘
```

### Navigation Description
1. **Home Page** is the entry point. Users can search, use quick filters, or browse featured venues
2. From Home, users navigate to **Browse/Search Results** via the search bar or filter buttons
3. From Browse, users click a venue card to view the **Venue Detail** page
4. The Venue Detail page shows **Related Venues** in the same suburb, allowing further exploration without returning to search
5. The **Admin Login** page is accessible from the navigation bar
6. After successful login, admins are directed to the **Admin Dashboard**
7. From the Dashboard, admins can **Add**, **Edit**, or **Delete** venues
8. All pages include a consistent navigation bar for direct access to any section

## 4.4 Acknowledgements

- Brisbane City Council. (2026). *Events Locations Dataset*. Brisbane City Council Open Data Portal. Retrieved February 2026, from https://data.brisbane.qld.gov.au/explore/dataset/brisbane-city-council-events-locations/
- Brisbane City Council. (2026). *Open Data Portal*. https://data.brisbane.qld.gov.au/
- Creative Commons. (n.d.). *Attribution 4.0 International (CC BY 4.0)*. https://creativecommons.org/licenses/by/4.0/
- Opendatasoft. (n.d.). *Opendatasoft Platform*. https://www.opendatasoft.com/

---

*Prepared for Digital Solutions IA1 — Kedron State High School, 2026*
