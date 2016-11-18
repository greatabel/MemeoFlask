function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi,    
    function(m,key,value) {
      vars[key] = value;
    });
    return vars;
  }


var url = "http://139.224.73.50"
url = "http://127.0.0.1:5000"
document.getElementById("content").innerHTML= window.location.href + '<br/>'+navigator.userAgent.toLowerCase();

$.getJSON( url+ '/api/childpicture/1', function(data) {
    console.log('here')
document.getElementById("ItemPreview").src = "data:;base64," + data['IMAGE_DATA'];

});


$.getJSON( url + '/api/userchild/0', function(data) {
console.log(data);
});
