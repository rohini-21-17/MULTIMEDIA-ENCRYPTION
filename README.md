# MULTIMEDIA-ENCRYPTION
A secure multimedia encryption application that enables safe transmission of images, audio, and video files using cryptographic techniques. Features sender-receiver authentication, key-based decryption, and MySQL database integration built with Flask.


🔐 Multimedia Encryption System (Image, Audio, Video)

A secure Multimedia Encryption System that encrypts and decrypts Images, Audio, and Video files using cryptographic techniques. The system allows secure communication between sender and receiver.

🚀 Features
🔐 Image Encryption & Decryption
🎵 Audio Encryption & Decryption
🎥 Video Encryption & Decryption
👤 Sender & Receiver Authentication
🛡️ Secure Key Generation
📂 File Upload & Download
📊 Admin Dashboard
🗄️ MySQL Database Integration

🏗️ Project Architecture
User → Flask Application → Encryption Module → Database → Receiver

🧰 Tech Stack
Python
Flask
MySQL
HTML
CSS
Bootstrap
Cryptography (ECIES)

The application uses Flask routes and MySQL database connection for user authentication and file encryption workflows.

📂 Project Structure
Multimedia-Encryption
│
├── app.py
├── database.sql
│
├── templates
│   ├── index.html
│   ├── AdminLogin.html
│   ├── SenderLogin.html
│   ├── ReceiverLogin.html
│
├── static
│   ├── css
│   ├── upload
│
└── README.md
⚙️ Installation
1. Clone Repository
git clone https://github.com/your-username/multimedia-encryption.git
2. Install Requirements
pip install flask mysql-connector-python eciespy
3. Setup Database
Import SQL file into MySQL:
database.sql
4. Run Application
python app.py

🔑 Login Credentials
Admin
Username: admin
Password: admin

🎯 Functional Modules
👤 Admin
View Senders
View Receivers
View Messages
📤 Sender
Login
Upload Image
Upload Audio
Upload Video
Encrypt File
📥 Receiver
Login
Receive File
Decrypt File

🔐 Encryption Method
ECIES Encryption
Key-based secure communication
File-based encryption


👩‍💻 Author
Rohini M
GitHub: https://github.com/rohini-21-17
LinkedIn: https://linkedin.com/in/rohini-m21

⭐ If you like this project
Give it a ⭐ on GitHub!
