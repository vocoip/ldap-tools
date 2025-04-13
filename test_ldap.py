from ldap_connection import LDAPClient
import logging

def test_ldap_connection():
    try:
        # 创建LDAP客户端
        print("正在创建LDAP客户端...")
        ldap_client = LDAPClient()
        
        # 连接到LDAP服务器
        print("正在连接到LDAP服务器...")
        if ldap_client.connect():
            print("连接成功！")
            
            # 测试搜索用户
            print("\n正在搜索用户...")
            users = ldap_client.search_users()
            
            # 打印搜索结果
            print(f"\n找到 {len(users)} 个用户:")
            for user in users:
                print("\n用户信息:")
                for key, value in user.items():
                    print(f"{key}: {value}")
                print("-" * 50)
            
            # 关闭连接
            ldap_client.close()
            print("\n连接已关闭")
        else:
            print("连接失败！")
            
    except Exception as e:
        print(f"测试过程中发生错误: {str(e)}")

if __name__ == "__main__":
    test_ldap_connection() 