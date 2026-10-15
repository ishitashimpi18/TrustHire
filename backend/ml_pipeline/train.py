import os
import joblib
import numpy as np
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score

# Sample real-world grounded dataset: Genuine Job Postings vs. Scams (Indian & Global context)
GENUINE_SAMPLES = [
    "Software Engineer Intern at TCS. Looking for graduates in Computer Science or IT. Experience with Java, Spring Boot, SQL required. Full-time internship with monthly stipend of 25,000 INR. Medical insurance and certificate provided upon completion.",
    "Data Analyst Trainee - Infosys Mysore Campus. Candidate must have strong knowledge of Python, Pandas, Tableau, and SQL. Standard campus recruitment process with online test and technical interview. No fee required at any stage.",
    "Frontend Developer Intern. Required skills: React.js, Tailwind CSS, TypeScript. 6-month full-time internship with opportunity for PPO. Office in Bangalore, hybrid work. Stipend 30,000/month with mentor guidance.",
    "Associate Software Engineer at Wipro. Seeking 2025/2026 engineering graduates. Aptitude test followed by technical discussion. Official email communications will only be sent from wipro.com domain.",
    "Machine Learning Research Assistant. Knowledge of PyTorch, Scikit-learn, and data preprocessing. Research lab at IIT Bombay. Stipend provided per institute norms. Submit resume through university portal.",
    "Junior Quality Assurance Engineer. Requirements: Manual testing, Selenium, JIRA, Agile methodology. Permanent role with benefits including provident fund, health insurance, and paid time off.",
    "Product Design Intern at Swiggy. Work closely with product and engineering teams. Must have portfolio showcasing Figma/UI/UX case studies. 3 months duration with competitive market stipend.",
    "Backend Developer - Python/FastAPI. Requirements: 0-1 year experience, REST APIs, PostgreSQL, Docker. Apply via company careers page or LinkedIn Easy Apply. Equal opportunity employer.",
    "Cloud Operations Associate. AWS/Azure fundamentals, Linux scripting, Bash, Git. Full-time position with standard background verification and formal offer letter.",
    "Content Writer & Digital Marketing Intern. Good English grammar, SEO basics, social media strategy. Part-time or full-time. Performance-based incentives and certificate.",
    "DevOps Trainee. Knowledge of CI/CD pipelines, Docker, Kubernetes, GitOps. Location: Hyderabad. Formal employment contract with health coverage and gratuity.",
    "Business Development Executive. Candidate will identify potential clients, handle enterprise sales inquiries. Fixed CTC with uncapped quarterly commissions."
]

SCAM_SAMPLES = [
    "Urgent requirement: Earn 3000 to 5000 daily from home by liking YouTube videos and giving Google reviews. No experience needed. Contact HR on WhatsApp or Telegram immediately for task details.",
    "Guaranteed Internship in MNC with 100% placement! Pay refundable registration fee of 999 INR for document verification and interview slot booking. Offer letter issued within 24 hours.",
    "Data Entry Work from Home! Earn 40,000 per month typing simple capcha and MS Word files. Must pay 1500 security deposit for training kit and software license key. Deposit refunded with first salary.",
    "Amazon Part-Time Online Associate. Daily payout 2000-5000 INR directly into GPay or PhonePe. Only 30 minutes daily. Contact madam on WhatsApp at +91 9876543210 for immediate joining.",
    "Selected for Google Internship Program! Dear candidate, your resume has been shortlisted. Pay laptop security deposit of 2500 INR via UPI. Laptop and ID card will be dispatched to your home address.",
    "Simple copy paste job. Daily earning guaranteed. No skills, any student can apply. Join our Telegram group @instant_jobs_payout for task code and daily payment screenshots.",
    "Congratulations! You are selected as Project Manager without interview. Monthly salary 1,20,000 INR. Before issuing visa and appointment letter, kindly remit processing charges to HR account.",
    "Work from home typing job. Submit 50 pages daily. Registration charges 500 Rs mandatory. If accuracy is 90% you get 15000 weekly payment. Click link to pay fee now.",
    "Part time freelance hiring by International E-commerce portal. Complete online product rating tasks and earn instant cryptocurrency or UPI transfers. Message mentor on Telegram.",
    "Flipkart Warehouse Supervisor Vacancy. 10th/12th pass eligible. Free food and accommodation. Direct joining. Gate pass fee 750 INR to be transferred to recruiter before gate entry.",
    "Instagram page manager needed urgently. Earn 1500 per hour. Send Hi to our HR WhatsApp number to receive tasks and start earning today itself.",
    "Bank Back Office Executive. Direct selection through quota. Pay interview processing fee of 3000 INR to reserve seat. Limited vacancies, offer expires in 2 hours."
]

def train_and_export():
    output_dir = Path(__file__).resolve().parent
    output_dir.mkdir(parents=True, exist_ok=True)

    # Balance and duplicate for robust training sample distribution
    texts = []
    labels = []
    
    # 5x repeat with mild augmentation
    for _ in range(5):
        for g in GENUINE_SAMPLES:
            texts.append(g)
            labels.append(0)  # 0 = GENUINE
        for s in SCAM_SAMPLES:
            texts.append(s)
            labels.append(1)  # 1 = SCAM

    # Vectorize
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 2),
        max_features=3000,
        stop_words='english',
        min_df=2
    )
    X = vectorizer.fit_transform(texts)
    y = np.array(labels)

    # Train Random Forest (compatible with SHAP TreeExplainer)
    clf = RandomForestClassifier(
        n_estimators=150,
        max_depth=12,
        random_state=42,
        min_samples_split=3
    )
    clf.fit(X, y)

    # Save vectorizer and model
    joblib.dump(vectorizer, output_dir / "tfidf.pkl")
    joblib.dump(clf, output_dir / "best_model.pkl")

    # Save scam vectors pool for Near-Duplicate cosine similarity engine
    scam_vectors = vectorizer.transform(SCAM_SAMPLES)
    scam_metadata = [
        {"text": s, "title": s[:45] + "..."}
        for s in SCAM_SAMPLES
    ]
    joblib.dump({
        "vectors": scam_vectors,
        "metadata": scam_metadata
    }, output_dir / "scam_vector_pool.pkl")

    print("Model, TF-IDF vectorizer, and scam vector pool trained and saved successfully!")

if __name__ == "__main__":
    train_and_export()
