$(function () {
    $('.home').width(innerWidth)
    var swiper = new Swiper('#topSwiper', {
        pagination: '.swiper-pagination',
        paginationClickable: '.swiper-pagination',
        spaceBetween: 30,
        loop: true,
        autoplay:2000,
    });



   var swiper = new Swiper('#mustbuySwiper', {
    pagination: '.swiper-pagination',
    paginationClickable: '.swiper-pagination',
    spaceBetween: 5,
    loop: true,
    autoplay:2000,
       slidesPerView:3,
});
})
