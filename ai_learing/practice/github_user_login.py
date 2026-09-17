import requests

def get_user_info(username):
    url = f"https://api.github.com/users/{username}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError:
        return None
    except requests.exceptions.RequestException as e:
        print(f"网络错误：{e}")
        return None

def main():
    username = input("请输入GitHub用户名：")
    data = get_user_info(username)
    
    if data is None:
        print(f"❌ 用户 {username} 不存在或查询失败")
        return
    
    print(f"\n👤 用户名：{data['login']}")
    print(f"📛 真实姓名：{data.get('name', '未设置')}")
    print(f"⭐ 粉丝数：{data['followers']}")
    print(f"📦 公开仓库：{data['public_repos']}")

if __name__ == "__main__":
    main()