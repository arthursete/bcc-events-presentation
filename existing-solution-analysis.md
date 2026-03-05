# Existing Solution Analysis: Brisbane City Council Open Data Portal

## Solution Name
**Brisbane City Council Open Data Portal** (data.brisbane.qld.gov.au)

Powered by the Opendatasoft platform, this is Brisbane City Council's official open data website where they publish 384+ datasets for public access, including the **Events Locations** dataset that contains 1,696 event venue records across 186 suburbs.

---

## Description

The Brisbane City Council Open Data Portal is a government data publishing platform that makes council datasets publicly available for download and exploration. It is not designed as an end-user application for finding events or venues -- it is a **data catalogue** primarily intended for developers, researchers, and data analysts who want to access raw council data.

The Events Locations dataset (identifier: `brisbane-city-council-events-locations`) is one of many datasets hosted on the portal. It provides the venue name, venue type, street address, suburb, and latitude/longitude coordinates for every council event location. The dataset is published under a Creative Commons Attribution 4.0 licence and can be downloaded in CSV, JSON, Excel, and GeoJSON formats.

The portal also hosts several related event datasets (Library Events, Music Events, Markets Events, Active and Healthy Events, Creative Events, Business Events) that can be linked to the Events Locations dataset by venue name. These event datasets are sourced from an external service called Trumba and are updated daily via the Trumba Calendar API XML feed, limited to the next 1,000-2,000 upcoming events.

---

## How It Works

When a user visits the portal, they are presented with a catalogue of all available datasets. To find the Events Locations dataset, a user must:

1. Navigate to the **Explore** page (data.brisbane.qld.gov.au/explore/)
2. Search or browse through 384+ datasets using theme filters (e.g. "Arts and Culture", "Parks and Recreation") or keyword search
3. Click into the Events Locations dataset page
4. Choose between several viewing tabs: **Table**, **Map**, **Analyse**, and **Export/API**

### Table View
Displays venue records in a paginated spreadsheet-style table with columns for Venue Name, Venue Type, Address, Suburb, Latitude, and Longitude. Users can scroll through records page by page.

### Map View
Renders venue locations as markers on an interactive Leaflet.js map. Multiple basemap options are available (Jawg Streets, OpenStreetMap, Brisbane City Council aerial imagery). Users can draw circles, squares, or polygons on the map to filter data within geographic areas.

### Analyse View
Provides a basic chart-building tool where users can create simple visualisations from the dataset fields. Charts cannot be saved.

### Filter Panel
A left-hand sidebar provides text search and faceted filters. Users can filter by dataset fields (e.g. Venue Type, Suburb) using the active filters panel. However, the text search has been noted as non-functional when using the API console.

### Export/API
Technical users can download the full dataset in CSV, JSON, Excel, or GeoJSON formats, or access data programmatically through the Opendatasoft Explore API.

---

## UI Components

| Component | Description |
|---|---|
| **Top Navigation Bar** | Horizontal menu with links to Home, Stories, Data, Visualise, API, About, Contact, and Sign In |
| **Search Bar** | Text-based search on the catalogue page and within individual datasets |
| **Theme Filters** | Category-based filtering on the catalogue (Arts and Culture, Parks and Recreation, Transport, Environment, etc.) |
| **Dataset Cards** | On the catalogue page, each dataset is displayed as a card showing title, creator, and last-updated timestamp |
| **Tab Navigation** | Within a dataset: Table, Map, Analyse, Export tabs for switching between views |
| **Data Table** | Paginated spreadsheet-style table with sortable columns |
| **Interactive Map** | Leaflet.js map with markers, multiple basemap options, and geographic shape-drawing tools for spatial filtering |
| **Filter Sidebar** | Left-hand panel showing active filters and faceted filter options |
| **Record Counter** | Displays total number of records matching current filters |
| **Download Buttons** | Options to export data in CSV, JSON, Excel, GeoJSON formats |
| **Footer** | Brisbane City Council branding, Indigenous Acknowledgement of Country, language translation (109 languages), accessibility and privacy links |

---

## Colour Scheme and Visual Design

The portal uses a **corporate government aesthetic** with a blue-and-white colour scheme consistent with Brisbane City Council branding. The design is clean but utilitarian -- it prioritises data accessibility over visual appeal. Typography is standard sans-serif. There are no images, illustrations, or visual storytelling elements on dataset pages. The overall look is functional but sterile compared to modern consumer web applications.

---

## Pros

1. **Comprehensive raw data access** -- The full dataset of 1,696 venue locations is freely available for download in multiple formats (CSV, JSON, Excel, GeoJSON), making it excellent for developers and researchers.

2. **API access** -- The Opendatasoft Explore API allows programmatic access to the data, enabling third-party applications to build on top of it.

3. **Geographic visualisation** -- The built-in map view plots all venue locations with coordinate data, and supports spatial filtering by drawing shapes on the map.

