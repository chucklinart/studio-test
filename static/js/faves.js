  // Create cookie with name and json value

  function createCookie(name, value, days) {
    var expires = '',
    date = new Date();
    if (days) {
      date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
      expires = '; expires=' + date.toGMTString();
    }
    document.cookie = name + '=' + value + expires + '; path=/';
  }

  // Read cookie. Return value will be a json array of favorites

  function readCookie(name) {
    var nameEQ = name + '=',
    allCookies = document.cookie.split(';'),
    i,
    cookie;
    for (i = 0; i < allCookies.length; i += 1) {
      cookie = allCookies[i];
      while (cookie.charAt(0) === ' ') {
        cookie = cookie.substring(1, cookie.length);
      }
      if (cookie.indexOf(nameEQ) === 0) {
        return cookie.substring(nameEQ.length, cookie.length);
      }
    }
    return null;
  }
var faves = new Array();
faves = [];
// need to separate arrays to persist styles below
var faved = new Array();
faved = [];
  $(function(){
    $(document.body).on("click", ".fave", function(){
      var parentDiv = $(this).closest(".card-body");
      var numstring = parentDiv.prop('className');
      var num = numstring.replace('card-body comicnum', '');
      var img = parentDiv.find('img').prop('src');
      var alt = parentDiv.find('h5').text();
      var safe_title = parentDiv.find('h4').text();
      var fav = {'num':num, 'img':img, 'alt':alt, 'title':safe_title};
      faves.push(fav);
      var stringified = JSON.stringify(faves);
      createCookie('favecomics', stringified, 30);
      $(this).removeClass('fave');
      $(this).addClass('unfave');
    });
    $(document.body).on("click", ".unfave", function(){
      var id = $(this).data('id');
      faves.splice(id,1);
      var stringified = JSON.stringify(faves);
      createCookie('favecomics', stringified, 30);
      $(this).removeClass('unfave');
      $(this).addClass('fave');
    });
    $(document).ready(function() {
      faved = readCookie('favecomics');
      console.log(faved);
      $('.card-body').each(function() {
      	var numstring = $(this).prop('className');
        var num = numstring.replace('card-body comicnum', '');
        for(var i = 0; i < faved.length; i++) {
          if(faved[i].num == num) {
            console.log(faved[i].num);
            $(this).children('button').removeClass('.fave').addClass('.unfave');
          }
        } 
      });
    });
  });
