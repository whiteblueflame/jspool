# 开发环境要求

| 组件 | 版本要求 | 说明 |
|------|----------|------|
| Python | **3.8+**（推荐 3.8 或 3.10 LTS） | 后端与 Alembic；请勿使用 3.7 及以下 |
| Node.js | **16+**（推荐 18+） | 前端 Vite 4；用于 `npm install` / `npm run dev` |
| MySQL | 5.7+ / 8.x | 应用库；字符集建议 `utf8mb4` |

## Windows 提示

- 若 `python` 指向旧版本，可使用 [py launcher](https://docs.python.org/3/using/windows.html#launcher)：`py -3.8 -m venv .venv`
- 确保安装 Node 后，`node` 与 `npm` 在 **PATH** 中可用

## 验证命令

```bash
python --version   # 或 py -3.8 --version
node -v
npm -v
```
