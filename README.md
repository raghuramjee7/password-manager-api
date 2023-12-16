# Password Manager API

## Requirements
1. Users can store all their usernames and passwords securely for each site
2. Users generate their own private and public keys
3. The public key is a part of their profile, the private key stays with them
4. Whenever they upload data, its encrypted with their public key
5. Whenever they download data, its decrypted with their private key

## API
1. User registration
2. User login
3. User logout
4. Generate public and private keys
5. Upload data
6. Download data
    1. By ID
    2. By username
    3. By website