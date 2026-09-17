# AI 多功能助手

一个基于大模型的命令行AI助手，支持翻译、摘要、代码解释、润色、写作等多种模式，并支持多轮对话和流式输出。

## 功能特性

- 🎯 **多模式切换**：翻译、摘要、代码解释、润色、写作
- 💬 **多轮对话**：AI 记得上下文，可连续追问
- ⚡ **流式输出**：AI 回复像打字机一样逐字显示
- 🎨 **终端美化**：使用 rich 库渲染彩色界面和 Markdown
- 🔒 **安全存储**：API Key 通过 .env 管理，不泄露到代码

## 技术栈

- Python 3.10+
- OpenAI SDK（兼容 DeepSeek API）
- rich（终端美化）
- python-dotenv（环境变量管理）

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/你的用户名/ai-learning.git
cd ai-learning
```

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置 API Key

在项目根目录创建 `.env` 文件：

```
DEEPSEEK_API_KEY=你的key
```

> 到 [platform.deepseek.com](https://platform.deepseek.com) 注册获取 API Key

### 4. 运行

```bash
python ai_assistant.py
```

## 使用说明

启动后选择模式编号，进入对话：

- 输入内容 → AI 回复
- 输入 `exit` → 返回菜单
- 输入 `clear` → 清空当前对话历史
- 输入 `0` → 退出程序

## 项目结构

```
ai-learning/
├── ai_assistant.py       # 主程序
├── requirements.txt      # 依赖列表
├── .env                  # API Key（不上传）
└── practice/             # 学习练习代码
```

## 学习背景

这个项目是我从前端开发转向 AI 应用开发的第一个实践项目，
通过它掌握了 Python、大模型 API 调用、流式输出、终端美化等基础能力。

## License

MIT