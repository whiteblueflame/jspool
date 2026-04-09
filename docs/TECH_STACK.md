# 技术栈与约定

本文档记录集群优化 Web 应用（jspool）的技术选型与约束，后续迭代以本文为准同步更新。

## 目标与约束

- **场景**：多集群（CDH 7.1.7 SP2）、Kerberos 多 realm；采集 YARN（RM REST + SPNEGO）、Impala（CM `impalaQueries` API）、Hive Metastore（JDBC 只读）；应用元数据与业务数据使用 **MySQL**。
- **明确不采用**：Redis（会话、缓存、队列均不使用 Redis；分布式锁与队列后续可用 MySQL 或操作系统级调度解决）。

## 前端

| 类别 | 选型 | 说明 |
|------|------|------|
| 框架 | Vue 3 | Composition API + `<script setup>` |
| 语言 | TypeScript | 严格模式建议逐步开启 |
| 构建 | Vite | 开发与构建 |
| 路由 | Vue Router 4 | |
| 状态 | Pinia | 全局状态与用户偏好等 |
| UI | Element Plus | 后台表格、表单、布局 |
| HTTP | Axios | 统一拦截器、错误处理 |
| 图表 | ECharts | 趋势与 TopN 等（可按页按需引入） |

**开发约定**：环境变量前缀 `VITE_`；API 基地址 `VITE_API_BASE_URL`（开发环境可指向本地 FastAPI）。

## 后端

| 类别 | 选型 | 说明 |
|------|------|------|
| 语言 | Python **3.8** | 类型注解使用 `typing`（如 `List`、`Optional`），避免 3.9+ 内置泛型 |
| Web | FastAPI | OpenAPI 自动生成，便于前后端联调 |
| ASGI | Uvicorn | 开发与本机部署 |
| 校验/配置 | Pydantic v2 + pydantic-settings | 环境变量与配置模型 |
| ORM | SQLAlchemy 2.0（同步） | 与 MySQL 交互；异步与连接池后续可按需演进 |
| 驱动 | PyMySQL | 纯 Python，便于 Windows/Linux 部署 |
| 迁移 | Alembic | 与 SQLAlchemy 模型对齐 |

**采集模块（规划）**：HTTP 客户端使用 `httpx`；Kerberos SPNEGO 对接 CM/RM 时在独立模块实现，与 API 服务进程隔离或同进程分配置均可，需避免多 realm ticket 混用。

## 数据存储

| 用途 | 存储 | 说明 |
|------|------|------|
| 应用元数据与业务表 | MySQL | 用户、权限、集群注册、采集游标、汇总与明细（分表策略后续定） |
| Hive 元数据分析 | Metastore JDBC（只读） | 不写入 Metastore，仅读取 |

## 版本与文档

- 依赖版本见 `backend/requirements.txt` 与 `frontend/package.json`。
- 目录说明见 [PROJECT_STRUCTURE.md](./PROJECT_STRUCTURE.md)。
