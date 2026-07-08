// firebase-config.js
// Initializes Firebase (loaded via CDN, no build step / npm needed).
// This file is imported by both login.html (auth.js) and every other
// page (nav-auth.js) so there is ONE shared Firebase instance.

import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";
import { getAuth, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-auth.js";
import { getAnalytics, isSupported } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-analytics.js";

// NOTE: This config (and the apiKey) is safe to expose in client-side code.
// Firebase Web API keys are not secret — real protection comes from
// Authorized Domains + Firebase Security Rules, which we set up separately.
const firebaseConfig = {
  apiKey: "AIzaSyCnHysvMCU1tYf0TRLRuu5gk_s7GEYmvdw",
  authDomain: "incredible-india-explore.firebaseapp.com",
  projectId: "incredible-india-explore",
  storageBucket: "incredible-india-explore.firebasestorage.app",
  messagingSenderId: "374198923456",
  appId: "1:374198923456:web:b181b0a15f3184b5867d25",
  measurementId: "G-RD0LYL477T"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
const googleProvider = new GoogleAuthProvider();

// Analytics only works on https/localhost and some browsers block it —
// isSupported() prevents a console error if it's blocked.
isSupported().then((supported) => {
  if (supported) getAnalytics(app);
}).catch(() => {
  /* analytics blocked (adblock/private mode) — safe to ignore */
});

export { app, auth, googleProvider };