from constance import config
from django.utils.timezone import now

from apps.cart import models

CART_ID = 'CART-ID'


class ItemAlreadyExists(Exception):
    pass


class ItemDoesNotExist(Exception):
    pass


class Cart:
    def __init__(self, request):
        cart_id = request.session.get(CART_ID)
        if cart_id:
            try:
                cart = models.Cart.objects.get(id=cart_id, checked_out=False)
            except models.Cart.DoesNotExist:
                cart = self.new(request)
        else:
            cart = self.new(request)
        self.cart = cart

    def __iter__(self):
        for item in self.cart.item_set.all():
            yield item

    def new(self, request):
        cart = models.Cart(creation_date=now())
        cart.save()
        request.session[CART_ID] = cart.id
        return cart

    def add(self, product, unit_price, quantity=1, size=None):
        try:
            item = models.Item.objects.get(
                cart=self.cart,
                product=product,
                selected_size=size,
            )
        except models.Item.DoesNotExist:
            item = models.Item()
            item.cart = self.cart
            item.product = product
            item.unit_price = unit_price
            item.quantity = quantity
            item.selected_size = size
            item.save()
        else:  # ItemAlreadyExists
            item.unit_price = unit_price
            item.quantity = item.quantity + int(quantity)
            item.save()

    def remove(self, product, size=None):
        try:
            item = models.Item.objects.get(
                cart=self.cart,
                product=product,
                selected_size=size,
            )
        except models.Item.DoesNotExist:
            raise ItemDoesNotExist
        else:
            item.delete()

    def update(self, product, quantity, unit_price=None, size=None):
        try:
            item = models.Item.objects.get(
                cart=self.cart,
                product=product,
                selected_size=size,
            )
        except models.Item.DoesNotExist:
            raise ItemDoesNotExist
        else:  # ItemAlreadyExists
            if quantity == 0:
                item.delete()
            else:
                item.unit_price = unit_price
                item.quantity = int(quantity)
                item.save()

    def count(self):
        result = 0
        for item in self.cart.item_set.all():
            result += 1 * item.quantity
        return result

    @property
    def subtotal(self):
        result = 0
        for item in self.cart.item_set.all():
            result += item.total_price
        return float(result)

    @property
    def has_magazine_only(self):
        for item in self.cart.item_set.all():
            if hasattr(item.get_product(), 'product'):
                return False
        return True

    @property
    def tps(self):
        return 0.05 * self.subtotal

    @property
    def shipping(self):
        if self.has_magazine_only:
            return config.SHIPPING_COST + config.SHIPPING_EXTRA
        return config.SHIPPING_COST

    @property
    def tvq(self):
        return 0.09975 * self.subtotal

    @property
    def total(self):
        return self.subtotal + self.tps + self.tvq + self.shipping

    def clear(self):
        for item in self.cart.item_set.all():
            item.delete()
