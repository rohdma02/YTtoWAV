
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-app.js";
import { getAuth, GoogleAuthProvider, signInWithPopup } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-auth.js";


const firebaseConfig = {
    apiKey: "AIzaSyApvj8RAOZja4-xYmtCYBVJq5hyy9_dK_8",
    authDomain: "purplemusic-login.firebaseapp.com",
    projectId: "purplemusic-login",
    storageBucket: "purplemusic-login.appspot.com",
    messagingSenderId: "183024460646",
    appId: "1:183024460646:web:19903a37f24118f7cd1ea7"
};


const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
auth.languageCode = 'en';
const provider = new GoogleAuthProvider();

const googleLogin = document.getElementById("google-login-btn");
googleLogin.addEventListener("click", function () {
    signInWithPopup(auth, provider)
        .then((result) => {
            // This gives you a Google Access Token. You can use it to access the Google API.
            const credential = GoogleAuthProvider.credentialFromResult(result);
            const token = credential.accessToken;
            const user = result.user;
            console.log(user);

            // Send the user data to the Flask route
            const userData = {
                userName: user.displayName,
                userEmail: user.email,
                userProfilePicture: user.photoURL
            };
            const queryParams = new URLSearchParams(userData).toString();
            window.location.href = `/logged?${queryParams}`;
        }).catch((error) => {
            // Handle Errors here.
            const errorCode = error.code;
            const errorMessage = error.message;
            // The email of the user's account used.
            const email = error.customData.email;
            // The AuthCredential type that was used.
            const credential = GoogleAuthProvider.credentialFromError(error);
            // ...
        });
})