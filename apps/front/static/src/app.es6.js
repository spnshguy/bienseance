import {FormAjax} from './tools/form.ajax.es6';
import cookie from './tools/cookie.es6';
import ui from './ui.es6';

const NEWSLETTER_FORM = '#newsletter_form';
const CONTACT_FORM = '#contact_form';

$(document).ready(function(){
    let csrf = cookie.getCookie('csrftoken');
    $.ajaxSetup({ headers : {'X-CSRFToken': csrf }});

    ui.ready();
    if ($(document).innerWidth()< 768) {
        $('.btn-burger').click(()=> {
            $('.burger').toggleClass('active');
            let height = $('.header-link-content').css('height');
            if ($('.burger').hasClass('active')){
                $('.header-link-container').css('height',height).css('opacity',1);
            }else{
                $('.header-link-container').css('height', 0).css('opacity', 0);

            }
        });
    } else{
        $('.header-link-container').css('height', 'auto').css('opacity',1);

    }
    $(".burger").click(function(e){
        $(".burger").toggleClass("active")
        $(".main-menu").toggleClass("active")

    });
    if ($('.instagram-images-section').length) {
        $('.image-container').slick({
            mobileFirst:true,
            arrows: true,
            infinite: true,
            slidesToShow: 1,
            responsive: [
                {
                    breakpoint: 1200,
                    settings: {
                        arrows: true,
                        slidesToShow: 6,
                    }
                },
                {
                    breakpoint: 992,
                    settings: {
                        arrows: true,
                        slidesToShow: 4,
                    }
                },
                {
                    breakpoint: 768,
                    settings: {
                        arrows: true,
                        slidesToShow: 3
                    }
                },
                {
                    breakpoint: 480,
                    settings: {
                        arrows: true,
                        slidesToShow: 2
                    }
                }
          ]
        });
    }
    if ($(NEWSLETTER_FORM).length) {

        new FormAjax($(NEWSLETTER_FORM), (response, e) => {
            $('.newsletter-form-container').prepend("<p class='text-center'>" + response.message + '<p>')
        });
    }
    if ($(CONTACT_FORM).length) {
        console.log($(CONTACT_FORM).find('input'))
        $(CONTACT_FORM).find('input').on('keyup', function(e) {

            if ($(e.currentTarget).val() != ''){
                $(e.currentTarget).addClass('has-content');
            } else {
                $(e.currentTarget).removeClass('has-content');
            }

        });
        $(CONTACT_FORM).find('textarea').on('keyup', function(e) {
            if ($(e.currentTarget).val() != ''){
                $(e.currentTarget).addClass('has-content');
            } else {
                $(e.currentTarget).removeClass('has-content');
            }

        });
        new FormAjax($(CONTACT_FORM), (response, e) => {
            $(CONTACT_FORM)[0].reset();
            $('.contact-form-container').find(".success-message").remove();
            $('.contact-form-container').prepend("<p class='text-center success-message'>" + response.message + '<p>')
        });
    }
});


$(window).on('load', () => {
    ui.loaded();
});