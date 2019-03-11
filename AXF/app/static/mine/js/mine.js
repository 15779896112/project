$(function () {
    $('.mine').width(innerWidth)
    $('#aa').click(function () {
        $.cookie('back', 'mine', {expires: 3, path: '/'})
        window.open('/login/', '_self')
    })


})