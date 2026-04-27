<img src="https://capsule-render.vercel.app/api?type=waving&color=316192&height=160&section=header&text=bases-datos-avanzadas&fontSize=26&fontColor=FFFFFF&fontAlignY=40&desc=Bases%20de%20Datos%20Avanzadas%20%7C%20UAH%202025-26&descAlignY=60&descColor=9FE1CB" width="100%"/>

<div align="center">

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-1D9E75?style=for-the-badge)
![UAH](https://img.shields.io/badge/UAH-GII-085041?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-1D9E75?style=for-the-badge)

</div>

---

## About

**Asignatura:** Bases de Datos Avanzadas · UAH GII · Curso 2025-26

Deep dive into PostgreSQL internals: physical storage, indexing structures (B-Tree and Hash), table partitioning and I/O monitoring. All experiments performed on a table of **30 million records**.

---

## Topics covered

| Topic | Content |
|-------|---------|
| Physical storage | Heap files, block factor, OIDs, pg_relation_filepath |
| Dead tuples | DELETE behaviour, VACUUM FULL, ANALYZE |
| B-Tree indexes | Levels, pages per level, tuples per block, pgstatindex |
| Hash indexes | Buckets, fill factor, distribution analysis |
| Partitioning | Hash mod N, range by field, partition pruning |
| I/O monitoring | pg_statio_user_tables, pg_statio_user_indexes, heap_blks_read/hit |

---

## Practices

| # | Name | Description |
|---|------|-------------|
| PL1 | [postgresql-storage](./pl1-postgresql-storage/) | Physical file organisation, block factor analysis, B-Tree/Hash indexes on 30M records, hash/range partitioning, VACUUM/ANALYZE, full I/O monitoring with pg_statio |

---

## Key tools

```sql
SELECT pg_relation_filepath('estudiantes');
SELECT pg_size_pretty(pg_total_relation_size('estudiantes'));
SELECT * FROM pgstatindex('idx_btree_estudiante_id');
SELECT heap_blks_read, heap_blks_hit
FROM pg_statio_user_tables WHERE relname = 'estudiantes';
SELECT pg_stat_reset(); -- reset before each monitored query
```

---

## Data generator

```python
# 30M records: codigo_carrera [0,100] · edad [18,40] · indice [0,10000]
python generar_datos.py --rows 30000000 --output estudiantes.csv
```

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=316192&height=100&section=footer" width="100%"/>

*Bases de Datos Avanzadas · UAH GII · 2025-26*
</div>
