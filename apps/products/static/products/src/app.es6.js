import {FormAjax} from './../../../../front/static/src/tools/form.ajax.es6';

const PRODUCT_FILTER_FORM = '#product_filter_form'
const PRODUCT_ORDER_FORM = '#product-order-form'
const PRODUCT_ORDER_ID = '#id_order'
const PRODUCT_FILTER_DESIGNER = '#id_designer'
const PRODUCT_FILTER_TAG = '#id_tag'


$(PRODUCT_ORDER_ID).on('change', () => {
    $(PRODUCT_FILTER_FORM).submit()
});
$(PRODUCT_FILTER_DESIGNER).on('change', () => {
    $(PRODUCT_FILTER_FORM).submit()
});
$(PRODUCT_FILTER_TAG).on('change', () => {
    $(PRODUCT_FILTER_FORM).submit()
});

if ($(PRODUCT_FILTER_FORM).length) {
    new FormAjax($(PRODUCT_FILTER_FORM), (response, e) => {
        $('.product_listing').html(response.template)
    });
}
if ($(PRODUCT_ORDER_FORM).length) {
    new FormAjax($(PRODUCT_ORDER_FORM), (response, e) => {
        window.location.href = response.success_url;
    });
}

