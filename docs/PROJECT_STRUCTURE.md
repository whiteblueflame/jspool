# 目录结构

```
jspool/
├── docs/                    # 项目文档
│   ├── TECH_STACK.md        # 技术栈与约定
│   └── PROJECT_STRUCTURE.md # 本文件
├── backend/                 # Python 3.8 + FastAPI
│   ├── app/
│   │   ├── main.py          # 应用入口
│   │   ├── api/v1/          # HTTP API 版本化路由
│   │   ├── core/            # 配置等横切能力
│   │   ├── db/              # 引擎、Session、Base
│   │   ├── models/          # SQLAlchemy 模型
│   │   └── schemas/         # Pydantic 请求/响应模型
│   ├── alembic/             # 数据库迁移
│   ├── requirements.txt
│   └── .env.example
├── frontend/                # Vue 3 + Vite + TypeScript
│   ├── src/
│   │   ├── api/             # Axios 封装与接口模块
│   │   ├── router/
│   │   ├── stores/
│   │   └── views/
│   ├── package.json
│   └── vite.config.ts
└── README.md
```

后续可增加：

- `backend/app/services/`：采集与统计领域服务
- `backend/app/jobs/`：定时任务入口（APScheduler 或外部 crontab 调 CLI）
- `frontend/src/components/`：通用业务组件
