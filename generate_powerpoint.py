import sys
import os

# Auto-install python-pptx if missing
try:
    import pptx
except ImportError:
    print("Installing python-pptx...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "python-pptx"])
    import pptx

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

OUTPUT_FILE = r"C:\TrustHire\TrustHire_Review_III_Presentation.pptx"

# Modern Palette (Sky Blue, Navy, White, Alert Red, Emerald Green)
COLOR_NAVY = RGBColor(15, 23, 42)        # #0F172A
COLOR_SKY = RGBColor(2, 132, 199)        # #0284C7
COLOR_LIGHT_SKY = RGBColor(240, 249, 255)# #F0F9FF
COLOR_WHITE = RGBColor(255, 255, 255)    # #FFFFFF
COLOR_SLATE_BG = RGBColor(248, 250, 252) # #F8FAFC
COLOR_BORDER = RGBColor(226, 232, 240)   # #E2E8F0
COLOR_TEXT_DARK = RGBColor(15, 23, 42)   # #0F172A
COLOR_TEXT_MUTED = RGBColor(71, 85, 105) # #475569
COLOR_RED = RGBColor(220, 38, 38)        # #DC2626
COLOR_GREEN = RGBColor(22, 163, 74)      # #16A34A
COLOR_AMBER = RGBColor(217, 119, 6)      # #D97706

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
blank_layout = prs.slide_layouts[6]

def add_header(slide, title_text, category_text="REVIEW-III: CAPSTONE DELIVERABLES"):
    # Category tag
    tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.5), Inches(0.35))
    tf_tag = tag_box.text_frame
    tf_tag.word_wrap = True
    p_tag = tf_tag.paragraphs[0]
    p_tag.text = f"🛡️ TRUSTHIRE AI • {category_text.upper()}"
    p_tag.font.size = Pt(11)
    p_tag.font.bold = True
    p_tag.font.color.rgb = COLOR_SKY
    
    # Title
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.72), Inches(11.5), Inches(0.7))
    tf_title = title_box.text_frame
    tf_title.word_wrap = True
    p_title = tf_title.paragraphs[0]
    p_title.text = title_text
    p_title.font.size = Pt(24)
    p_title.font.bold = True
    p_title.font.color.rgb = COLOR_NAVY

def add_card(slide, left, top, width, height, bg_color=COLOR_SLATE_BG, border_color=COLOR_BORDER):
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = Pt(1.5)
    else:
        shape.line.fill.background()
    return shape

# ==============================================================================
# SLIDE 1: TITLE SLIDE (Dark Navy Hero)
# ==============================================================================
slide1 = prs.slides.add_slide(blank_layout)
bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
bg1.fill.solid()
bg1.fill.fore_color.rgb = COLOR_NAVY
bg1.line.fill.background()

# Badge
badge1 = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(0.9), Inches(5.8), Inches(0.45))
badge1.fill.solid()
badge1.fill.fore_color.rgb = RGBColor(30, 41, 59)
badge1.line.color.rgb = COLOR_SKY
badge1.text_frame.paragraphs[0].text = "🎓 SPPU FINAL YEAR B.E. CAPSTONE • GROUP 18"
badge1.text_frame.paragraphs[0].font.size = Pt(11)
badge1.text_frame.paragraphs[0].font.bold = True
badge1.text_frame.paragraphs[0].font.color.rgb = COLOR_SKY
badge1.text_frame.paragraphs[0].alignment = PP_ALIGN.CENTER

# Main Title
tb1 = slide1.shapes.add_textbox(Inches(1.0), Inches(1.55), Inches(11.3), Inches(2.2))
tf1 = tb1.text_frame
tf1.word_wrap = True
p1_1 = tf1.paragraphs[0]
p1_1.text = "TrustHire AI (v2.0)"
p1_1.font.size = Pt(44)
p1_1.font.bold = True
p1_1.font.color.rgb = COLOR_WHITE

p1_2 = tf1.add_paragraph()
p1_2.text = "Multimodal Deep Learning & Knowledge Graph Framework for Automated Recruitment Scam Detection"
p1_2.font.size = Pt(20)
p1_2.font.color.rgb = RGBColor(148, 163, 184)

# 3 Highlights Cards on Title
card_w = Inches(3.55)
card_h = Inches(2.4)
card_y = Inches(4.2)

# Card 1
c1 = add_card(slide1, Inches(1.0), card_y, card_w, card_h, bg_color=RGBColor(30, 41, 59), border_color=COLOR_SKY)
tf_c1 = c1.text_frame
tf_c1.word_wrap = True
tf_c1.margin_left = tf_c1.margin_right = tf_c1.margin_top = Inches(0.25)
p = tf_c1.paragraphs[0]
p.text = "📱 Multimodal Ingestion"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = COLOR_WHITE
p2 = tf_c1.add_paragraph()
p2.text = "\nDirect WhatsApp/Telegram chat screenshot processing via sub-35ms RapidOCR without requiring manual text transcription."
p2.font.size = Pt(11.5)
p2.font.color.rgb = RGBColor(203, 213, 225)

