function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi,    
    function(m,key,value) {
      vars[key] = value;
    });
    return vars;
  }


document.getElementById("content").innerHTML= window.location.href + '<br/>'+navigator.userAgent.toLowerCase();

$.getJSON('http://127.0.0.1:5000/api/childpicture/5', function(data) {
document.getElementById("ItemPreview").src = "data:image/png;base64," + data['IMAGE_DATA'];

});
