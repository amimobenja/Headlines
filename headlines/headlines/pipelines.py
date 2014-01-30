from sqlalchemy.orm import sessionmaker
from models import Headlines, db_connect, create_headlines_table

class HeadlinesPipeline(object):
	def __init__(self):
		engine = db_connect()
		create_headlines_table(engine)
		self.Session = sessionmaker(bind=engine)
	
	def process_item(self, item, spider):
		session = self.Session()
		headline = Headlines(**item)
		
		try:
			session.add(headline)
			session.commit()
		except:
			session.rollback()
			raise
		finally:
			session.close()
		return item
