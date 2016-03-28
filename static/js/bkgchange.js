$( '#bkgchange' ).click(function() {
    var array = [
    "../../static/gallary/suzu1.jpg",
    "../../static/gallary/suzu2.jpg",
    "../../static/gallary/suzu3.jpg",
    "../../static/gallary/suzu4.jpg",
    "../../static/gallary/suzu5.jpg",
    "../../static/gallary/suzu6.jpg",
    "../../static/gallary/suzu7.jpg",
    "../../static/gallary/suzu8.jpg",
    "../../static/gallary/suzu9.jpg",
    "../../static/gallary/suzu10.jpg",
    "../../static/gallary/suzu10.jpg",
    "../../static/gallary/suzu11.jpg",
    "../../static/gallary/suzu12.jpg",
    "../../static/gallary/suzu13.jpg",
    "../../static/gallary/suzu14.jpg",
    "../../static/gallary/suzu15.jpg",
    "../../static/gallary/suzu16.jpg",
    "../../static/gallary/me1.jpg",
    "../../static/gallary/me3.jpg",
    ];
    var l = array.length;
    var r = Math.floor(Math.random()*l);
    var imgurl = array[r];
    $("body").css({
      'background-size': "100%",
      'background-attachment': "fixd",
      'background-image': ('url("'+imgurl+'")')});

});
