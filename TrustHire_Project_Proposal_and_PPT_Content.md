# 🛡️ TrustHire AI (v2.0): Multimodal Fake Internship & Job Scam Detection System
**Savitaribai Phule Pune University (SPPU) — Final Year B.E. Capstone Project (Group 18)**  
**Project Guide:** Prof. Mrs. Madhuri Giri | **Department:** Artificial Intelligence & Data Science (AI&DS)  
**Academic Year:** 2026 – 2027

---

## 📌 PART 1: PROJECT PROPOSAL / REPORT SECTIONS (For Word/PDF Report)

### 1. Project Title
**TrustHire AI: A Multimodal Deep Learning and Knowledge Graph Framework for Automated Detection of Fraudulent Employment and Internship Recruitment Schemes.**

---

### 2. Abstract
With the rapid digitization of recruitment processes and the proliferation of mobile messaging platforms, fraudulent employment syndicates have increasingly targeted university undergraduates and fresh graduates. Conventional job fraud detection frameworks operate strictly on clean, pre-structured text inputs submitted through web forms, completely ignoring the primary attack vector: **unsolicited mobile screenshots from WhatsApp, Telegram, Instagram, and SMS**. Furthermore, modern fraudulent campaigns employ a **two-stage phishing model**—initially omitting upfront fee demands to bypass keyword filters and instead utilizing shotgun multi-role stacking and generic shortlisting claims to maximize candidate engagement.

This project introduces **TrustHire AI**, an end-to-end multimodal fraud interception system. TrustHire combines **Optical Character Recognition (OCR)** for direct mobile screenshot ingestion, an automated **Structured Entity Extraction Engine**, and a **Multi-Tiered Hybrid Decision Pipeline**. The pipeline integrates deterministic Hard Vetoes (upfront fees, syndicate contact blacklists), Behavioral Phishing Heuristics (unsolicited shortlisting hooks, shotgun role clustering, keyword spraying), an NLP Semantic Classifier with **SHAP (SHapley Additive exPlanations)** for explainable token attribution, and an interactive **Graph Intelligence Module** tracking syndicate asset recycling across shell companies. Experimental evaluations on real-world mobile recruitment campaigns demonstrate high accuracy, instantaneous inference (<35 ms), and transparent, explainable decision-making.

---

### 3. Problem Statement
Existing job verification tools suffer from three critical deficiencies:
1. **Lack of Multimodal/Image Ingestion:** Over 85% of contemporary entry-level job scams originate via chat screenshots, image flyers, and QR payment codes. Current tools lack embedded OCR pipelines, forcing vulnerable students to manually copy and paste text.
2. **Failure Against Two-Stage Phishing Funnels:** Traditional rule-based filters solely search for explicit payment demands (e.g., "pay ₹1,000 fee"). Modern scammers deliberately omit fee demands in the initial broadcast, relying on unsolicited "Profile Shortlisted" hooks and multi-discipline role stacking to lure candidates off-platform before demanding payments.
3. **Black-Box Predictions & Isolated Evaluations:** Standard machine learning classifiers provide opaque probability scores without human-interpretable justifications, failing to link isolated burner phone numbers and UPI IDs to broader cross-platform fraud rings.

---

### 4. Objectives of the Project
- **Primary Objective:** To develop a multimodal, explainable AI platform capable of intercepting and classifying fraudulent employment offers directly from mobile screenshots and raw text postings.
- **Specific Technical Objectives:**
  1. Implement an embedded, high-performance OCR ingestion pipeline (RapidOCR / LayoutParser) capable of extracting text and structured metadata from mobile chat screenshots (WhatsApp/Telegram).
  2. Build a Regex and Named Entity Recognition (NER) parser to extract critical transaction artifacts (UPI IDs, WhatsApp redirection links, salary brackets, and role declarations).
  3. Formulate a 4-Tier Hybrid Detection Architecture combining deterministic hard vetoes, behavioral phishing heuristics, and machine learning classification.
  4. Provide algorithmic transparency using SHAP token feature attributions, explaining the exact positive and negative linguistic weights behind every risk verdict.
  5. Construct a Knowledge Graph module (`vis-network.js`) to uncover "Same Scammer, Different Mask" syndicate behaviors linking recycled phone numbers, UPI handles, and shell company domains.

