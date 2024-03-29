# 数据库

## OLTP vs OLAP

| 分类 | 全称                                                                 | 说明                                                                          |
| ---- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| OLTP | OnLine Transaction Processsing<br />联机事务处理                     | 注重对业务的快速响应和支持，进行增删改查操作。                                |
| OLAP | OnLine Analytical Processsing<br />联机分析处理                      | 注重面向应用、市场的数据分析，辅助决策                                        |
| HTAP | Hibrid Transaction and Analytical Processing<br />混合事务和分析处理 | 可同时支持事务和分析处理，在设计架构上，避免了ETL（extract, transform, load） |

## Hadoop

支持数据密集型分布式应用程序的**开源软件框架**。

| 模块       | 功能     | 说明                                                                                               |
| ---------- | -------- | -------------------------------------------------------------------------------------------------- |
| HDFS       | 文件存储 | Hadoop Distributed File System<br />Hadoop分布式文件系统                                           |
| MapReduce  | 磁盘计算 | 用于大规模数据处理的MapReduce计算模型实现                                                          |
| 对象存储   | 对象存储 | HDFS的替代方向<br />基于云的数据存储和管理技术，适用于非结构化数据。<br />是数据湖的理想存储结构。 |
| Spark      | 内存计算 | 使用内存中缓存和优化的查询执行方式，处理大数据负载的分布式系统                                     |
| Iceberg    |          | Netflix发起，适用于高性能的分析和可靠的数据管理。                                                  |
| Hudi       |          | Uber发起，Hadoop Upsert Deletes and Incrementals；<br />适用于增量型的数据更新                     |
| Delta Lake |          | Databricks发起，适用于流批一体的数据处理。                                                         |

## 云存储类型

| 类型       | 说明                                                                                                                                           |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| 文件存储   | 存储和共享文件，具有目录和文件夹的层次结构<br />适用于非结构化数据、大型内容存储库、媒体存储。<br />用户为自然人，操作对象是文件和文件夹，变长 |
| 对象存储   | 带有元数据的平面结构，每个对象的唯一标识符，可无限拓展。<br />用户为计算机软件，操作对象是对象，变长                                           |
| 数据块存储 | 提供低延迟、高性能，无需元数据。<br />适用于结构化数据库、文件系统卷。<br />用户为数据库等软件系统，操作对象是块设备，如磁盘。定长             |