# Card 2
c2 = add_card(slide1, Inches(4.88), card_y, card_w, card_h, bg_color=RGBColor(30, 41, 59), border_color=COLOR_SKY)
tf_c2 = c2.text_frame
tf_c2.word_wrap = True
tf_c2.margin_left = tf_c2.margin_right = tf_c2.margin_top = Inches(0.25)
p = tf_c2.paragraphs[0]
p.text = "🎣 2-Stage Phishing Defense"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = COLOR_WHITE
p2 = tf_c2.add_paragraph()
p2.text = "\nCatches scams before money is demanded by intercepting unsolicited shortlisting hooks and shotgun multi-role stacking."
p2.font.size = Pt(11.5)
p2.font.color.rgb = RGBColor(203, 213, 225)

# Card 3
c3 = add_card(slide1, Inches(8.76), card_y, card_w, card_h, bg_color=RGBColor(30, 41, 59), border_color=COLOR_SKY)
tf_c3 = c3.text_frame
tf_c3.word_wrap = True
tf_c3.margin_left = tf_c3.margin_right = tf_c3.margin_top = Inches(0.25)
p = tf_c3.paragraphs[0]
p.text = "🕸️ Syndicate Knowledge Graph"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = COLOR_WHITE
p2 = tf_c3.add_paragraph()
p2.text = "\nExposes 'Same Scammer, Different Mask' rings by linking recycled burner phones and UPI handles across discarded shell domains."
p2.font.size = Pt(11.5)
p2.font.color.rgb = RGBColor(203, 213, 225)

# Footer credits
tb_foot = slide1.shapes.add_textbox(Inches(1.0), Inches(6.8), Inches(11.3), Inches(0.5))
p_foot = tb_foot.text_frame.paragraphs[0]
p_foot.text = "Project Guide: Prof. Mrs. Madhuri Giri  •  Savitribai Phule Pune University (SPPU)  •  GitHub: github.com/ishitashimpi18/TrustHire"
p_foot.font.size = Pt(10.5)
p_foot.font.color.rgb = RGBColor(148, 163, 184)

# ==============================================================================
# SLIDE 2: PROBLEM STATEMENT & MOTIVATION
# ==============================================================================
slide2 = prs.slides.add_slide(blank_layout)
add_header(slide2, "Problem Statement & Real-World Motivation")

# Big Problem Quote Card
q_card = add_card(slide2, Inches(0.8), Inches(1.5), Inches(11.733), Inches(1.3), bg_color=COLOR_LIGHT_SKY, border_color=COLOR_SKY)
tf_q = q_card.text_frame
tf_q.word_wrap = True
tf_q.margin_left = tf_q.margin_right = tf_q.margin_top = Inches(0.2)
pq = tf_q.paragraphs[0]
pq.text = "“To design and build an explainable, multimodal AI defense platform capable of detecting fraudulent job and internship offers directly from mobile chat screenshots and raw postings, mitigating two-stage recruitment phishing funnels through tiered hard vetoes and syndicate knowledge graphs.”"
pq.font.size = Pt(13)
pq.font.italic = True
pq.font.bold = True
pq.font.color.rgb = COLOR_NAVY

# 3 Column Context Cards
c_y2 = Inches(3.1)
c_h2 = Inches(3.8)

# Col 1
c1 = add_card(slide2, Inches(0.8), c_y2, Inches(3.7), c_h2)
tf = c1.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.25)
tf.paragraphs[0].text = "🚨 The Modern Attack Vector"
tf.paragraphs[0].font.size = Pt(15)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = COLOR_RED
p = tf.add_paragraph()
p.text = "\n• Over 85% of fresher recruitment fraud in India originates on WhatsApp, Telegram, and Instagram.\n\n• Attackers distribute image flyers and chat templates rather than web postings.\n\n• Over ₹1,200 Crores lost annually in India to fraudulent job & task schemes."
p.font.size = Pt(11)
p.font.color.rgb = COLOR_TEXT_DARK

# Col 2
c2 = add_card(slide2, Inches(4.8), c_y2, Inches(3.7), c_h2)
tf = c2.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.25)
tf.paragraphs[0].text = "⚠️ The 2-Stage Trap"
tf.paragraphs[0].font.size = Pt(15)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = COLOR_AMBER
p = tf.add_paragraph()
p.text = "\n• Stage 1 (The Bait): Scammers claim 'Your profile is shortlisted!' for 5 distinct roles at ₹2.5–₹6.5 LPA. Zero fee is asked initially.\n\n• Stage 2 (The Trap): Once the candidate replies, scammers demand ₹999 for training kits or laptop dispatch.\n\n• Traditional AI flags Stage 1 as 0% risk!"
p.font.size = Pt(11)
p.font.color.rgb = COLOR_TEXT_DARK