4. **Multiple related datasets** -- The portal links together Events Locations with several event-category datasets (Library, Music, Markets, etc.), allowing cross-referencing by venue name.

5. **Open licence** -- Published under Creative Commons Attribution 4.0, the data can be freely reused and redistributed.

6. **Daily updates** -- Event datasets are refreshed daily from the Trumba Calendar API, ensuring relatively current information.

7. **Multiple export formats** -- Users can download in whichever format suits their needs, including GeoJSON for mapping applications.

---

## Cons

1. **Not designed for general public use** -- The portal is a data catalogue, not an event discovery tool. A regular Brisbane resident looking for "community halls near me" or "parks in my suburb with events" would find the interface confusing and unintuitive. The target audience is developers and data analysts, not everyday users.

2. **No suburb-based browsing or location search** -- There is no way to simply type in a suburb name and see all venues in that area presented in a friendly format. Users must either scroll through the raw table or use the map's geographic drawing tools, which require technical knowledge.

3. **No venue type filtering in a user-friendly way** -- While faceted filters exist, they present raw field values rather than friendly categories with icons or descriptions. There is no visual way to browse by venue type (e.g. clicking a "Parks" icon to see all parks).

4. **No integration between locations and events** -- The Events Locations dataset and the various Events datasets are completely separate. A user cannot click on a venue and see what events are happening there. The datasets must be manually cross-referenced by venue name, which requires data skills.

5. **Raw data presentation** -- The table view shows raw latitude/longitude coordinates, database-style field names, and unformatted text. There are no venue descriptions, photos, accessibility information, capacity details, or other contextual information that would help someone choose a venue.

6. **No personalisation or recommendations** -- There are no features for saving favourite venues, getting recommendations based on interests, filtering by accessibility needs, or any other personalisation. Every user sees the same undifferentiated data dump.

7. **Poor mobile experience** -- The Opendatasoft portal is designed for desktop data exploration. The table view, filter sidebar, and map tools do not translate well to mobile screens, yet many users would want to find venues on their phone while out and about.

8. **No distance or proximity search** -- Users cannot search for venues near their current location or within a specific distance radius. The only spatial filtering is the draw-a-shape-on-the-map tool, which is cumbersome.

9. **Overwhelming for non-technical users** -- The portal interface includes API documentation, JSON schemas, dataset identifiers, metadata processing timestamps, and other technical elements that clutter the experience for general users. There is no simplified view.

10. **Limited to 1,000-2,000 events** -- The Trumba API feed cap means users only see a subset of upcoming events, with no access to historical or long-term scheduling data.

---

## Key Page Descriptions

### Page 1: Explore Catalogue (data.brisbane.qld.gov.au/explore/)
The main entry point shows all 384+ council datasets as a list of cards. Each card displays the dataset title, publisher, and last-updated date. A left sidebar provides theme-based filters (Arts and Culture, Environment, Parks and Recreation, etc.) and a keyword search bar. Datasets are sorted by most recently updated. A user looking for event venues would need to know what to search for, or browse through multiple theme categories to find the relevant dataset. There is no prominent "Events" or "Venues" section.

### Page 2: Events Locations - Table View
After finding and clicking into the Events Locations dataset, the user sees a heading ("Events locations"), a paragraph of description text, and a paginated table showing all 1,696 records. Columns include Venue Name, Venue Type, Address, Suburb, Latitude, and Longitude. A left sidebar shows filter options and a record counter. The table is plain and spreadsheet-like with no visual hierarchy, icons, or colour coding to distinguish venue types. Users must page through results or use text search to find specific venues.

### Page 3: Events Locations - Map View
Switching to the Map tab, venue locations are plotted as markers on an interactive map of Brisbane. The map uses Leaflet.js with multiple basemap options. Users can zoom, pan, and click markers to see venue details in a popup. The geographic filtering tools (circle, square, polygon drawing) allow spatial queries but are not intuitive for casual users. There is no suburb boundary overlay, no clustering by venue type, and no integration with transit or directions.

### Page 4: Events Locations - Information/Metadata View
This tab shows technical metadata about the dataset: the dataset identifier, licence type (CC BY 4.0), keywords (event, location, venue), JSON schema documentation, download statistics, and links to related datasets. This page is useful for developers but offers nothing to a general user trying to find a venue.

---

## Summary

The Brisbane City Council Open Data Portal is an excellent resource for accessing raw venue and event data, but it fundamentally fails as a tool for the general public to discover and explore event locations in Brisbane. Its data-catalogue design, technical interface, lack of cross-dataset integration, absence of suburb-based browsing, and raw data presentation create significant barriers for non-technical users. This gap represents a clear opportunity for a purpose-built web application that transforms the same underlying data into an accessible, visually engaging, and user-friendly venue discovery experience.

---

*Source: data.brisbane.qld.gov.au, accessed February 2026. Platform: Opendatasoft.*
