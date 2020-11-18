'''
数据库操作
1. 数据库从mysql->换成sqlite, 脚本层不需要改动，只需要改动caw里面的mysqlop.py这个文件。
2. 这一部分访问到业务的数据库，所以放在baw中。（维护方便，涉及到数据库变更方面，修改的地方少）
'''
from ZongHe.caw import MySqlOp


def deleteUser(db, phone):
    '''
    根据手机号删除用户
    :param db: 一个字典，存储数据库信息
    :param phone: 手机号
    :return:
    '''
    conn = MySqlOp.connect(db)
    MySqlOp.execute(conn, f'delete from Member where MobilePhone={phone};')
    MySqlOp.disconnect(conn)