# Col 3
c3 = add_card(slide2, Inches(8.8), c_y2, Inches(3.7), c_h2)
tf = c3.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.25)
tf.paragraphs[0].text = "🛡️ TrustHire's Intervention"
tf.paragraphs[0].font.size = Pt(15)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = COLOR_GREEN
p = tf.add_paragraph()
p.text = "\n• Embedded OCR: Students simply upload screenshots; text and entities are parsed in <35ms.\n\n• Phishing Heuristics: Identifies unsolicited shortlisting and role stacking at Stage 1 (flags 88% High Risk).\n\n• Complete Transparency: Explains exact decision factors with SHAP token attribution."
p.font.size = Pt(11)
p.font.color.rgb = COLOR_TEXT_DARK

# ==============================================================================
# SLIDE 3: ABSTRACT
# ==============================================================================
slide3 = prs.slides.add_slide(blank_layout)
add_header(slide3, "Project Abstract")

# Left Column (The Problem & Gap)
c_left = add_card(slide3, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.4))
tf = c_left.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.3)
tf.paragraphs[0].text = "Executive Summary & Research Gap"
tf.paragraphs[0].font.size = Pt(16)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = COLOR_NAVY
p = tf.add_paragraph()
p.text = (
    "\nWith the widespread digitization of off-campus hiring, fraudulent syndicates aggressively target fresh university graduates. "
    "Existing research benchmarks (e.g. EMSCAD dataset) assume clean, structured text forms and rely purely on explicit fee detection.\n\n"
    "This creates two severe vulnerabilities:\n"
    "1. Blindness to Mobile Screenshots: Inability to parse images, flyers, and UPI handles distributed over WhatsApp.\n"
    "2. False Negatives on Phishing Funnels: Traditional classifiers evaluate unsolicited shortlisting campaigns as 'Safe' because no fee is requested in the initial message.\n\n"
    "TrustHire AI bridges this fundamental gap by introducing a multi-tiered multimodal architecture."
)
p.font.size = Pt(11.5)
p.font.color.rgb = COLOR_TEXT_DARK

# Right Column (4 Solution Pillars)
c_right = add_card(slide3, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.4), bg_color=COLOR_LIGHT_SKY, border_color=COLOR_SKY)
tf = c_right.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.3)
tf.paragraphs[0].text = "Core Innovations of TrustHire v2.0"
tf.paragraphs[0].font.size = Pt(16)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = COLOR_NAVY

pillars = [
    ("1. RapidOCR Multimodal Ingestion", "Sub-35ms ONNX engine extracting text, bounding boxes, and transaction entities directly from images."),
    ("2. 4-Tier Hybrid Detection Engine", "Combines deterministic Hard Vetoes (upfront fees), Behavioral Phishing Heuristics (role stacking), and NLP classification."),
    ("3. Explainable AI (SHAP)", "Mathematical transparency attributing positive/negative risk weights to individual words for human trust."),
    ("4. Syndicate Knowledge Graph", "Interactive force-directed graph exposing multi-identity rings sharing burner contacts across shell domains.")
]

for title, desc in pillars:
    p_t = tf.add_paragraph()
    p_t.text = f"\n• {title}"
    p_t.font.size = Pt(12)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_SKY
    p_d = tf.add_paragraph()
    p_d.text = f"  {desc}"
    p_d.font.size = Pt(10.5)
    p_d.font.color.rgb = COLOR_TEXT_DARK

# ==============================================================================
# SLIDE 4: LITERATURE SURVEY & GAP ANALYSIS
# ==============================================================================
slide4 = prs.slides.add_slide(blank_layout)
add_header(slide4, "Literature Survey: Comparative Benchmark")

# Table Card
tbl_card = add_card(slide4, Inches(0.8), Inches(1.5), Inches(11.733), Inches(4.4))
tf_tbl = tbl_card.text_frame
tf_tbl.margin_left = tf_tbl.margin_right = tf_tbl.margin_top = Inches(0.2)
tf_tbl.word_wrap = True

p = tf_tbl.paragraphs[0]
p.text = "Feature Matrix: Traditional Systems vs. ScamGuard vs. TrustHire AI"
p.font.size = Pt(15)
p.font.bold = True
p.font.color.rgb = COLOR_NAVY

# 5 Comparative rows
rows = [
    ("Input Modality", "Form Text Only", "Plain Text Only", "Multimodal (Screenshots + Text)"),
    ("Mobile Chat OCR", "❌ None", "❌ None", "✅ Native RapidOCR (<35ms ONNX)"),
    ("2-Stage Phishing Defense", "❌ Fails (0% if no fee)", "❌ False Negative (32% Low)", "✅ Unsolicited Hook & Role Stacking (88%)"),
    ("Explainable AI (XAI)", "❌ Opaque Black-Box", "⚠️ Static Keywords", "✅ SHAP Token Contribution Weights"),
    ("Syndicate Graph Defense", "❌ Isolated Accounts", "❌ Static Database", "✅ Dynamic Knowledge Graph (vis-network)"),
    ("Indian MCA Validation", "⚠️ Domain match only", "⚠️ Domain match only", "✅ MCA Registry & Entity Disambiguation")
]

