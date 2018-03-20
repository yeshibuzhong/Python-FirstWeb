import www.orm as orm, asyncio, logging
from www.models import User, Blog, Comment

import asyncio
import sys

async def test(loop):
    # 创建连接池
    db_dict = {'user': 'root', 'password': 'root', 'db': 'awesome'}
    await orm.create_pool(loop=loop, **db_dict)

    u = User(name='Test1', email='test@example.com4', passwd='123425678901', image='about:blank1')
    await u.save()
    await orm.close_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
