class SchedulerConfig(object):
    """
    定时任务配置
    """
    JOBS = [
        {
            'id': 'sync_wx_user',  # 任务id
            'func': 'task',  # 任务执行程序
            'trigger': 'interval',  # 任务执行类型，定时器
            'seconds': 5,  # 任务执行时间，单位秒
        }
    ]


class Wx:
    """
    微信配置信息
    """
    CORP_ID = 'wle4845bc753'  # corpid
    CORP_SECRET = 'pIGgS5eyArxBzeLRQRXmtfFvh7bUICfO_ska0aFZeFw'  # corpsecret
