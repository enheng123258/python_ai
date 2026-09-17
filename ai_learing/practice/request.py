import requests

try:
    response = requests.get(
        "https://api.github.com/users/一个不存在的用户xyz123",
        timeout=5  # 5秒超时
    )
    
    # 主动检查状态码（相当于JS的 response.ok）
    response.raise_for_status()  # 4xx/5xx 会抛出异常
    
    data = response.json()
    print(data["login"])

except requests.exceptions.Timeout:
    print("请求超时了")
except requests.exceptions.HTTPError as e:
    print(f"HTTP错误：{e}")     # 比如 404
except requests.exceptions.RequestException as e:
    print(f"请求失败：{e}")