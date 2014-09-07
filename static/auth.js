var googleKey;
var facebookKey;


var ref = new Firebase("https://torid-heat-3815.firebaseio.com/");
var authClient = new FirebaseSimpleLogin(ref, function(error, user) {
    if (error) {
        console.log(error);
    } else if (user) {
        console.log("User ID: " + user.uid + ", Provider: " + user.provider);
        if(authClient.provider == 'google') {
            googleKey = user.accessToken;
            if(isnull(facebookKey)) {
                authFacebook();
            }
        } else {
            facebookKey = user.accessToken;
            if(isnull(googleKey)) {
                authGoogle();
            }
        }
    } else {
        
    }
});

function authGoogle(){
    authClient.login('google');

}

function authFacebook(){
    authClient.login('facebook');

}

function loggedIn(){
    var url = sprintf("http://centiment.me/dashboard?google=%s&facebook=%s", googleKey, facebookKey);
    window.location.replace(url);
}

$(document).ready(function(){
    console.log("signing in");
    $("#logIn").click(function(){
        authGoogle();
    });
});
