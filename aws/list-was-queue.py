# This script created a queue
#
# Author - Paul Doyle Aug 2013
#
#
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

conn = boto.sqs.connect_to_region("ireland-1", aws_access_key_id='AKIAJ2BJXBF74JPNZKCQ', aws_secret_access_key='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')

rs = conn.get_all_queues()
for q in rs:
	print q.id

#i think this is correct for creating a queue, this 120 represents how long
#a message is invisable to other queues once read
q=conn.create_queue('myqueue',120)


#writing message
m=message()
m.set_body('my first message')
q.write(m)

#to remove message from queue
q.delete_message(m)

# to delete whole queue
conn.delete_queue(q)›
