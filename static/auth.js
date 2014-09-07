var googleKey = null;
var facebookKey = null;


var ref = new Firebase("https://torid-heat-3815.firebaseio.com/");
var authClient = new FirebaseSimpleLogin(ref, function(error, user) {
    if (error) {
        console.log(error);
    } else if (user) {
        console.log("User ID: " + user.uid + ", Provider: " + user.provider);
        if(user.provider == 'google') {
            googleKey = user.accessToken;
            if(null == facebookKey) {
                authFacebook();
            }
        } else {
            facebookKey = user.accessToken;
            if(null === googleKey) {
                authGoogle();
            }
        }
        if (googleKey != null and facebookKey != null) {
            //lookup table
            loggedIn();
        }
    }
    
});

function authGoogle(){
    authClient.logout();
    authClient.login('google');

}

function authFacebook(){
    authClient.logout();
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
