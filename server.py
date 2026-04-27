from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 百度推送接口配置
BAIDU_API_URL = 'http://data.zz.baidu.com/urls?site=www.walankaai.com&token=qY25KMcQC6thjZzh'

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

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)