p_t = tf_tbl.add_paragraph()
p_t.text = f"\n{'PARAMETER / CAPABILITY':<30} | {'EXISTING PORTALS / PAPERS':<30} | {'SCAMGUARD (BASELINE)':<26} | {'TRUSTHIRE AI (PROPOSED)'}"
p_t.font.size = Pt(10)
p_t.font.bold = True
p_t.font.color.rgb = COLOR_SKY

for param, ext, base, prop in rows:
    p_r = tf_tbl.add_paragraph()
    p_r.text = f"• {param:<28} | {ext:<30} | {base:<26} | {prop}"
    p_r.font.size = Pt(10)
    p_r.font.color.rgb = COLOR_TEXT_DARK

# Key Takeaway Box
b_card = add_card(slide4, Inches(0.8), Inches(6.05), Inches(11.733), Inches(0.95), bg_color=COLOR_LIGHT_SKY, border_color=COLOR_SKY)
tf_b = b_card.text_frame
tf_b.word_wrap = True
tf_b.margin_left = tf_b.margin_right = tf_b.margin_top = Inches(0.18)
pb = tf_b.paragraphs[0]
pb.text = "💡 Research Takeaway: Prior literature heavily overfits to explicit payment tokens in clean text. TrustHire is the first student-focused system to address multimodal OCR ingestion and early Stage-1 recruitment phishing funnels."
pb.font.size = Pt(11)
pb.font.bold = True
pb.font.color.rgb = COLOR_NAVY

# ==============================================================================
# SLIDE 5: METHODOLOGY
# ==============================================================================
slide5 = prs.slides.add_slide(blank_layout)
add_header(slide5, "End-to-End System Methodology")

# 4 Horizontal Pipeline Cards
step_w = Inches(2.7)
step_h = Inches(4.5)
step_y = Inches(1.5)

steps = [
    ("Step 1: Ingestion Gateway", "📱 Multimodal Input", 
     "• User uploads chat screenshot or pastes raw offer text.\n• RapidOCR applies binarization and layout extraction.\n• Generates clean, editable text transcript in <35 ms."),
    ("Step 2: Entity Parsing", "⚙️ Regex & NER Engine", 
     "• Scans for UPI payment handles (@okaxis, @paytm).\n• Extracts compensation brackets (₹2.5–₹6.5 LPA / daily).\n• Discovers WhatsApp redirect links (wa.me/).\n• Counts stacked divergent IT roles."),
    ("Step 3: Tiered Scoring", "🧠 4-Tier Hybrid Pipeline", 
     "• Tier 1: Deterministic Hard Vetoes (Fees/Blacklist).\n• Tier 2: Behavioral Phishing Heuristics (Bait hook).\n• Tier 3: NLP TF-IDF Semantic Classification.\n• Tier 4: SHAP Explainability Engine."),
    ("Step 4: Output & Telemetry", "🎯 Multi-Action Output", 
     "• Interactive Plotly Radial Risk Gauge.\n• Bulleted Triggered Factor Explanations.\n• SHAP Token Attribution Chart.\n• Cross-Domain Syndicate Graph Linkages.")
]

for i, (title, icon, content) in enumerate(steps):
    card = add_card(slide5, Inches(0.8 + i*3.0), step_y, step_w, step_h)
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.2)
    
    p0 = tf.paragraphs[0]
    p0.text = icon
    p0.font.size = Pt(16)
    
    p1 = tf.add_paragraph()
    p1.text = title
    p1.font.size = Pt(13)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_SKY
    
    p2 = tf.add_paragraph()
    p2.text = f"\n{content}"
    p2.font.size = Pt(10.5)
    p2.font.color.rgb = COLOR_TEXT_DARK

# Bottom note
note = slide5.shapes.add_textbox(Inches(0.8), Inches(6.25), Inches(11.733), Inches(0.5))
p = note.text_frame.paragraphs[0]
p.text = "📌 Reference to Project Deliverables: Maps directly to Fig 1. Architecture and Fig 2.2 Level 1 DFD in Design Report."
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = COLOR_TEXT_MUTED

# ==============================================================================
# SLIDE 6: DESIGN, ALGORITHMS & TECHNIQUES USED
# ==============================================================================
slide6 = prs.slides.add_slide(blank_layout)
add_header(slide6, "System Design, Algorithms & Techniques")

# Left Column: Mathematical Formula
c_formula = add_card(slide6, Inches(0.8), Inches(1.5), Inches(6.0), Inches(5.3))
tf = c_formula.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.25)

tf.paragraphs[0].text = "Hierarchical Tiered Scoring Formula"
tf.paragraphs[0].font.size = Pt(15)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = COLOR_NAVY

