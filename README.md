# jspool

多集群 CDH 运维与优化相关 Web 应用：文档见 [docs/TECH_STACK.md](./docs/TECH_STACK.md)。环境要求见 [docs/DEV_ENV.md](./docs/DEV_ENV.md)。

## 本地开发

### 后端（Python 3.8）

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
# 编辑 .env 中的 DATABASE_URL，创建空库 jspool
python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

- API 文档：<http://127.0.0.1:8000/docs>
- 健康检查：<http://127.0.0.1:8000/api/v1/health>

数据库迁移（有模型后）：

```bash
cd backend
alembic revision --autogenerate -m "init"
alembic upgrade head
```

### 前端（Vue 3 + Vite）

```bash
cd frontend
npm install
npm run dev
```

默认 <http://127.0.0.1:5173>。开发环境 `VITE_API_BASE_URL` 为空时使用 Vite 将 `/api` 代理到后端 8000 端口。

生产构建：`npm run build`，静态资源在 `frontend/dist/`。

## 目录

- `docs/` — 技术栈与结构说明
- `backend/` — FastAPI + SQLAlchemy + Alembic + MySQL
- `frontend/` — Vue 3 + TypeScript + Element Plus + Pinia + Axios + ECharts
