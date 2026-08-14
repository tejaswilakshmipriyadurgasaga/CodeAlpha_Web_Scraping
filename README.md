# CodeAlpha_Web_Scraping
Web scraping project using Python, Requests, BeautifulSoup, and Pandas to collect book data and create a structured CSV dataset with prices converted to INR.
# CodeAlpha Web Scraping Project

## 📌 Internship

**CodeAlpha Data Analytics Internship**

## 📊 Task 1: Web Scraping

### 📖 Project Overview

This project was completed as part of the **CodeAlpha Data Analytics Internship – Task 1**.

The objective of this task is to collect book-related information from a website using **Python web scraping techniques** and store the collected data in a structured CSV dataset.

For this project, the **Books to Scrape** website was used as the data source.

## 🎯 Objectives

* Access web pages using Python
* Understand basic HTML structure
* Extract useful information from web pages
* Scrape data from multiple pages
* Convert the scraped data into a structured dataset
* Convert book prices from GBP to Indian Rupees (INR)
* Save the final data as a CSV file

## 🛠️ Technologies Used

* **Python**
* **Requests** – To send HTTP requests and retrieve webpage content
* **BeautifulSoup** – To parse HTML and extract information
* **Pandas** – To organize and save the scraped data

## 📋 Data Collected

The following information was collected for each book:

* **Book Title**
* **Price (INR)**
* **Rating**
* **Availability**

## 💰 Price Conversion

The original book prices on the website are displayed in British Pounds (GBP).

For this project, a fixed conversion rate of:

**1 GBP = ₹115**

was used to convert the prices into Indian Rupees.

## 🔄 Web Scraping Process

The project follows this workflow:

```text
Books to Scrape Website
        ↓
Requests
        ↓
HTML Content
        ↓
BeautifulSoup
        ↓
Extract Book Information
        ↓
Pandas DataFrame
        ↓
CSV Dataset
```

## 📄 Output

The scraped data is saved as:

```text
books_dataset.csv
```

The dataset contains approximately **100 book records collected from 5 pages** of the website.

## 📁 Project Structure

```text
codealpha_web_scraping/
│
├── task1.py
├── books_dataset.csv
└── README.md
```

## ▶️ How to Run

### 1. Install Python libraries

```bash
pip install requests beautifulsoup4 pandas
```

### 2. Run the Python program

```bash
python task1.py
```

### 3. Output

After successful execution, the program creates:

```text
books_dataset.csv
```

## 📚 Learning Outcome

Through this project, I learned the fundamentals of:

* Web scraping
* HTML parsing
* Data extraction
* Python Requests
* BeautifulSoup
* Pandas
* CSV dataset creation
* Handling data from multiple web pages

## 👩‍💻 Internship

**CodeAlpha Data Analytics Internship**
**Task 1 – Web Scraping**

---

**Author:** Saga Tejaswi Lakshmi Priya Durga
