import requests

print('='*60)
print('SEO优化功能测试')
print('='*60)

# 测试sitemap
print('\n1. 测试站点地图 (sitemap.xml)')
try:
    response = requests.get('http://localhost:5000/sitemap.xml')
    print('状态码:', response.status_code)
    print('内容类型:', response.headers.get('Content-Type'))
    print('内容预览:')
    print(response.text[:500] + '...')
except Exception as e:
    print('错误:', e)

# 测试SEO信息接口
print('\n2. 测试SEO信息接口 (/api/seo-info)')
try:
    response = requests.get('http://localhost:5000/api/seo-info')
    print('状态码:', response.status_code)
    data = response.json()
    print('SEO信息:')
    print('  网站名称:', data['site'])
    print('  域名:', data['domain'])
    print('  关键词:', data['keywords'])
    print('  页面数量:', data['pages_count'])
except Exception as e:
    print('错误:', e)

# 测试百度验证
print('\n3. 测试百度验证')
try:
    response = requests.get('http://localhost:5000/baidu_verify_codeva-WSMt9Bp4y4.html')
    print('状态码:', response.status_code)
    print('验证内容:', response.text)
except Exception as e:
    print('错误:', e)

# 测试批量推送
print('\n4. 测试批量推送 (/api/baidu-push-all)')
try:
    response = requests.post('http://localhost:5000/api/baidu-push-all')
    print('状态码:', response.status_code)
    data = response.json()
    print('推送结果:', data['message'])
    success_count = sum(1 for r in data['results'] if r['success'])
    print('成功数量:', success_count)
except Exception as e:
    print('错误:', e)

print('\n' + '='*60)
print('测试完成!')
print('='*60)