ITEM_PIPELINES = ['headlines.pipelines.HeadlinesPipeline']

BOT_NAME = 'headlines'

SPIDER_MODULES = ['headlines.spiders']

DATABASE = {
	'drivername': 'postgres',
	'host': 'localhost',
	'port': '5432',
	'username': 'postgres',
	'password': 'postgres',
	'database': 'headlines'
	}
