# Deal Pilot

## 配置环境变量

基础设施（Langfuse 及其依赖组件）的密钥与账号密码全部通过根目录的 `.env` 注入：

```shell
cp .env.example .env
```

首次启动前需要在 `.env` 中补齐以下配置，其中密码类可以自定义，`SALT` / `ENCRYPTION_KEY` / `NEXTAUTH_SECRET` 建议用 `openssl rand -base64 32` 生成：

- `LANGFUSE_SALT`
- `LANGFUSE_ENCRYPTION_KEY`
- `LANGFUSE_NEXTAUTH_SECRET`
- `LANGFUSE_POSTGRES_PASSWORD`
- `LANGFUSE_CLICKHOUSE_PASSWORD`
- `LANGFUSE_MINIO_ROOT_PASSWORD`

> 已有数据后不要再更换 `LANGFUSE_SALT` 与 `LANGFUSE_ENCRYPTION_KEY`，否则历史数据无法解密。

## 启动服务

**启动基础设施环境**

```shell
make docker-recreate
```

**启动Agent服务**

```shell
# 开发模式
make dev
# debug模式
make debug
```

## 服务说明

### 常用服务

- **Agent服务**

  API访问地址：http://localhost

  langsmith调试地址：https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:80

- **Langfuse 管理后台**

  访问地址： http://localhost:3000

### 不常用服务

- MinIO 管理后台

  访问地址： http://localhost:9001

  账号/密码：`.env` 中的 `LANGFUSE_MINIO_ROOT_USER` / `LANGFUSE_MINIO_ROOT_PASSWORD`

