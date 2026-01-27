# Data Sources for LuxembourgHoods

## Official Government Sources (Primary)

### 1. STATEC - National Statistics Institute
- **URL**: https://statistiques.public.lu/
- **Data available**:
  - Population by commune
  - Demographics (age, nationality)
  - Employment / unemployment
  - Income statistics
  - Housing statistics
- **API**: https://lustat.statec.lu/
- **Open Data Portal**: https://data.public.lu/

### 2. Guichet.lu - Government Portal
- **URL**: https://guichet.public.lu/
- **Data available**:
  - List of communes
  - Schools by commune
  - Public services

### 3. data.public.lu - Luxembourg Open Data
- **URL**: https://data.public.lu/
- **Datasets to explore**:
  - Communes boundaries (GeoJSON)
  - Population data
  - Electoral districts
  - Public transport

---

## Real Estate Sources

### 4. Immotop.lu
- **URL**: https://www.immotop.lu/en/prix-immobilier/
- **Data available**:
  - Average price per m² by commune
  - Price trends
  - Rental prices
- **Legal note**: Check ToS before scraping. Consider contacting for API access.

### 5. Athome.lu
- **URL**: https://www.athome.lu/
- **Data available**:
  - Property listings
  - Price estimates
- **Legal note**: Same as Immotop - check ToS.

### 6. Observatoire de l'Habitat
- **URL**: https://logement.public.lu/fr/observatoire-habitat.html
- **Data available**:
  - Official housing price indices
  - Government housing statistics
- **Legal**: Public government data, safe to use.

---

## Transport Sources

### 7. Mobiliteit.lu
- **URL**: https://www.mobiliteit.lu/
- **Data available**:
  - Bus/train routes
  - Stations
  - Travel times
- **API**: https://data.public.lu/en/datasets/horaires-et-arrets-des-transport-publics-gtfs/

---

## Geographic Data

### 8. OpenStreetMap
- **URL**: https://www.openstreetmap.org/
- **Data available**:
  - Commune boundaries
  - Points of interest
  - Road network
- **Legal**: Open license, free to use with attribution.

### 9. Luxembourg Geoportal
- **URL**: https://map.geoportail.lu/
- **Data available**:
  - Official maps
  - Cadastral data
  - Aerial imagery

---

## Data Collection Strategy

### Phase 1: Government Open Data
1. Download commune list from data.public.lu
2. Fetch population data from STATEC
3. Get geographic boundaries (GeoJSON) from open data

### Phase 2: Real Estate Data
1. Contact Immotop/Athome for official API or data partnership
2. Or use Observatoire de l'Habitat (government, safe)

### Phase 3: Enrichment
1. Add transport data from GTFS feeds
2. Add school data from Guichet.lu

---

## Citation Format

For each data point, store:
```json
{
  "value": 12500,
  "year": 2025,
  "source": "statec",
  "source_url": "https://exact-url-to-data",
  "retrieved_date": "2026-01-25"
}
```

---

## Useful API Endpoints

### STATEC API (SDMX)
```
https://lustat.statec.lu/rest/data/{dataflow}/{key}
```

### Open Data Portal
```
https://data.public.lu/api/1/datasets/
```

### GTFS (Transport)
```
https://data.public.lu/en/datasets/horaires-et-arrets-des-transport-publics-gtfs/
```
