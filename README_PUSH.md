# 百度搜索引擎推送系统

## 功能说明

这个系统实现了自动向百度搜索引擎推送网站页面的功能，每当有用户访问页面或发布新文章时，相关页面都会被自动推送到百度。

## 系统架构

- **前端**: HTML + CSS + JavaScript
- **后端**: Flask API 服务器
- **推送服务**: 百度搜索引擎 API

## 安装和运行

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 启动服务器

#### 方式一：使用启动脚本（推荐）
```bash
start.bat
```

#### 方式二：手动启动
```bash
# 启动后端服务器
python server.py

# 启动前端服务器
python -m http.server 8000
```

### 3. 访问网站

- 前端网站: http://localhost:8000
- 后端API: http://localhost:5000

## API 接口

### 百度推送接口

**请求**
- URL: `POST /api/baidu-push`
- Content-Type: `application/json`
- Body:
```json
{
  "url": "http://www.walankaai.com/page.html"
}
```

**响应**
```json
{
  "success": true,
  "data": {
    "success": 1,
    "remain": 9999
  }
}
```

### 健康检查接口

**请求**
- URL: `GET /api/health`

**响应**
```json
{
  "status": "ok"
}
```

## 工作原理

1. 用户访问网站的任何页面
2. 页面加载时，JavaScript 获取当前页面 URL
3. 前端向后端 API 发送推送请求
4. 后端服务器调用百度推送 API
5. 百度返回推送结果
6. 结果记录在浏览器控制台中

## 测试方法

1. 启动服务器
2. 访问网站的任何页面
3. 打开浏览器开发者工具（按 F12）
4. 查看控制台输出，会显示百度推送的结果

## 配置说明

### 百度推送配置

在 `server.py` 中修改以下配置：

```python
BAIDU_API_URL = 'http://data.zz.baidu.com/urls?site=www.walankaai.com&token=qY25KMcQC6thjZzh'
```

### 前端 API 地址

在 `script.js` 中修改以下配置：

```javascript
const apiUrl = 'http://localhost:5000/api/baidu-push';
```

## 注意事项

1. 百度推送接口有每日推送次数限制
2. 推送的 URL 必须是完整的 URL 地址
3. 建议在生产环境中使用 HTTPS
4. 可以根据需要调整推送频率和策略

## 故障排除

### 推送失败

1. 检查后端服务器是否正常运行
2. 检查百度 API 配置是否正确
3. 查看浏览器控制台的错误信息
4. 查看后端服务器的日志

### CORS 错误

如果遇到 CORS 错误，确保后端服务器已正确配置 CORS：

```python
from flask_cors import CORS
CORS(app)
```

## 许可证

© 2026 吉林省瓦兰卡科技有限公司. All rights reserved.