import aio_pika


async def publish_message_in_default_exc(amqp_channel: aio_pika.abc.AbstractChannel, message: str, routing_key: str):
    await amqp_channel.default_exchange.publish(aio_pika.Message(message.encode()), routing_key)


async def create_amqp_queue(amqp_channel: aio_pika.abc.AbstractChannel, queue_name: str):
    await amqp_channel.declare_queue(queue_name)
