from flask import Flask, request, jsonify, Response, send_from_directory
import requests
from flask_cors import CORS
import xml.etree.ElementTree as ET
from datetime import datetime
from xml.dom import minidom
import os

app = Flask(__name__)
CORS(app)

# 确保当前目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 提供静态HTML文件
@app.route('/')
def index():
    return send_from_directory(BASE_DIR, 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(BASE_DIR, filename)

# 百度推送接口配置
BAIDU_API_URL = 'http://data.zz.baidu.com/urls?site=www.walankaai.com&token=qY25KMcQC6thjZzh'

# 网站页面信息
PAGES = [
    {'url': 'http://www.walankaai.com/', 'priority': '1.0', 'changefreq': 'weekly'},
    {'url': 'http://www.walankaai.com/geo-brand-optimization.html', 'priority': '0.8', 'changefreq': 'monthly'},
    {'url': 'http://www.walankaai.com/ai-programming.html', 'priority': '0.8', 'changefreq': 'monthly'},
    {'url': 'http://www.walankaai.com/ai-healthcare.html', 'priority': '0.8', 'changefreq': 'monthly'},
    {'url': 'http://www.walankaai.com/ai-customer-acquisition.html', 'priority': '0.8', 'changefreq': 'monthly'},
    {'url': 'http://www.walankaai.com/ai-customer-service.html', 'priority': '0.8', 'changefreq': 'monthly'},
    {'url': 'http://www.walankaai.com/custom-ai-agents.html', 'priority': '0.8', 'changefreq': 'monthly'},
    {'url': 'http://www.walankaai.com/contact.html', 'priority': '0.7', 'changefreq': 'monthly'},
]

@app.route('/api/baidu-push', methods=['POST'])
def baidu_push():
    try:
        data = request.json
        url = data.get('url')
        
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        
        # 调用百度推送API
        response = requests.post(
            BAIDU_API_URL,
            headers={'Content-Type': 'text/plain'},
            data=url
        )
        
        result = response.json()
        return jsonify({
            'success': True,
            'data': result
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/baidu-push-all', methods=['POST'])
def baidu_push_all():
    try:
        results = []
        today = datetime.now().strftime('%Y-%m-%d')
        
        for page in PAGES:
            url = page['url']
            try:
                response = requests.post(
                    BAIDU_API_URL,
                    headers={'Content-Type': 'text/plain'},
                    data=url
                )
                result = response.json()
                results.append({
                    'url': url,
                    'success': True,
                    'data': result
                })
            except Exception as e:
                results.append({
                    'url': url,
                    'success': False,
                    'error': str(e)
                })
        
        return jsonify({
            'success': True,
            'message': '批量推送完成',
            'results': results
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    try:
        urlset = ET.Element('urlset')
        urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
        urlset.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
        urlset.set('xsi:schemaLocation', 'http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd')
        
        today = datetime.now().strftime('%Y-%m-%d')
        
        for page in PAGES:
            url = ET.SubElement(urlset, 'url')
            
            loc = ET.SubElement(url, 'loc')
            loc.text = page['url']
            
            lastmod = ET.SubElement(url, 'lastmod')
            lastmod.text = today
            
            changefreq = ET.SubElement(url, 'changefreq')
            changefreq.text = page['changefreq']
            
            priority = ET.SubElement(url, 'priority')
            priority.text = page['priority']
        
        xml_str = minidom.parseString(ET.tostring(urlset)).toprettyxml(indent='    ')
        
        return Response(xml_str, content_type='application/xml')
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/baidu_verify_codeva-WSMt9Bp4y4.html', methods=['GET'])
def baidu_verify():
    return '289d0617db58251308b7187a65663b32'

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@app.route('/api/seo-info', methods=['GET'])
def seo_info():
    return jsonify({
        'site': '吉林省瓦兰卡科技有限公司',
        'domain': 'www.walankaai.com',
        'keywords': 'AI智能, GEO品牌优化, AI编程, 智能医疗, 智能拓客, 智能客服, 智能体服务',
        'description': '吉林省瓦兰卡科技有限公司 - AI智能赋能千行百业，提供GEO品牌优化、AI编程、智能医疗健康、智能拓客、智能客服等专业服务。',
        'pages_count': len(PAGES),
        'last_updated': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)