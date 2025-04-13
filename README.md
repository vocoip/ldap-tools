# Python LDAP 工具库

这是一个基于Python的LDAP操作工具库，提供了简单易用的接口来操作LDAP服务器。该工具库使用ldap3库实现，支持多种认证方式，并提供了完整的日志记录功能。

## 功能特点

- 支持多种认证方式（SIMPLE/NTLM）
- 灵活的配置管理（YAML配置文件）
- 完整的日志记录
- 用户搜索和管理
- 安全的连接处理（支持SSL）
- 异常处理和错误日志

## 系统要求

- Python 3.6+
- ldap3>=2.9.1
- PyYAML>=6.0.1

## 快速开始

### 1. 安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/ldap-tools.git
cd ldap-tools

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置

1. 复制配置文件模板：
```bash
cp config.example.yaml config.yaml
```

2. 编辑配置文件，根据你的环境修改以下内容：

#### SIMPLE认证配置示例（适用于标准LDAP服务器）
```yaml
ldap:
  server:
    url: 'ldap://your-ldap-server:389'
    use_ssl: false
    timeout: 30
  auth:
    username: 'cn=admin,dc=example,dc=com'  # 使用DN格式
    password: 'your-password'
    authentication: 'SIMPLE'
```

#### NTLM认证配置示例（适用于Active Directory）
```yaml
ldap:
  server:
    url: 'ldap://your-ad-server:389'
    use_ssl: false
    timeout: 30
  auth:
    username: 'user@domain.com'  # 使用域用户格式
    password: 'your-password'
    authentication: 'NTLM'
```

### 3. 基本使用

```python
from ldap_connection import LDAPClient

# 创建LDAP客户端
ldap_client = LDAPClient()

# 连接到LDAP服务器
if ldap_client.connect():
    # 搜索用户
    users = ldap_client.search_users()
    
    # 处理结果
    for user in users:
        print(f"用户: {user['cn']}")
        print(f"邮箱: {user['mail']}")
    
    # 关闭连接
    ldap_client.close()
```

## 认证方式说明

### SIMPLE认证
- 适用于标准LDAP服务器
- 使用DN格式的用户名
- 明文传输，建议配合SSL使用
- 配置简单，兼容性好

### NTLM认证
- 适用于Active Directory
- 使用域用户名格式（user@domain.com）
- Windows集成认证
- 支持更安全的认证机制

## 搜索配置

### 基础DN设置
```yaml
search:
  base_dn: 'dc=example,dc=com'  # 搜索基础DN
```

### 搜索过滤器
```yaml
search:
  default_filter: '(&(objectClass=user)(objectCategory=person))'  # AD用户搜索
  # 或
  default_filter: '(objectClass=person)'  # 标准LDAP用户搜索
```

### 返回属性配置
```yaml
search:
  attributes:
    - cn              # 通用名称
    - mail           # 邮箱
    - department     # 部门
    - title          # 职位
    # AD特有属性
    - sAMAccountName # Windows登录名
    - userPrincipalName # 用户主体名称
```

## 安全建议

1. 使用SSL/TLS加密连接
```yaml
server:
  url: 'ldaps://your-server:636'  # 使用LDAPS
  use_ssl: true
```

2. 最小权限原则
- 使用只读账号进行搜索
- 限制搜索范围
- 只返回必要属性

3. 错误处理
- 启用日志记录
- 设置合适的超时时间
- 妥善处理异常

## 故障排除

### 1. 连接失败
- 检查服务器地址和端口
- 验证网络连接
- 确认防火墙设置

### 2. 认证失败
- 检查用户名格式（DN或域格式）
- 验证密码正确性
- 确认认证方式配置

### 3. 搜索无结果
- 验证base_dn设置
- 检查搜索过滤器语法
- 确认用户权限

## 日志配置

```yaml
logging:
  level: 'INFO'  # DEBUG, INFO, WARNING, ERROR
  format: '%(asctime)s - %(levelname)s - %(message)s'
  file: 'ldap.log'
```

## 测试

使用测试脚本验证配置：
```bash
python test_ldap.py
```

## 更新日志

### v1.0.0
- 支持SIMPLE和NTLM认证
- 完整的用户搜索功能
- 灵活的配置系统
- 日志记录功能

## 贡献指南

1. Fork 项目
2. 创建特性分支
3. 提交更改
4. 推送到分支
5. 创建 Pull Request

## 许可证

MIT License

## 技术支持

如有问题或建议，请提交 Issue 或联系维护者。 