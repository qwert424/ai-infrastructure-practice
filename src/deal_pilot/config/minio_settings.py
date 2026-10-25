from deal_pilot.config.base_settings import BaseSettingsWithEnv


class MinioSettings(BaseSettingsWithEnv):
    # 专用服务账号的访问密钥（不使用 root 凭证）。
    access_key: str = ""
    # 专用服务账号的秘密密钥。
    secret_key: str = ""
    # MinIO API 地址，不包含协议前缀。
    endpoint: str = "localhost:9002"
    # 是否使用 HTTPS 连接。
    secure: bool = False
    # 默认存储桶，服务账号的权限仅限该桶。
    bucket: str = "deal-pilot"

    model_config = {"env_prefix": "MINIO_"}


minio_settings = MinioSettings()
