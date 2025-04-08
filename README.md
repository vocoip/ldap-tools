# Python LDAP 工具库

这是一个基于Python的LDAP操作工具库，提供了简单易用的接口来操作LDAP服务器。该工具库使用ldap3库实现，支持多种认证方式，并提供了完整的日志记录功能。

## 功能特点

- 支持多种认证方式（NTLM、SIMPLE、ANONYMOUS）
- 灵活的配置管理（YAML配置文件）
- 完整的日志记录
- 用户搜索和管理
- 安全的连接处理（支持SSL）
- 异常处理和错误日志

## 系统要求

- Python 3.6+
- ldap3
- PyYAML

## 安装方法

1. 克隆仓库：
```bash
git clone https://github.com/yourusername/ldap-tools.git
cd ldap-tools
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 配置说明

1. 复制配置文件模板：
```bash
cp config.example.yaml config.yaml
```

2. 编辑 `config.yaml` 文件，配置以下内容：
   - LDAP服务器地址和端口
   - 认证信息（用户名、密码、认证方式）
   - 搜索配置（基础DN、搜索过滤器、返回属性）
   - 日志配置（日志级别、格式、文件路径）

## 使用示例

### 基本使用

```python
from ldap_connection import LDAPClient

# 创建LDAP客户端实例
ldap_client = LDAPClient()

# 连接到LDAP服务器
if ldap_client.connect():
    # 搜索用户
    users = ldap_client.search_users()
    
    # 处理搜索结果
    for user in users:
        print(f"用户: {user['cn']}")
        print(f"邮箱: {user['mail']}")
        print(f"部门: {user['department']}")
        print("-" * 50)
    
    # 关闭连接
    ldap_client.close()
```

### 自定义搜索

```python
# 使用自定义搜索过滤器
custom_filter = '(&(objectClass=user)(department=IT))'
users = ldap_client.search_users(search_filter=custom_filter)
```

## 主要功能模块

### 1. 连接管理
- 服务器连接配置
- 多种认证方式支持
- 连接池管理
- SSL/TLS支持

### 2. 用户操作
- 用户搜索
- 属性查询
- 结果处理

### 3. 配置管理
- YAML配置文件支持
- 灵活的配置选项
- 环境变量支持

### 4. 日志管理
- 可配置的日志级别
- 自定义日志格式
- 文件日志支持

## 错误处理

工具库包含完整的错误处理机制：
- 连接错误处理
- 认证失败处理
- 搜索错误处理
- 配置错误处理

## 安全建议

1. 使用SSL/TLS加密连接
2. 妥善保管配置文件
3. 使用最小权限原则
4. 定期更新密码
5. 启用日志审计
6. 限制访问IP

## 常见问题

1. 连接失败
   - 检查服务器地址和端口
   - 验证网络连接
   - 确认防火墙设置

2. 认证失败
   - 验证用户名和密码
   - 检查认证方式
   - 确认用户权限

3. 搜索无结果
   - 检查基础DN
   - 验证搜索过滤器
   - 确认用户存在

## 贡献指南

欢迎提交问题和改进建议！请遵循以下步骤：

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 更新日志

### v1.0.0
- 初始版本发布
- 基本LDAP操作支持
- 配置文件支持
- 日志系统集成

## 许可证

MIT License

## 作者

[Your Name]

## 联系方式

- Email: [your-email@example.com]
- GitHub: [your-github-profile] 