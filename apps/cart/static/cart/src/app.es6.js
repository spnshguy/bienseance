import {FormAjax} from './../../../../front/static/src/tools/form.ajax.es6';

const CART_FORM = '.cart-item-form'
const CART_SECTION = '.shopping-cart'
const ITEM_QUANTITY_INPUT = '.item-quantity'


if ($(ITEM_QUANTITY_INPUT).length) {
    $(CART_SECTION).on('change', ITEM_QUANTITY_INPUT, (e)=>{
        new FormAjax($(e.currentTarget).closest(CART_FORM), (response, e) => {
            $(CART_SECTION).html(response.template)
        });
        $(e.currentTarget).closest(CART_FORM).submit();
    })
    $(CART_SECTION).on('click', '.remove-product', (e)=>{
        $.ajax({
            method: 'POST',
            url: $(e.currentTarget).data('url'),
            success: (response) => {
                $(CART_SECTION).html(response.template)
            },
            error: (response) => {
            }
        });
    });
}

