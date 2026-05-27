<img src="https://capsule-render.vercel.app/api?type=waving&color=316192&height=160&section=header&text=bases-datos-avanzadas&fontSize=26&fontColor=FFFFFF&fontAlignY=40&desc=BDA%20%7C%20UAH%202025-26&descAlignY=60&descColor=9FC5E8" width="100%"/>

<div align="center">

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-1D9E75?style=for-the-badge)
![UAH](https://img.shields.io/badge/UAH-GII-085041?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-5DCAA5?style=for-the-badge)

</div>

---

## About

**Asignatura:** Bases de Datos Avanzadas &middot; UAH GII &middot; Curso 2025-26

Advanced PostgreSQL internals: physical storage, indexing structures, partitioning, bulk data loading and query processing optimisation. Analysis of real I/O behaviour over datasets of up to 30 M rows.

---

## Topics covered

| Block | Content |
|-------|---------|
| Physical storage | Heap files, page layout, fill factor, `pg_relation_filepath`, `pg_size_pretty` |
| VACUUM / ANALYZE | Dead tuples, FSM/VM files, autovacuum, `VACUUM FULL`, storage reclamation |
| Partitioning | Hash partitioning (`mod`), range/list partitioning, partition pruning |
| B-Tree indexes | Multi-level structure, fan-out, height, `pgstatindex`, `pageinspect` |
| Hash indexes | Buckets, overflow, `pg_index`, `pageinspect` |
| Statistics system | `pg_statistic`, `pg_stats`, `ANALYZE`, `default_statistics_target` |
| Query processing | `EXPLAIN`, `EXPLAIN ANALYZE`, plan nodes, cost model, planner statistics |
| I/O monitoring | `pg_statio_user_tables`, `pg_statio_user_indexes`, cumulative stats reset |
| Bulk loading | `COPY`, load ordering with FK constraints, timing per table |
| Query optimisation | Index selection, multi-column indexes, VACUUM after mass DELETE |

---

## Practices

| # | Name | Description | Stack |
|---|------|-------------|-------|
| PL1 | [almacenamiento](./pl1-almacenamiento/) | 27-question deep-dive into PostgreSQL physical storage: heap layout, block fill, VACUUM/ANALYZE, hash & B-Tree indexes, partitioning and I/O monitoring — 30 M row `estudiantes` dataset | PostgreSQL · Python · SQL |
| PL2 | [carga-masiva](./pl2-carga-masiva/) | Bulk-load of 6-table MUSICOS database (1 M músicos, 24 M entradas, 12 M canciones); EXPLAIN-driven query optimisation, mass DELETE with FK cascade, multi-column index tuning | PostgreSQL · Python · SQL |

---

## Project structure

```
bases-datos-avanzadas/
├── pl1-almacenamiento/
│   ├── Int_Datos.py          # Generates 30 M-row estudiantes CSV
│   └── Consulta1.sql         # DDL + COPY + ANALYZE for estudiantes
└── pl2-carga-masiva/
    └── CSVMusicos.py         # Generates all 7 MUSICOS CSVs
                              #   grupos (200K), musicos (1M), conciertos (100K),
                              #   discos (1M), canciones (12M),
                              #   entradas (24M), grupos_conciertos (2M)
```

---

## Authors

| Name | DNI |
|------|-----|
| Daniel Del Nogal Buchanan | 54010299C |

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=316192&height=100&section=footer" width="100%"/>

*Bases de Datos Avanzadas &middot; UAH GII &middot; 2025-26*
</div>
