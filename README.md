# Python LDAP 工具库

这是一个基于Python的LDAP操作工具库，提供了简单易用的接口来操作LDAP服务器。

## 功能特点

- 连接LDAP服务器
- 用户认证
- 目录查询
- 用户管理
- 组织架构管理

## 常用开源工具

1. **python-ldap**
   - 最基础和广泛使用的Python LDAP库
   - 安装：`pip install python-ldap`
   - 适合需要直接操作LDAP的场景

2. **ldap3**
   - 更现代的Python LDAP库
   - 纯Python实现，安装更容易
   - 安装：`pip install ldap3`
   - 适合新项目使用

3. **django-ldap-auth**
   - Django框架的LDAP认证插件
   - 安装：`pip install django-ldap-auth`
   - 适合Django项目使用

4. **Flask-LDAP**
   - Flask框架的LDAP扩展
   - 安装：`pip install Flask-LDAP`
   - 适合Flask项目使用

5. **OpenLDAP**
   - 最流行的开源LDAP服务器
   - 可以自己搭建LDAP服务器
   - 适合需要完整LDAP解决方案的场景

## 安装方法

```bash
pip install python-ldap
```

## 基本使用示例

```python
import ldap

# 连接LDAP服务器
conn = ldap.initialize('ldap://your-ldap-server:389')

# 绑定（登录）
conn.simple_bind_s('cn=admin,dc=example,dc=com', 'password')

# 搜索用户
base_dn = 'dc=example,dc=com'
search_filter = '(uid=username)'
result = conn.search_s(base_dn, ldap.SCOPE_SUBTREE, search_filter)
```

## 主要功能模块

1. **连接管理**
   - 服务器连接
   - 认证绑定
   - 连接池管理

2. **用户操作**
   - 用户查询
   - 用户添加
   - 用户修改
   - 用户删除

3. **组织管理**
   - 组织单位查询
   - 组织架构管理
   - 组成员管理

## 注意事项

- 确保LDAP服务器地址正确
- 使用适当的认证凭据
- 注意权限设置
- 遵循安全最佳实践

## 错误处理

常见错误及解决方案：
- 连接失败：检查服务器地址和端口
- 认证失败：验证用户名和密码
- 权限错误：检查用户权限设置

## 安全建议

1. 使用SSL/TLS加密连接
2. 妥善保管认证信息
3. 实施适当的访问控制
4. 定期更新密码
5. 记录重要操作日志

## 贡献指南

欢迎提交问题和改进建议！

## 许可证

MIT License 