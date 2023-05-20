import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='test')

message = "Hello World!"
channel.basic_publish(exchange='', routing_key='test', body=message)
print(f"Sent {message}")

connection.close()