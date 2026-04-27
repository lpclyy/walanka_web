import requests
import json

def test_baidu_push_api():
    """测试百度推送API接口"""
    
    # 测试URL
    test_url = "http://www.walankaai.com/test-page.html"
    
    # API端点
    api_url = "http://localhost:5000/api/baidu-push"
    
    # 请求数据
    payload = {
        "url": test_url
    }
    
    try:
        print("正在测试百度推送API...")
        print(f"推送URL: {test_url}")
        print(f"API端点: {api_url}")
        print()
        
        # 发送POST请求
        response = requests.post(
            api_url,
            headers={'Content-Type': 'application/json'},
            data=json.dumps(payload)
        )
        
        # 检查响应状态
        print(f"响应状态码: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("推送成功!")
            print(f"响应数据: {json.dumps(result, indent=2, ensure_ascii=False)}")
        else:
            print(f"推送失败: {response.status_code}")
            print(f"错误信息: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("错误: 无法连接到后端服务器")
        print("请确保后端服务器正在运行: python server.py")
    except Exception as e:
        print(f"发生错误: {str(e)}")

def test_health_api():
    """测试健康检查API接口"""
    
    api_url = "http://localhost:5000/api/health"
    
    try:
        print("\n正在测试健康检查API...")
        print(f"API端点: {api_url}")
        
        response = requests.get(api_url)
        
        print(f"响应状态码: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print("健康检查通过!")
            print(f"响应数据: {json.dumps(result, indent=2, ensure_ascii=False)}")
        else:
            print(f"健康检查失败: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("错误: 无法连接到后端服务器")
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    print("=" * 50)
    print("百度推送API测试工具")
    print("=" * 50)
    print()
    
    # 测试健康检查
    test_health_api()
    
    print("\n" + "=" * 50)
    
    # 测试百度推送
    test_baidu_push_api()
    
    print("\n" + "=" * 50)
    print("测试完成!")
    print("=" * 50)