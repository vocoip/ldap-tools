from ldap3 import Server, Connection, ALL, NTLM, SIMPLE, ANONYMOUS, SUBTREE
import logging
import yaml
import os

class LDAPClient:
    def __init__(self, config_path='config.yaml'):
        """
        初始化LDAP客户端
        :param config_path: 配置文件路径
        """
        self.config = self._load_config(config_path)
        self.conn = None
        self._setup_logging()

    def _load_config(self, config_path):
        """
        加载配置文件
        :param config_path: 配置文件路径
        :return: dict 配置信息
        """
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            return config['ldap']
        except Exception as e:
            raise Exception(f"加载配置文件失败: {str(e)}")

    def _setup_logging(self):
        """
        设置日志
        """
        log_config = self.config['logging']
        logging.basicConfig(
            level=getattr(logging, log_config['level']),
            format=log_config['format'],
            filename=log_config['file'],
            encoding='utf-8'
        )
        self.logger = logging.getLogger(__name__)

    def _get_auth_method(self, auth_type):
        """
        获取认证方法
        :param auth_type: 认证类型字符串
        :return: 认证方法对象
        """
        auth_methods = {
            'NTLM': NTLM,
            'SIMPLE': SIMPLE,
            'ANONYMOUS': ANONYMOUS
        }
        return auth_methods.get(auth_type.upper(), NTLM)

    def connect(self):
        """
        连接到LDAP服务器
        :return: bool 连接是否成功
        """
        try:
            server_config = self.config['server']
            auth_config = self.config['auth']

            # 创建服务器对象
            server = Server(
                server_config['url'],
                get_info=ALL,
                use_ssl=server_config['use_ssl'],
                connect_timeout=server_config['timeout']
            )
            
            # 创建连接对象
            self.conn = Connection(
                server,
                user=auth_config['username'],
                password=auth_config['password'],
                authentication=self._get_auth_method(auth_config['authentication']),
                auto_bind=True
            )
            
            self.logger.info(f"成功连接到LDAP服务器: {server_config['url']}")
            return True
            
        except Exception as e:
            self.logger.error(f"连接LDAP服务器失败: {str(e)}")
            return False

    def search_users(self, search_filter=None):
        """
        搜索用户
        :param search_filter: 搜索过滤器，如果为None则使用默认过滤器
        :return: list 搜索结果
        """
        try:
            if not self.conn:
                self.logger.error("未连接到LDAP服务器")
                return []

            search_config = self.config['search']
            filter_to_use = search_filter or search_config['default_filter']

            # 执行搜索
            self.conn.search(
                search_base=search_config['base_dn'],
                search_filter=filter_to_use,
                search_scope=SUBTREE,
                attributes=search_config['attributes']
            )

            # 获取搜索结果
            results = []
            for entry in self.conn.entries:
                result = {'dn': entry.entry_dn}
                for attr in search_config['attributes']:
                    result[attr] = getattr(entry, attr).value if hasattr(entry, attr) else None
                results.append(result)

            self.logger.info(f"搜索到 {len(results)} 个用户")
            return results

        except Exception as e:
            self.logger.error(f"搜索用户失败: {str(e)}")
            return []

    def close(self):
        """
        关闭LDAP连接
        """
        if self.conn:
            self.conn.unbind()
            self.logger.info("LDAP连接已关闭")

def main():
    # 使用示例
    try:
        # 创建LDAP客户端
        ldap_client = LDAPClient()

        # 连接服务器
        if ldap_client.connect():
            # 搜索用户
            users = ldap_client.search_users()

            # 打印搜索结果
            for user in users:
                print("\n用户信息:")
                for key, value in user.items():
                    print(f"{key}: {value}")
                print("-" * 50)

            # 关闭连接
            ldap_client.close()

    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == '__main__':
    main() 