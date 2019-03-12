$(function () {
    $('.cart').width(innerWidth)
    total()
    $('li .confirm-wrapper').click(function () {
        $span = $(this).find('span')
        // $(this).find('span').removeClass('glyphicon-ok').addClass('no')
        request_data = {
            'cartid': $(this).attr('data-cardid')
        }
        $.get('/changecartselect/', request_data, function (response) {
            if (response.status == 1) {
                if (response.value) {
                    $span.removeClass('no').addClass('glyphicon glyphicon-ok')
                } else {
                    $span.removeClass('glyphicon glyphicon-ok').addClass('no')
                }
                total()
            }

        })

    })


    $('.cart .all').click(function () {
        var isall = $(this).attr('data-all')
        $span = $(this).find('span')

        isall = (isall == 'false') ? true : false

        $(this).attr('data-all', isall)

        if (isall) {
            $span.removeClass('no').addClass('glyphicon glyphicon-ok')
        } else {
            $span.removeClass('glyphicon glyphicon-ok').addClass('no')
        }
        total()
        request_data = {
            'isall': isall
        }

        $.get('/allselect/', request_data, function (response) {

            if (response.status == 1) {
                $('.confirm-wrapper').each(function () {
                    if (isall) {
                        $(this).find('span').removeClass('no').addClass('glyphicon glyphicon-ok')
                    } else {
                        $(this).find('span').removeClass('glyphicon glyphicon-ok').addClass('no')
                    }
                    total()

                })
            }
        })
    })


    function total(){


        $.get('/total/', function (response) {
            $('#all_price').html(response.sum)
        })
    }
})