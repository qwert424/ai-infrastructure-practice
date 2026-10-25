from langgraph.config import get_config


def get_thread_id() -> str | None:
    """取当前会话的 thread_id，不在 graph 运行时上下文内返回 None。"""
    try:
        config = get_config()
    except RuntimeError:  # 例如脚本、评测等场景没有 runnable 上下文
        return None
    return config.get("configurable", {}).get("thread_id", None)
