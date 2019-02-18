# -*- coding: utf-8 -*-



BOT_NAME = 'game_3dm'

SPIDER_MODULES = ['game_3dm.spiders']
NEWSPIDER_MODULE = 'game_3dm.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Redis 配置
#清空dupefilter缓存
SCHEDULER_FLUSH_ON_START = True

DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
SCHEDULER_PERSIST = True
REDIS_HOST = 'master'
REDIS_PORT = 6379
REDIS_PARAMS = {
    'password': '123456'
}


#输出文件编码设置
FEED_EXPORT_ENCODING = 'utf-8'


#pipelines设置
