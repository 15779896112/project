$(function () {
    index = $.cookie('index')
    if (index) {
        $('.market .type-slider li').eq(index).addClass('active')
    } else {
        $('.market .type-slider li').eq(0).addClass('active')
    }
    $('.market .type-slider li ').click(function () {

        $.cookie('index', $(this).index(), {expires: 3, path: '/'})

    })
    var fenlei_vlue = false
    var paixu_vlue = false
    $('#fenlei').click(function () {
        fenlei_vlue ? f_none() : f_show()
        p_none()
        fenlei_vlue = !fenlei_vlue
        paixu_vlue = false


    })


    $('#paixu').click(function () {
        paixu_vlue ? p_none() : p_show()
        f_none()
        paixu_vlue = !paixu_vlue
        fenlei_vlue = false


    })

    function f_none() {
        $('.main-content  .fenlei').css('display', 'none')
        $('#fenlei i').removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up')
    }

    function f_show() {
        $('.main-content  .fenlei').css('display', 'block')
        $('#fenlei i').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')
    }

    function p_none() {
        $('.main-content  .paixu').css('display', 'none')
        $('#paixu i').removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up')
    }

    function p_show() {
        $('.main-content  .paixu').css('display', 'block')
        $('#paixu i').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')
    }


//////////////////////////////////////////////////////////////////////////////
  $('.bt-wrapper .num').each(function () {
        var num = parseInt($(this).html())
        if (num) {
            $(this).prev().show()
            $(this).show()
        } else {
            $(this).prev().hide()
            $(this).hide()
        }
    })


    $('.bt-wrapper>.glyphicon-plus').click(function () {

        productid = $(this).attr('productid')
        $that = $(this)
        data = {
            'productid': productid,

        }
        $.get('/addcart/', data, function (response) {
            if (response.value == 0) {
                $.cookie('back', 'market', {expires: 3, path: '/'})
                window.open('/login/', '_self')
            } else {
                $that.prev().prev().show()
                $that.prev().show()
                $that.prev().html(response.num)

            }
        })
    })


    $('.bt-wrapper>.glyphicon-minus').click(function () {

        productid = $(this).attr('productid')
        $that = $(this)
        data = {
            'productid': productid,
        }
        $.get('/delcart/', data, function (response) {
            $that.next().html(response.num)
            num = parseInt(response.num)
            if (num > 0) {

                $that.show()
                $that.next().show()
                $that.next().html(response.num)
            } else {
                $that.hide()
                $that.next().hide()
            }


        })
    })

  })