from .models import Order


def create_order(raw_data: dict):
    order_data = dict(
        customer_name=raw_data.get('customer_name'),
        delivery_time=raw_data.get('delivery_time') or None,
        delivery_address=raw_data.get('delivery_address') or None,
        user_email=raw_data.get('user_email') or None,
        user_phone=raw_data.get('user_phone_0') + raw_data.get('user_phone_1'),
    )
    Order.objects.create(**order_data)
