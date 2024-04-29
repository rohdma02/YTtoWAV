
import { initializeApp } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-app.js";
import { getAuth, googleAuthProvider, signInWithPopup } from "https://www.gstatic.com/firebasejs/10.11.1/firebase-auth.js";


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
const provider = new googleAuthProvider();

const googleLogin = document.getElementById("google-login-btn");
googleLogin.addEventListener("click", function () {
    alert(5)
})