formula_text = (
    "\nS_risk = \n"
    "• 98.0%,  if V_fee = 1 (Mandatory Upfront Fee Veto)\n"
    "• 94.0%,  if V_syndicate = 1 (Syndicate Contact Veto)\n"
    "• min(92%, 82% + 4·N_roles + 2·I_salary), if H_shortlist = 1 ∧ (N_roles ≥ 3 ∨ B_buzz ≥ 4)\n"
    "• min(92%, 58% + 11·N_task), if N_task > 0\n"
    "• max(8%, 24% - 6·N_genuine), if N_genuine > 0 ∧ H_shortlist = 0\n"
    "• 52.0%,  otherwise (Unverified Baseline)\n\n"
    "Mathematical Rationale:\n"
    "Prevents dilution of critical fraud markers. If an offer demands a registration fee, no amount of positive keywords can reduce its risk."
)
p = tf.add_paragraph()
p.text = formula_text
p.font.size = Pt(10.5)
p.font.color.rgb = COLOR_TEXT_DARK

# Right Column: Algorithms & Graph Analytics
c_algo = add_card(slide6, Inches(7.1), Inches(1.5), Inches(5.4), Inches(5.3), bg_color=COLOR_LIGHT_SKY, border_color=COLOR_SKY)
tf = c_algo.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.25)

tf.paragraphs[0].text = "Algorithmic Techniques"
tf.paragraphs[0].font.size = Pt(15)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = COLOR_NAVY

algos = [
    ("1. RapidOCR (ONNX Runtime)", "Employs lightweight text detection and directional angle classification; executes in sub-35ms without GPU."),
    ("2. SHAP (Shapley Additive Explanations)", "Game-theoretic feature attribution assigning exact marginal contribution values to individual words."),
    ("3. Force-Directed Graph Modeling", "vis-network.js physics simulation tracking co-occurrences between burner contacts, UPI handles, and shell company domains."),
    ("4. MCA Corporate Cross-Verification", "Disambiguates legitimate enterprise recruiters against registered Corporate Identification Numbers (CIN).")
]

for title, desc in algos:
    p_t = tf.add_paragraph()
    p_t.text = f"\n• {title}"
    p_t.font.size = Pt(11.5)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_SKY
    p_d = tf.add_paragraph()
    p_d.text = f"  {desc}"
    p_d.font.size = Pt(10)
    p_d.font.color.rgb = COLOR_TEXT_DARK

# ==============================================================================
# SLIDE 7: MODULES SPLIT-UP
# ==============================================================================
slide7 = prs.slides.add_slide(blank_layout)
add_header(slide7, "System Modules Split-Up")

# 4 Grid Cards
grid_w = Inches(5.6)
grid_h = Inches(2.55)

# Module 1
m1 = add_card(slide7, Inches(0.8), Inches(1.5), grid_w, grid_h)
tf = m1.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.2)
tf.paragraphs[0].text = "Module 1: Mobile Chat OCR & Ingestion Gateway"
tf.paragraphs[0].font.size = Pt(14)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = COLOR_SKY
p = tf.add_paragraph()
p.text = "\n• Ingests image formats (PNG, JPG, JPEG) from WhatsApp/Telegram.\n• RapidOCR extracts text blocks with orientation correction.\n• Provides an editable transcript area for manual user verification.\n• Zero-dependency deployment running on standard CPU hardware."
p.font.size = Pt(10.5)
p.font.color.rgb = COLOR_TEXT_DARK

# Module 2
m2 = add_card(slide7, Inches(6.8), Inches(1.5), grid_w, grid_h)
tf = m2.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.2)
tf.paragraphs[0].text = "Module 2: Structured Entity & Transaction Parser"
tf.paragraphs[0].font.size = Pt(14)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = COLOR_SKY
p = tf.add_paragraph()
p.text = "\n• UPI Identifier Extraction: Targets @okaxis, @oksbi, @paytm, @ybl.\n• Compensation Range Parser: Discovers clickbait LPA brackets.\n• Off-Platform Redirections: Detects wa.me/ links and Telegram handles.\n• Role Stacking Counter: Analyzes multi-discipline career bundling."
p.font.size = Pt(10.5)
p.font.color.rgb = COLOR_TEXT_DARK

# Module 3
m3 = add_card(slide7, Inches(0.8), Inches(4.3), grid_w, grid_h)
tf = m3.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.2)
tf.paragraphs[0].text = "Module 3: Multi-Tiered Hybrid Detection Engine"
tf.paragraphs[0].font.size = Pt(14)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = COLOR_SKY
p = tf.add_paragraph()
p.text = "\n• Tier 1: Deterministic Hard Veto on upfront registration fees (98%).\n• Tier 2: Behavioral Phishing Heuristics on unsolicited shortlist hooks (88%).\n• Tier 3: NLP TF-IDF + Classifier trained on recruitment text corpus.\n• Prevents positive keyword dilution using priority veto gates."
p.font.size = Pt(10.5)
p.font.color.rgb = COLOR_TEXT_DARK

