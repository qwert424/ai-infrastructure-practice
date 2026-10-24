# Deal Pilot

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
  
- **LiteLLM**

  管理后台：http://localhost:4000/ui/
  
  账号/密码：`.env` 中的 `LITELLM_UI_USERNAME` / `LITELLM_UI_PASSWORD`
  
  API 地址：http://localhost:4000/v1

### 不常用服务

- MinIO 管理后台

  访问地址： http://localhost:9001

  账号/密码：`.env` 中的 `LANGFUSE_MINIO_ROOT_USER` / `LANGFUSE_MINIO_ROOT_PASSWORD`