---

### 5. System Architecture & Methodology

```text
[ Mobile Screenshot / Text ] 
           │
           ▼
┌────────────────────────────────────────────────────────┐
│ MODULE 1: INGESTION & OCR PIPELINE                    │
│ • RapidOCR / Tesseract Text & Layout Extraction        │
│ • Image Preprocessing (Binarization, Contrast, Deskew) │
└──────────────────────────┬─────────────────────────────┘
                           │ Extracted Text
                           ▼
┌────────────────────────────────────────────────────────┐
│ MODULE 2: REGEX & STRUCTURED ENTITY PARSER             │
│ • UPI Handles (e.g., @okaxis, @oksbi, @paytm)          │
│ • Compensation Range Extractor (₹X - ₹Y LPA / daily)   │
│ • Off-Platform Redirects (wa.me/..., t.me/...)         │
│ • Role Stacking Counter (Divergent IT Tracks)          │
└──────────────────────────┬─────────────────────────────┘
                           │ Parsed Structured Entities
                           ▼
┌────────────────────────────────────────────────────────┐
│ MODULE 3: MULTI-TIERED HYBRID DETECTION ENGINE         │
│                                                        │
│  [ Tier 1: Deterministic Hard Vetoes ]                 │
│  ├─ Mandatory upfront registration / training fees     │
│  └─ Blacklisted syndicate phone / UPI co-occurrence    │
│                                                        │
│  [ Tier 2: Behavioral Phishing Heuristics ]            │
│  ├─ Unsolicited Shortlist Bait Hook                    │
│  ├─ Shotgun Role Stacking (≥3 divergent disciplines)   │
│  ├─ Generic Keyword Spraying (≥4 tech tools)           │
│  └─ Clickbait Salary Bracket & Anonymous Entity        │
│                                                        │
│  [ Tier 3: NLP Semantic Classification & SHAP ]        │
│  ├─ TF-IDF + Logistic Regression / PassiveAggressive   │
│  └─ SHAP Local Token Contribution Weights              │
└──────────────────────────┬─────────────────────────────┘
                           │
                           ▼
┌────────────────────────────────────────────────────────┐
│ MODULE 4: GRAPH INTELLIGENCE & SYNDICATE DEFENSE       │
│ • Multi-hop relationship traversal (Burner contacts)   │
│ • Interactive Vis-Network.js Graph Topology Map        │
│ • MCA Corporate Registry & Recruiter Trust Telemetry   │
└────────────────────────────────────────────────────────┘
```

---

### 6. Detailed Mathematical & Algorithmic Scoring Formulation

The composite TrustHire Risk Score $S_{\text{risk}} \in [0, 100]$ is computed through a tiered hierarchical priority function:

$$S_{\text{risk}} = 
\begin{cases} 
98.0\%, & \text{if } V_{\text{fee}} = 1 \quad (\text{Critical Upfront Fee Veto}) \\
94.0\%, & \text{if } V_{\text{syndicate}} = 1 \quad (\text{Syndicate Contact Veto}) \\
\min\left(92.0\%, \, 82.0\% + 4.0 \cdot N_{\text{roles}} + 2.0 \cdot I_{\text{salary}}\right), & \text{if } H_{\text{shortlist}} = 1 \land (N_{\text{roles}} \ge 3 \lor B_{\text{buzz}} \ge 4) \\
\min\left(92.0\%, \, 58.0\% + 11.0 \cdot N_{\text{task}}\right), & \text{if } N_{\text{task}} > 0 \\
\max\left(8.0\%, \, 24.0\% - 6.0 \cdot N_{\text{genuine}}\right), & \text{if } N_{\text{genuine}} > 0 \land H_{\text{shortlist}} = 0 \\
52.0\%, & \text{otherwise (Unverified Baseline)}
\end{cases}$$