# Module 4
m4 = add_card(slide7, Inches(6.8), Inches(4.3), grid_w, grid_h)
tf = m4.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.2)
tf.paragraphs[0].text = "Module 4: Explainability (SHAP) & Syndicate Graph"
tf.paragraphs[0].font.size = Pt(14)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = COLOR_SKY
p = tf.add_paragraph()
p.text = "\n• Plotly Radial Gauge for instant, color-coded risk visualization.\n• SHAP Token Attribution bars justifying word-level risk weights.\n• Interactive vis-network.js force-directed syndicate graph.\n• Community threat reporting feed and recruiter trust telemetry."
p.font.size = Pt(10.5)
p.font.color.rgb = COLOR_TEXT_DARK

# ==============================================================================
# SLIDE 8: PROPOSED SYSTEM & KEY NOVELTIES
# ==============================================================================
slide8 = prs.slides.add_slide(blank_layout)
add_header(slide8, "Proposed System & Architectural Novelty")

# 4 Key Novelties Cards
nov_w = Inches(5.6)
nov_h = Inches(2.55)

# Card 1
c1 = add_card(slide8, Inches(0.8), Inches(1.5), nov_w, nov_h, bg_color=COLOR_LIGHT_SKY, border_color=COLOR_SKY)
tf = c1.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.2)
tf.paragraphs[0].text = "1. Zero-Text Ingestion Dependency"
tf.paragraphs[0].font.size = Pt(14)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = COLOR_NAVY
p = tf.add_paragraph()
p.text = "\n• Traditional systems force students to re-type or copy text from images.\n• TrustHire accepts direct screenshots from WhatsApp, Telegram, or camera roll.\n• RapidOCR executes in <35 ms on CPU with zero cloud latency."
p.font.size = Pt(10.5)
p.font.color.rgb = COLOR_TEXT_DARK

# Card 2
c2 = add_card(slide8, Inches(6.8), Inches(1.5), nov_w, nov_h, bg_color=COLOR_LIGHT_SKY, border_color=COLOR_SKY)
tf = c2.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.2)
tf.paragraphs[0].text = "2. Two-Stage Phishing Funnel Defense"
tf.paragraphs[0].font.size = Pt(14)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = COLOR_NAVY
p = tf.add_paragraph()
p.text = "\n• Scammers deliberately omit fee demands in the initial broadcast.\n• TrustHire detects Stage-1 markers: Unsolicited shortlisting hooks, 5+ stacked divergent roles, and generic keyword spraying.\n• Protects students BEFORE they enter private communication."
p.font.size = Pt(10.5)
p.font.color.rgb = COLOR_TEXT_DARK

# Card 3
c3 = add_card(slide8, Inches(0.8), Inches(4.3), nov_w, nov_h, bg_color=COLOR_LIGHT_SKY, border_color=COLOR_SKY)
tf = c3.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.2)
tf.paragraphs[0].text = "3. Explainable AI via Game-Theoretic SHAP"
tf.paragraphs[0].font.size = Pt(14)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = COLOR_NAVY
p = tf.add_paragraph()
p.text = "\n• Replaces opaque 'black-box' percentages with human-interpretable reasons.\n• Accurately measures token weights (e.g. 'profile shortlisted' +0.38 SCAM vs 'provident fund' -0.36 GENUINE).\n• Empowers students to understand red flags independently."
p.font.size = Pt(10.5)
p.font.color.rgb = COLOR_TEXT_DARK

# Card 4
c4 = add_card(slide8, Inches(6.8), Inches(4.3), nov_w, nov_h, bg_color=COLOR_LIGHT_SKY, border_color=COLOR_SKY)
tf = c4.text_frame
tf.word_wrap = True
tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.2)
tf.paragraphs[0].text = "4. 'Same Scammer, Different Mask' Syndicate Defense"
tf.paragraphs[0].font.size = Pt(14)
tf.paragraphs[0].font.bold = True
tf.paragraphs[0].font.color.rgb = COLOR_NAVY
p = tf.add_paragraph()
p.text = "\n• Fraud syndicates routinely discard domains but reuse phone numbers and UPI IDs.\n• Knowledge Graph traverses multi-hop relationships between shell entities.\n• Automatically blacklists new fake domains linked to known scammer nodes."
p.font.size = Pt(10.5)
p.font.color.rgb = COLOR_TEXT_DARK

# ==============================================================================
# SLIDE 9: SOFTWARE TOOLS & TECHNOLOGIES
# ==============================================================================
slide9 = prs.slides.add_slide(blank_layout)
add_header(slide9, "Software Tools & Technologies Used")

# 4 Tech Cards
tech_w = Inches(2.7)
tech_h = Inches(5.3)
tech_y = Inches(1.5)

