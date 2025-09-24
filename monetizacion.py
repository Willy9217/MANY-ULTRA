import stripe
import os

stripe.api_key = os.environ.get("STRIPE_API_KEY")  # Tu API Key de Stripe

def crear_pago_empresa(empresa_email, monto_usd):
    """Crea un link de pago para una empresa"""
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {'name': f'Monetización {empresa_email}'},
                    'unit_amount': int(monto_usd * 100),  # convertir USD a centavos
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='https://tu-web-exito.com/success',
            cancel_url='https://tu-web-exito.com/cancel',
        )
        return checkout_session.url
    except Exception as e:
        return str(e)
