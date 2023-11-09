import pika, json

params = pika.URLParameters('amqps://xaavqxcz:EBu3nPBPOiayJAbRRZ8oImQe1kCzfjLX@shrimp.rmq.cloudamqp.com/xaavqxcz')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