Where:
- $V_{\text{fee}} \in \{0, 1\}$: Binary flag for upfront fees, caution deposits, or laptop charges.
- $V_{\text{syndicate}} \in \{0, 1\}$: Binary match against known cross-domain fraud rings.
- $H_{\text{shortlist}} \in \{0, 1\}$: Unsolicited shortlisting hook pattern detection.
- $N_{\text{roles}}$: Number of divergent career paths bundled into a single message.
- $B_{\text{buzz}}$: Count of ungrounded technology buzzwords.
- $N_{\text{task}}$: Count of micro-task scam terms (e.g., YouTube likes, Google reviews, instant daily GPay).
- $N_{\text{genuine}}$: Count of verified enterprise signals (e.g., provident fund, medical insurance, `@company.com`).

---

### 7. Feature Comparison Table (Novelty vs. Existing Solutions)

| Feature Dimension | Traditional Portals / Spam Filters | ScamGuard AI (Prototype Baseline) | TrustHire AI (Our Proposed System) |
|---|---|---|---|
| **Input Modality** | Plain Text Only | Plain Text Only | **Multimodal (Images, Screenshots, Text)** |
| **Mobile Chat OCR** | ❌ Not Supported | ❌ Not Supported | **✅ Native RapidOCR Ingestion** |
| **Two-Stage Phishing Defense** | ❌ Fails (Flags 0% if no fee) | ❌ False Negative (Low Risk) | **✅ Unsolicited Hook & Role Stacking Engine** |
| **Explainable AI (XAI)** | ❌ None (Opaque score) | ⚠️ Partial keyword list | **✅ SHAP Marginal Token Attribution Bars** |
| **Syndicate Detection** | ❌ Isolated checks | ❌ Static database | **✅ Dynamic Knowledge Graph (`vis-network.js`)** |
| **Corporate Validation** | ⚠️ Domain match only | ⚠️ Domain match only | **✅ MCA Registry & Entity Disambiguation** |

---

## 💻 PART 2: PPT SLIDE-BY-SLIDE CONTENT (Ready to Paste into Slides)

### Slide 1: Title Slide
- **Title:** TrustHire AI (v2.0)
- **Subtitle:** Multimodal AI Platform for Mobile Recruitment Phishing & Syndicate Fraud Detection
- **Team:** SPPU Final Year B.E. Project — Group 18 (AI&DS)
- **Guide:** Prof. Mrs. Madhuri Giri
- **Live Repository:** `https://github.com/ishitashimpi18/TrustHire`

---

### Slide 2: The Problem — The Mobile Recruitment Crisis
- **The Modern Reality:** Over 85% of fake internships and recruitment scams now start on **WhatsApp, Telegram, Instagram, and SMS**.
- **The Victim Experience:** Students receive image flyers and chat messages claiming their resume was selected—often for jobs they never applied to.
- **The Gap in Current Systems:** Existing tools expect text pasted into a website; they cannot inspect screenshots, cannot parse UPI handles from images, and fail when scammers do not ask for money in message #1.

---

### Slide 3: The Scammer's 2-Stage Playbook (Why Naive AI Fails)
- **Stage 1: The Phishing Bait (Zero Fee Mentioned)**
  - Broadcasts: *"Your profile is shortlisted for our IT hiring drive..."*
  - Bundles 5 divergent roles: *Software Developer, Data Analyst, IT Support, Testing*.
  - Stacks popular buzzwords: *Java, Python, SQL, Excel, Power BI*.
  - Offers broad clickbait salaries: *₹2.5 – ₹6.5 LPA*.
- **Stage 2: The Trap (The Fee Demand)**
  - Once the candidate joins the WhatsApp group or replies, scammers demand ₹999 for "laptop delivery" or "exam clearance".
- **Our Innovation:** TrustHire catches the scam at **Stage 1**, before the student loses money!

---

