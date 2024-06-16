## Performing a K-Means Clustering to Reclassify Players Beyond Their Listed Positions

### Overview
This project aims to uncover new insights into player roles and similarities by performing a K-Means clustering using a variety of player statistics.

### Contents
1. **Datasets** (located in `data/`)
   - `combined_stats.csv`: Combined player statistics across various categories.
   - `player_3pt_defense.json`: Defensive statistics of players against three-point shots.
   - `players_per_game_stats.json`: Per game statistics of players.
   - `players_advanced_stats.json`: Advanced statistics of players.
   - `player_2pt_defense.json`: Defensive statistics of players against two-point shots.
   - `player_passing_stats.json`: Player passing statistics.
   - `nba_alias.csv`: Player names.
   - `players_adj_shooting_stats.csv`: Adjusted shooting statistics of players.

2. **Scripts** (located in `src/`)
   - `positions_clustering.py`: Script for performing K-Means clustering to reclassify player positions.
   - `all_stats_to_csv.py`: Script for consolidating all statistics into a single CSV file.

3. **Images** (located in the `img/`)
   - Members and qualities of each cluster

### Usage
#### Scripts
1. **positions_clustering.py**
   This script performs the clustering on player statistics to reclassify player positions by:

   1. **Loading Data**: Load necessary datasets.
   2. **Preprocessing Data**: Clean and prepare the data.
   3. **Feature Selection**: Select relevant features for clustering.
   4. **Normalizing Data**: Normalize the data for equal feature contribution.
   5. **K-Means Clustering**: Apply K-Means clustering to the normalized data.
   6. **Analyzing Results**: Analyze and interpret the clustering results.

   Example usage:
   ```bash
   cd src
   python3 positions_clustering.py
   ```
2. **all_stats_to_csv.py**
   This script consolidates all provided statistics into a single CSV file for easier analysis and processing.
   
   Example usage:
   ```bash
   cd src
   python3 all_stats_to_csv.py
   ```

### Results

- **Cluster 1: Inefficient players**
  - Characteristics: Low 2 point percentage, low 3 point percentage

- **Cluster 2: Big men**
  - Characteristics: High 2 point percentage, low 3 point attempt rate, high offensive and defensive rebound percentages

- **Cluster 3: High usage players**
  - Characteristics: High usage rate, above average assists per 36, above average efficiency, above average free throw rate

- **Cluster 4: All around players**
  - Characteristics: Slightly above average in many categories

- **Cluster 5: Ball handlers**
  - Characteristics: High assists per 36, but not very efficient

- **Cluster 6: Perimeter defenders**
  - Characteristics: High steal percentage

- **Cluster 7: 3 point shooters**
  - Characteristics: High 3 point attempt rate

- **Cluster 8: Big men who hit one or two 3's so their 3 point percentage is unusually high and their 3 point attempt rate is low**

