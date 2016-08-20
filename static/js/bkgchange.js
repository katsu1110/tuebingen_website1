$( '#bkgchange' ).click(function() {
    var array = [
    "../../static/gallary/suzu1.jpg",
    "../../static/gallary/suzu2.jpg",
    "../../static/gallary/suzu3.jpg",
    "../../static/gallary/suzu5.jpg",
    "../../static/gallary/suzu7.jpg",
    "../../static/gallary/suzu8.jpg",
    "../../static/gallary/suzu9.jpg",
    "../../static/gallary/suzu10.jpg",
    "../../static/gallary/suzu14.jpg",
    "../../static/gallary/suzu16.jpg",
    "../../static/gallary/suzu17.jpg",
    "../../static/gallary/suzu18.jpg",
    "../../static/gallary/suzu19.jpg",
    "../../static/gallary/suzu23.jpg",
    "../../static/gallary/suzu24.jpg",
    "../../static/gallary/masa1.jpg",
    "../../static/gallary/masa2.jpg",
    "../../static/gallary/masa3.jpg",
    "../../static/gallary/masa4.jpg",
    "../../static/gallary/masa5.jpg",
    "../../static/gallary/masa6.jpg",
    "../../static/gallary/masa7.jpg",
    "../../static/gallary/me5.jpg",
    "../../static/gallary/me7.jpg",
    "../../static/gallary/me8.jpg",
    "../../static/gallary/me9.jpg",
    ];
    var l = array.length;
    var r = Math.floor(Math.random()*l);
    var imgurl = array[r];
    $("body").css({
      'background-size': "cover",
      'background-attachment': "fixd",
      'background-image': ('url("'+imgurl+'")')});

});
