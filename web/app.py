#coding:UTF-8
#Last Change: 20210312

import logging
from aiohttp import web


logging.basicConfig(level=logging.INFO)  # 配置logging的基本信息， level=logging.INFO,记录INFO及以上的日志


def index(request):
    return web.Response(body='<h1>This is a test index of the project</h1>'.encode('utf-8'), content_type='text/html')

def init():
    app = web.Application()
    app.router.add_route('GET', '/', index)
    web.run_app(app, host='127.0.0.1', port=9000)
    logging.info('server started at http://127.0.0.1:9000...')

init()