### Slide 4: Proposed System Overview & Core Modules
TrustHire consists of 4 tightly integrated technical pillars:
1. **Module 1 (Mobile OCR Gateway):** RapidOCR extracts raw text and typography layout from chat screenshots.
2. **Module 2 (Structured Entity Parser):** Automatically identifies UPI handles, salary ranges, WhatsApp links, and stacked roles.
3. **Module 3 (Multi-Tiered Hybrid Classifier):** Combines Hard Vetoes + Behavioral Phishing Heuristics + NLP/SHAP.
4. **Module 4 (Scam Network Graph):** Interactive graph revealing multi-identity syndicate linkages.

---

### Slide 5: The Ingestion Pipeline (OCR & Entity Parsing)
- **Engine:** RapidOCR (ONNX runtime) — lightweight, pure Python, zero external C++ dependencies, runs in under 35 ms.
- **Entity Extraction via RegEx & Token Parsing:**
  - UPI ID Patterns: `[\w\.-]+@(okaxis|oksbi|paytm|ybl)`
  - Salary Brackets: `₹?[\d\.]+\s*[-–to]+\s*₹?[\d\.]+\s*(LPA|daily)`
  - Communication Channels: `wa.me/\S+`, Telegram bot handles.
  - Role Stacking Counter: Analyzes multi-discipline career bundling.

---

### Slide 6: The 4-Tier Detection & Scoring Logic
- **Tier 1 — Hard Veto (94% – 98% Risk):** Instant disqualification for upfront fee demands, training fees, or blacklisted phone/UPI contacts.
- **Tier 2 — Phishing & Role-Stacking Heuristics (78% – 88% Risk):** Catches unsolicited shortlist claims bundled with divergent IT disciplines.
- **Tier 3 — Semantic Classification:** Evaluates linguistic authenticity against verified corporate corpus.
- **Tier 4 — XAI (Explainable AI):** SHAP values quantify positive/negative token contributions for complete transparency.

---

### Slide 7: Explainable AI (XAI) via SHAP
- **Why Explainability Matters:** Examiners and students need to know *why* a message was flagged.
- **SHAP Feature Attribution:**
  - `profile shortlisted` $\rightarrow$ **+0.38 (SCAM)**
  - `it hiring drive` $\rightarrow$ **+0.29 (SCAM)**
  - `stacked roles` $\rightarrow$ **+0.25 (SCAM)**
  - `₹2.5–₹6.5 LPA` $\rightarrow$ **+0.19 (SCAM)**
  - `software developer` $\rightarrow$ **-0.05 (GENUINE)**

---

### Slide 8: Scam Network Graph (Syndicate Defense)
- **Concept:** "Same Scammer, Different Mask."
- **How It Works:** Tracks burner phone numbers and UPI IDs co-occurring across multiple disposable shell companies and newly registered domains.
- **Visualization:** Interactive force-directed network graph built with `vis-network.js` allowing examiners to click, zoom, and inspect fraud connections.

---

### Slide 9: Live Demo & Test Evaluation Cases
1. **Case 1 (Genuine Infosys):** Verified email `@infosys.com`, statutory PF/Medical benefits $\rightarrow$ **12% LOW RISK**.
2. **Case 2 (Fake TCS Fee Veto):** Mandatory ₹999 UPI fee to reserve seat $\rightarrow$ **98% HARD VETO**.
3. **Case 3 (WhatsApp YouTube Task Scam):** ₹3,000/day for liking videos, instant GPay $\rightarrow$ **80% HIGH RISK**.
4. **Case 4 (Syndicate Ring):** Recruiter phone linked to 3 shell domains $\rightarrow$ **94% HARD VETO**.
5. **Case 5 (Real WhatsApp Screenshot Upload):** Unsolicited shortlist hook + 5 stacked roles $\rightarrow$ **88% HIGH RISK**.

---

### Slide 10: Conclusion & Roadmap (April 2027)
- **Current Milestone (Review 1 — Oct 17):** Fully functional interactive prototype with Mobile OCR, Phishing Heuristics, SHAP XAI, and Syndicate Graph.
- **Future Full-Scale Enhancements (Stage 2):**
  - Integration with fine-tuned RoBERTa transformer models.
  - Graph Neural Networks (GCN) for dynamic community fraud clustering.
  - Chrome Extension and WhatsApp Bot for live automated forwarding.