techs = [
    ("Core Language &\nUI Framework", "🐍", 
     "• Python 3.12 (64-bit)\n• Streamlit (Web App)\n• Custom CSS Injection (Responsive Sky Blue theme)\n• Streamlit Components (HTML/JS embedding)\n• Virtualenv Architecture"),
    ("OCR & Computer\nVision", "👁️", 
     "• RapidOCR (ONNX Runtime)\n• Pure Python implementation\n• Zero C++ dependencies\n• Pillow (PIL Image Engine)\n• NumPy Array Preprocessing\n• Layout Text Bounding Boxes"),
    ("Machine Learning\n& XAI", "🧠", 
     "• Scikit-learn (TF-IDF)\n• PassiveAggressive Classifier\n• Logistic Regression\n• SHAP (Shapley Additive exPlanations)\n• RegEx Pattern Matchers\n• Serialized PKL Artifacts"),
    ("Graph & Visual\nAnalytics", "📊", 
     "• Plotly Graph Objects (Interactive Radial Gauge)\n• vis-network.js (Force-directed graph)\n• Pandas DataFrames\n• Git & GitHub Version Control\n• VS Code IDE")
]

for i, (title, icon, details) in enumerate(techs):
    card = add_card(slide9, Inches(0.8 + i*3.0), tech_y, tech_w, tech_h)
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.25)
    
    p0 = tf.paragraphs[0]
    p0.text = icon
    p0.font.size = Pt(22)
    
    p1 = tf.add_paragraph()
    p1.text = title
    p1.font.size = Pt(13)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_SKY
    
    p2 = tf.add_paragraph()
    p2.text = f"\n{details}"
    p2.font.size = Pt(10)
    p2.font.color.rgb = COLOR_TEXT_DARK

# ==============================================================================
# SLIDE 10: WORKING MODULE & EVALUATION
# ==============================================================================
slide10 = prs.slides.add_slide(blank_layout)
add_header(slide10, "Working Module: Live Demo & Test Scenarios")

# 5 Test Case Cards
tc_w = Inches(11.733)
tc_h = Inches(0.85)

test_cases = [
    ("🟢 Test Case 1: Genuine Infosys Campus Drive", "12.0% (VERIFIED)", COLOR_GREEN, 
     "Verified enterprise domain (@infosys.com), standard statutory benefits (PF, Medical), explicit zero-fee hiring disclaimer."),
    ("🚨 Test Case 2: Fake TCS Internship Fee Scam", "98.0% (HARD VETO)", COLOR_RED, 
     "Mandatory upfront ₹999 UPI fee to 'reserve seat & dispatch training kit'. Immediate Hard Veto triggered."),
    ("📱 Test Case 3: Mobile WhatsApp YouTube Task Scam", "80.0% (HIGH RISK)", COLOR_RED, 
     "Daily payout micro-task scheme (₹3,000–₹5,000/day for liking videos), instant GPay/PhonePe transfer via WhatsApp HR."),
    ("🕸️ Test Case 4: Syndicate Recruiter Contact Ring", "94.0% (HARD VETO)", COLOR_RED, 
     "Recruiter contact (+91-9876543210) co-occurs across 3 shell companies (Apex Tech, Global Task, TCS Hub) in Scam Graph."),
    ("🎣 Test Case 5: Real WhatsApp Screenshot (User Test)", "88.0% (HIGH RISK)", COLOR_RED, 
     "Stage-1 Phishing Hook: Claims profile shortlisted for 5 divergent roles (Dev, QA, Support, Analyst) at ₹2.5–₹6.5 LPA.")
]

for i, (name, score_txt, badge_col, desc) in enumerate(test_cases):
    card = add_card(slide10, Inches(0.8), Inches(1.5 + i*1.0), tc_w, tc_h)
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.12)
    
    p = tf.paragraphs[0]
    p.text = f"{name}   ➔   "
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY
    
    # Add score
    p_score = tf.add_paragraph()
    p_score.text = f"Verdict: {score_txt}  |  {desc}"
    p_score.font.size = Pt(10)
    p_score.font.color.rgb = badge_col
    p_score.font.bold = True

tb_demo = slide10.shapes.add_textbox(Inches(0.8), Inches(6.6), Inches(11.733), Inches(0.4))
p = tb_demo.text_frame.paragraphs[0]
p.text = "⚡ Live Application Running locally at http://localhost:8501  •  Ready for interactive examiner inspection."
p.font.size = Pt(11)
p.font.bold = True
p.font.color.rgb = COLOR_SKY

# ==============================================================================
# SLIDE 11: PARTIAL REPORT STATUS (SEMESTER – I)
# ==============================================================================
slide11 = prs.slides.add_slide(blank_layout)
add_header(slide11, "Partial Report Status: Semester – I Deliverables")

# 2 Columns: Completed Artifacts
c1 = add_card(slide11, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.3))
tf1 = c1.text_frame
tf1.word_wrap = True
tf1.margin_left = tf1.margin_right = tf1.margin_top = Inches(0.25)
tf1.paragraphs[0].text = "Completed Academic Deliverables"
tf1.paragraphs[0].font.size = Pt(15)
tf1.paragraphs[0].font.bold = True
tf1.paragraphs[0].font.color.rgb = COLOR_NAVY

