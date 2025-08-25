import requests
from typing import Any, Dict, Optional


def get_auth_token(
    base_url: str,
    username: str,
    password: str,
    client_id: str = "client-app",
    client_type: str = "pc",
    client_secret: str = "123456",
    grant_type: str = "password",
    timeout_seconds: int = 10,
) -> str:
    """
    登录获取 Bearer Token。
    成功返回形如 "Bearer <token>" 的完整 Authorization 值。
    """
    base_url = base_url.rstrip("/")
    url = f"{base_url}/mes-auth/oauth/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    payload = {
        "username": username,
        "password": password,
        "client_id": client_id,
        "client_type": client_type,
        "client_secret": client_secret,
        "grant_type": grant_type,
    }
    resp = requests.post(url, data=payload, headers=headers, timeout=timeout_seconds)
    resp.raise_for_status()
    obj = resp.json()
    if str(obj.get("code")) != "200":
        raise RuntimeError(f"登录失败: code={obj.get('code')}, msg={obj}")
    token = obj.get("data", {}).get("token")
    if not token:
        raise RuntimeError("登录返回无 token")
    return f"Bearer {token}"


def build_auth_headers(auth_token: str) -> Dict[str, str]:
    """根据 Bearer token 生成默认请求头。"""
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": auth_token,
    }


def scan_lot_code(
    base_url: str,
    station_id: str = "1530011073867132928",
    lot_code: str = "TEST-GCLZM-000000263",
    module_code: str = "ipc/home-device/index",
    timeout_seconds: int = 10,
    headers: Optional[Dict[str, str]] = None,
    auth_token: Optional[str] = None,
    auth_scheme: str = "Bearer",
) -> Dict[str, Any]:
    """
    调用制造报表接口: POST /mes-manufacture-report/manufactureReport/IPC/V2/scanLotCode

    Args:
        base_url: 例如 "https://your-host.com" 或 "http://host:port"
        station_id: 站点ID
        lot_code: 批次/条码
        module_code: 模块路径
        timeout_seconds: 请求超时秒数
        headers: 额外请求头（如需要自定义）
        auth_token: 鉴权 token（若提供，将自动添加 Authorization 头）
        auth_scheme: 鉴权方案，默认 "Bearer"（最终头形如 "Authorization: Bearer <token>")

    Returns:
        解析后的 JSON 响应字典
    """
    if not base_url:
        raise ValueError("base_url 不能为空")

    # 规范化 base_url，避免双斜杠
    base_url = base_url.rstrip("/")
    url = f"{base_url}/mes-manufacture-report/manufactureReport/IPC/V2/scanLotCode"

    request_headers: Dict[str, str] = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    # 注入鉴权头
    if auth_token:
        request_headers["Authorization"] = f"{auth_scheme} {auth_token}" if not auth_token.startswith("Bearer ") and auth_scheme == "Bearer" else auth_token

    if headers:
        request_headers.update(headers)

    payload = {
        "stationId": station_id,
        "lotCode": lot_code,
        "moduleCode": module_code,
    }

    response = requests.post(url, json=payload, headers=request_headers, timeout=timeout_seconds)
    response.raise_for_status()

    # 尝试解析 JSON
    try:
        return response.json()
    except ValueError:
        # 非 JSON 响应时返回原始文本
        return {"raw": response.text}


def scan_lot_code_with_login(
    base_url: str,
    username: str,
    password: str,
    station_id: str,
    lot_code: str,
    module_code: str = "ipc/home-device/index",
    timeout_seconds: int = 10,
) -> Dict[str, Any]:
    """便捷方法：先登录获取 token，再调用 scan_lot_code。"""
    bearer = get_auth_token(base_url=base_url, username=username, password=password, timeout_seconds=timeout_seconds)
    headers = build_auth_headers(bearer)
    return scan_lot_code(
        base_url=base_url,
        station_id=station_id,
        lot_code=lot_code,
        module_code=module_code,
        timeout_seconds=timeout_seconds,
        headers=headers,
        # 这里不再传 auth_token，避免与 headers 重复
    )


if __name__ == "__main__":
    # 示例调用，请替换为真实 base_url 与账号
    demo_base_url = "http://guava.ob.shuyilink.com"  # 示例，仅供调试
    try:
        token = get_auth_token(demo_base_url, username="admin", password="88888888")
        print(f"Login successful, token: {token}")
        result = scan_lot_code_with_login(
            base_url=demo_base_url,
            username="admin",
            password="88888888",
            station_id="1530011073867132928",
            lot_code="TEST-GCLZM-000000263",
        )
        print(result)
    except Exception as exc:
        print(f"请求失败: {exc}")
