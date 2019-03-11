$(function () {
    $('.register').width(innerWidth)
    $('#name-tip1').blur(function () {
        var reg = new RegExp("^1[34578]\\d{9}$")
        if ($(this).val() == '') return
        if (!reg.test($(this).val())) {
            $('.form-group').eq(0).addClass('has-error')
            $('#name-tip2').addClass('glyphicon-remove')
        } else {

            $('.form-group').eq(0).removeClass('has-error').addClass('has-success')
            $('#name-tip2').removeClass('glyphicon-remove').addClass('glyphicon-ok')
            data = {
                'username': $(this).val()
            }
            $.get('/checketel/', data, function (response) {
                if (response.status) {
                    $('#name-tip1').attr('data-content', '恭喜你账号是可用').popover('hide')

                    $('#name-tip1').removeClass('has-error').addClass('has-success')
                    $('#name-tip2').removeClass('glyphicon-remove').addClass('glyphicon-ok')
                } else {    // 0不可用
                    $('#name-tip1').attr('data-content', '账号存在').popover('show')

                    $('#name-tip2').removeClass('has-success').addClass('has-error')
                    $('#name-tip2').removeClass('glyphicon-ok').addClass('glyphicon-remove')
                }
            })
        }
    })


    $('#password-tip1').blur(function () {
        var reg = new RegExp("^[a-zA-Z0-9_]{6,10}$")
        if ($(this).val() == '') return
        if (!reg.test($(this).val())) {
            $('.form-group').eq(1).addClass('has-error')
            $('#password-tip2').addClass('glyphicon-remove')
        } else {

            $('.form-group').eq(1).removeClass('has-error').addClass('has-success')
            $('#password-tip2').removeClass('glyphicon-remove').addClass('glyphicon-ok')
        }
    })

    $('#subButton').click(function () {

        var value = true

        $('.register .form-group').each(function () {
            if (!$(this).is('.has-success')) {
                value = false
            }
        })

        if (value) {
            $('.register form').submit()
        }
    })


})