items1 = [
    "✅ Problem Definition & Title Approval",
    "✅ Comprehensive Literature Review (15+ Papers Indexed)",
    "✅ IEEE 830-Compliant SRS Documentation",
    "✅ Phase III: System Design Completed",
    "    • Fig 1. Architecture Diagram",
    "    • Fig 2.1, 2.2, 2.3 Data Flow Diagrams (DFD Level 0, 1, 2)",
    "    • Fig 3.1 Use Case Diagram (UML)",
    "    • Fig 3.2 Class Diagram (UML)",
    "    • Fig 3.3 Activity Diagram (UML Dual-Swimlane)",
    "✅ Working Interactive Prototype Developed"
]
for it in items1:
    p = tf1.add_paragraph()
    p.text = it
    p.font.size = Pt(10.5)
    p.font.color.rgb = COLOR_TEXT_DARK

c2 = add_card(slide11, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.3), bg_color=COLOR_LIGHT_SKY, border_color=COLOR_SKY)
tf2 = c2.text_frame
tf2.word_wrap = True
tf2.margin_left = tf2.margin_right = tf2.margin_top = Inches(0.25)
tf2.paragraphs[0].text = "Technical Prototype Readiness"
tf2.paragraphs[0].font.size = Pt(15)
tf2.paragraphs[0].font.bold = True
tf2.paragraphs[0].font.color.rgb = COLOR_NAVY

items2 = [
    "✅ Streamlit Frontend UI (Edge-to-edge, Sky Blue palette)",
    "✅ Embedded RapidOCR Pipeline for Chat Screenshots",
    "✅ Regex Entity Parser (UPI, Salary, Phone, Roles)",
    "✅ 4-Tier Hierarchical Decision Scoring Engine",
    "✅ Explainable AI (SHAP Feature Attribution Bars)",
    "✅ Force-Directed vis-network.js Scam Graph",
    "✅ 5 Comprehensive Real-World Test Cases Pre-loaded",
    "✅ Public GitHub Repository Configured & Pushed",
    "    URL: github.com/ishitashimpi18/TrustHire",
    "✅ One-Click Windows Launcher Script (run_demo.bat)"
]
for it in items2:
    p = tf2.add_paragraph()
    p.text = it
    p.font.size = Pt(10.5)
    p.font.color.rgb = COLOR_TEXT_DARK

# ==============================================================================
# SLIDE 12: PROJECT PLAN 2.0 (SEMESTER – II ROADMAP)
# ==============================================================================
slide12 = prs.slides.add_slide(blank_layout)
add_header(slide12, "Project Plan 2.0: Timeline & Roadmap (Towards April 2027)")

# 4 Horizontal Phases
phase_w = Inches(2.7)
phase_h = Inches(4.5)
phase_y = Inches(1.5)

phases = [
    ("Phase 1: Deep Learning", "Nov – Dec 2026", 
     "• Expand labeled corpus with 5,000+ mobile chat screenshots.\n• Fine-tune RoBERTa / DeBERTa transformer embeddings.\n• Implement multimodal cross-attention (Text + Image tokens)."),
    ("Phase 2: Graph Intelligence", "Jan – Feb 2027", 
     "• Graph Neural Networks (GCN) for dynamic community fraud clustering.\n• Automated MCA CIN API corporate registry ingestion.\n• Syndicate link prediction algorithm."),
    ("Phase 3: Integration", "Mar 2027", 
     "• Lightweight Chrome Browser Extension for LinkedIn / Naukri.\n• Automated WhatsApp Forwarding Verification Bot.\n• Cloud deployment on secure student portal."),
    ("Phase 4: Publication & Final", "Apr 2027", 
     "• Comprehensive empirical benchmarking against baseline models.\n• Author and submit research paper to IEEE/Springer conference.\n• SPPU Final University Capstone Defense.")
]

for i, (title, time_txt, tasks) in enumerate(phases):
    card = add_card(slide12, Inches(0.8 + i*3.0), phase_y, phase_w, phase_h)
    tf = card.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = Inches(0.2)
    
    p0 = tf.paragraphs[0]
    p0.text = time_txt
    p0.font.size = Pt(11)
    p0.font.bold = True
    p0.font.color.rgb = COLOR_SKY
    
    p1 = tf.add_paragraph()
    p1.text = title
    p1.font.size = Pt(13)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_NAVY
    
    p2 = tf.add_paragraph()
    p2.text = f"\n{tasks}"
    p2.font.size = Pt(10)
    p2.font.color.rgb = COLOR_TEXT_DARK

# Bottom closing
tb_close = slide12.shapes.add_textbox(Inches(0.8), Inches(6.3), Inches(11.733), Inches(0.6))
p = tb_close.text_frame.paragraphs[0]
p.text = "🎯 Summary: Semester I milestones fully completed. Ready for Review-III examination and Semester II execution."
p.font.size = Pt(12)
p.font.bold = True
p.font.color.rgb = COLOR_GREEN

prs.save(OUTPUT_FILE)
print(f"✓ PowerPoint presentation successfully created: {OUTPUT_FILE}")
