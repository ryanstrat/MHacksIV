var googleKey = null;


var ref = new Firebase("https://torid-heat-3815.firebaseio.com/");
var authClient = new FirebaseSimpleLogin(ref, function(error, user) {
    if (error) {
        console.log(error);
    } else if (user) {
        console.log("User ID: " + user.uid + ", Provider: " + user.provider);
        if(user.provider == 'google') {
            googleKey = user.accessToken;
            authFacebook();
        }
        loggedIn()
    }
    
});

function authGoogle(){
    authClient.logout();
    setTimeout(function() {
        authClient.login('google');
    }, 2000);

}

function loggedIn(){
    var url = sprintf("http://centiment.me/dashboard?google=%s", googleKey);
    window.location.replace(url);
}

$(document).ready(function(){
    console.log("signing in");
    $("#logIn").click(function(){
        authGoogle();
    });
});
