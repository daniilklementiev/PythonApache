import appsetting
from ViewController import ViewController
import sys
sys.path.append('./')
import dao


class CartController (ViewController):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    def index(self):
        cart_items = dao.Cart.get_items('100630311758462981')
        if len(cart_items) != 0:
            with open(f"{appsetting.VIEWS_PATH}/cart/DisplayTemplates/cart-item.html", encoding="utf-8") as tpl:
                data_template = tpl.read()
            cart_item_views = []
            for cart_item in cart_items:
                cart_item_view = data_template
                for k, v in cart_item.items():
                    cart_item_view = cart_item_view.replace(f"{{{{{k}}}}}", str(v))
                cart_item_views.append(cart_item_view)

            # add total cnt
            total_cnt = 0
            total_price = 0
            for cart_item in cart_items:
                total_cnt += cart_item['cnt']
                current_price = cart_item['cnt'] * cart_item['price']
                total_price += current_price

            self.view_data['@total'] = total_cnt
            self.view_data['@summary'] = total_price
            self.view_data['@display_for_cart'] = ''.join(cart_item_views)

        print(list(cart_items))
        self.return_view()
