
# 🧠 CCC Course Availability Detector

This project is an automated **Core Common Curriculum (CCC) course detector** for **Shiv Nadar University (SNU)**.  
It monitors the **ERP course catalog** in real-time and **sends an email notification** whenever a CCC course becomes available (i.e., a seat opens up because someone dropped it).  

It uses **Selenium** for automation, **SMTP** for email alerts, and **dotenv** for secure credential management.  

---

## 🧩 Project Structure

```
ccc-course-detector/
│
├── main.ipynb # Main program (runs the detector using Selenium)
├── mail.py # Handles sending email notifications
├── requirements.txt # Python dependencies
├── .env # User’s email credentials (not to be shared)
└── README.md # Documentation
```
---



---
## 🧰 Notes

- Make sure your internet connection is stable — Selenium relies on live page access.

- Keep your .env file private and never push it to public repositories.

- If the SNU ERP layout changes, you may need to update the CSS selectors in main.ipynb.

- To change refresh frequency, modify the time.sleep(60) value.




## 🚀 Features

- ✅ Automatically logs into the **SNU ERP** portal.
- 🔁 Continuously monitors **Core Common Curriculum (CCC)** courses.
- 🧩 Detects **newly opened** and **closed** courses in real-time.
- 📧 Sends **instant email notifications** when new seats become available.
- 🔒 Stores sensitive data (email/passwords) safely in a `.env` file.

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`SENDER_EMAIL=your_email@gmail.com`

`SENDER_PASSWORD=your_app_password`

`RECEIVER_EMAIL=receiver_email@gmail.com`

> ⚠️ **Important:**
> 
> - Do **not** use your regular email password.
> - If using Gmail, [create an App Password](https://myaccount.google.com/apppasswords).

---
## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/CCC-Course-Detector.git
cd ccc-course-detector
```

### 2. Install Dependencies

Make sure you have Python 3.8+ and pip installed.

Then run:

```
pip install -r requirements.txt
```

Your ```requirements.txt``` should include:
```
python-dotenv
```

### 3. ChromeDriver Setup

- Download [ChromeDriver](https://googlechromelabs.github.io/chrome-for-testing/) that matches your Chrome version.
- Add ChromeDriver to your system PATH so Selenium can access it.

---
## 🧠 How It Works

1. Logs into the **SNU ERP** automatically using **Selenium**.  
2. Navigates to the course catalog and searches for _Core Common Curriculum_.  
3. Every 60 seconds, it refreshes the page and checks for changes in course availability.  
4. When new courses open up, it triggers `mail.py` to send an email notification.

---

## 📧 Email Notification Format

When a new CCC course opens, you’ll receive an email like this:

**Subject:**
```
New University Courses Available!
```
**Body**
```
The following new course(s) have opened up:

- Class Code: 1536

- Class Code: 1551

- Class Code: 1570

Please check the portal.
```
## ▶️ How to Run

### Option 1: Run in Jupyter Notebook

Open **`main.ipynb`** and execute all cells in order.

### Option 2: Convert to Python Script

You can export and run the notebook as a normal Python file:
---

```bash
jupyter nbconvert --to script main.ipynb
python main.py
```
## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.


## Authors

- [@Saket Kumar Sinha](https://github.com/SaketSinha2005)



## License

[MIT](https://choosealicense.com/licenses/mit/)

