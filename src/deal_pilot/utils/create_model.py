# 统一使用 openai 兼容模式，暂不使用 anthropic api
from collections.abc import Mapping
from typing import Any

from langchain.chat_models import init_chat_model

from deal_pilot.config.openai_settings import openai_settings


def _resolve_thinking(thinking: bool | str | dict[str, Any]) -> bool:
    """把 thinking 配置归一化为布尔值。

    约定只传 true/false；同时兼容 Langfuse prompt 里常见的
    ``{"type": "enabled" | "disabled"}`` 写法。其余取值直接报错，
    避免脏配置被静默当成「开启」。
    """
    if isinstance(thinking, bool):
        return thinking
    if isinstance(thinking, Mapping):
        thinking = thinking.get("type", "")
    if isinstance(thinking, str):
        normalized = thinking.strip().lower()
        if normalized in {"enabled", "true", "on"}:
            return True
        if normalized in {"disabled", "false", "off"}:
            return False
    raise ValueError(
        "thinking 仅支持 true/false 或 {'type': 'enabled'|'disabled'}，"
        f"实际收到：{thinking!r}"
    )


def create_model(*, thinking: bool | str | dict[str, Any] = True, **kwargs: Any):
    kwargs.pop("model_provider", None)  # 删除 model_provider 字段
    extra_body: dict[str, Any] = {
        "thinking": {"type": "enabled" if _resolve_thinking(thinking) else "disabled"},
    }
    extra_body.update(kwargs.pop("extra_body", {}))
    config = {
        "model": openai_settings.default_model,
        "model_provider": "openai_reasoning",
        "extra_body": extra_body,
    }
    config.update(kwargs)

    model = init_chat_model(**config)
    return model
