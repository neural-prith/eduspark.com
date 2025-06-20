# Firebase Authentication Setup Guide

## Overview
This guide will help you set up Firebase Authentication for the EDU SPARK platform with Google and Facebook social login support.

## Prerequisites
- Firebase Project
- Google Cloud Project (automatically created with Firebase)
- Facebook Developer Account (for Facebook login)

## Step 1: Create Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Create a project"
3. Enter project name: `eduspark-agriculture` (or your preferred name)
4. Enable Google Analytics (optional)
5. Create project

## Step 2: Enable Authentication Methods

1. In Firebase Console, go to **Authentication** > **Sign-in method**
2. Enable the following providers:
   - **Email/Password**: Enable
   - **Google**: Enable and configure
   - **Facebook**: Enable and configure with App ID and App Secret

### Configure Google Authentication
1. Google provider is automatically configured with Firebase
2. Add your domain to authorized domains if needed

### Configure Facebook Authentication
1. Go to [Facebook Developers](https://developers.facebook.com/)
2. Create a new app or use existing
3. Add Facebook Login product
4. Copy App ID and App Secret
5. In Firebase, paste these credentials
6. Add Firebase OAuth redirect URL to Facebook app settings

## Step 3: Create Service Account

1. Go to Firebase Console > **Project Settings** > **Service Accounts**
2. Click **Generate New Private Key**
3. Download the JSON file
4. Keep this file secure - it contains sensitive credentials

## Step 4: Frontend Configuration

Update the Firebase configuration in your HTML files:

```javascript
const firebaseConfig = {
    apiKey: "your-api-key",
    authDomain: "your-project-id.firebaseapp.com",
    projectId: "your-project-id",
    storageBucket: "your-project-id.appspot.com",
    messagingSenderId: "your-sender-id",
    appId: "your-app-id"
};
```

Replace the placeholder values in:
- `templates/api_login_enhanced.html`
- `templates/api_signup_enhanced.html`

## Step 5: Backend Configuration

Set up environment variables for the backend. Create a `.env` file:

```env
# Firebase Admin SDK Configuration
FIREBASE_PROJECT_ID=your-project-id
FIREBASE_PRIVATE_KEY_ID=your-private-key-id
FIREBASE_PRIVATE_KEY="-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY_HERE\n-----END PRIVATE KEY-----\n"
FIREBASE_CLIENT_EMAIL=firebase-adminsdk-xxxxx@your-project-id.iam.gserviceaccount.com
FIREBASE_CLIENT_ID=your-client-id
FIREBASE_CLIENT_CERT_URL=https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-xxxxx%40your-project-id.iam.gserviceaccount.com
```

**Important**: Replace all placeholder values with actual values from your service account JSON file.

## Step 6: Install Dependencies

Install Firebase dependencies:

```bash
pip install -r firebase_requirements.txt
```

## Step 7: Security Rules (Optional)

If using Firestore database, set up security rules:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{userId} {
      allow read, write: if request.auth != null && request.auth.uid == userId;
    }
  }
}
```

## Step 8: Testing

1. Start your Flask application
2. Navigate to `/api_login_enhanced.html`
3. Test email/password authentication
4. Test Google social login
5. Test Facebook social login

## Troubleshooting

### Common Issues:

**Firebase Admin SDK not initialized**
- Check that all environment variables are set correctly
- Verify the private key format (should include `\n` for line breaks)

**Invalid domain for OAuth**
- Add your domain to Firebase Authentication > Settings > Authorized domains

**Facebook login not working**
- Verify Facebook App ID and Secret in Firebase Console
- Check that Facebook app is live (not in development mode)
- Ensure OAuth redirect URLs are configured correctly

**Token verification failed**
- Check that the frontend Firebase config matches your project
- Verify that the ID token is being sent correctly to the backend

## Security Best Practices

1. **Never expose service account keys**: Keep the private key secure and use environment variables
2. **Use HTTPS**: Always use HTTPS in production for secure authentication
3. **Validate tokens**: Always verify Firebase ID tokens on the backend
4. **Set token expiration**: Configure appropriate token expiration times
5. **Monitor authentication**: Use Firebase Console to monitor authentication events

## Production Deployment

1. Set up proper environment variable management
2. Use a secret management service for sensitive credentials
3. Enable Firebase Security Rules
4. Set up monitoring and logging
5. Configure proper CORS policies
6. Use a reverse proxy (nginx) for production serving

## Support

For issues with Firebase setup:
- [Firebase Documentation](https://firebase.google.com/docs)
- [Firebase Support](https://firebase.google.com/support)

For issues with this implementation:
- Check the console logs in browser developer tools
- Check the Flask application logs
- Verify all configuration values are correct 