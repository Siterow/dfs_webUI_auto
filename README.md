
✅ 推荐的 Pytest + Selenium 自动化项目目录结构

project_name/
├── tests/                  # ✅ 测试用例目录
│   ├── test_login.py       # 登录相关测试
│   ├── test_search.py      # 搜索相关测试
│   └── conftest.py         # pytest 的 fixture 配置
│
├── pages/                  # ✅ Page Object 模式封装的页面类
│   ├── login_page.py       # 登录页的元素和方法
│   └── search_page.py      # 搜索页的元素和方法
│
├── data/                   # ✅ 测试数据（如 YAML、JSON）
│   └── login_data.yaml
│
├── utils/                  # ✅ 工具类（公共函数、封装好的等待等）
│   └── wait_utils.py
│
├── reports/                # ✅ 测试报告输出目录（如 allure、html 报告）
│
├── logs/                   # ✅ 日志输出目录（可选）
│
├── requirements.txt        # 依赖库列表
├── pytest.ini              # pytest 配置文件
└── README.md               # 项目说明


⸻

📦 各模块职责说明

目录 / 文件	说明
tests/	存放测试用例，使用 test_*.py 命名规范
conftest.py	定义全局 fixture，如 driver()
pages/	每个页面封装为一个类，统一管理元素和操作（Page Object 模式）
data/	测试数据参数化用，YAML 或 JSON 格式都行
utils/	公共工具类：显式等待、截图、日志等
reports/	pytest-html 或 Allure 报告输出目录
logs/	存放运行日志（可选）
pytest.ini	pytest 的配置，如添加命令行参数、设置默认编码
requirements.txt	pip 安装依赖，如 selenium, pytest, webdriver_manager


