import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Circle, Polygon, Wedge

OUTPUT_DIR = r"C:\TrustHire\diagrams"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Common styling configuration
FONT_FAMILY = "sans-serif"
COLOR_PRIMARY_DARK = "#0F172A"      # Slate 900
COLOR_PRIMARY_BLUE = "#0284C7"      # Sky Blue 600
COLOR_ACCENT_BG = "#F0F9FF"         # Sky 50
COLOR_CARD_BG = "#FFFFFF"           # White
COLOR_BORDER = "#0F172A"            # Dark outline
COLOR_TEXT_DARK = "#0F172A"         # Dark Text
COLOR_TEXT_MUTED = "#475569"        # Muted Text
COLOR_DATABASE = "#1E293B"          # Database Cylinder Dark
COLOR_YELLOW = "#FEF08A"            # Decision Diamond

# -------------------------------------------------------------
# HELPER FUNCTIONS
# -------------------------------------------------------------
def draw_rounded_box(ax, x, y, w, h, text, title="", bg_color=COLOR_CARD_BG, border_color=COLOR_BORDER, border_width=1.5, text_color=COLOR_TEXT_DARK, font_size=10, bold=False):
    box = FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.03", 
                         facecolor=bg_color, edgecolor=border_color, linewidth=border_width, zorder=2)
    ax.add_patch(box)
    
    full_text = f"{title}\n{text}".strip() if title else text
    weight = "bold" if bold else "normal"
    ax.text(x + w/2, y + h/2, full_text, ha="center", va="center", fontsize=font_size, 
            color=text_color, family=FONT_FAMILY, weight=weight, zorder=3)

def draw_cylinder(ax, x, y, w, h, text="DATABASE", bg_color="#FFFFFF", border_color=COLOR_BORDER, text_color=COLOR_TEXT_DARK, font_size=9):
    # Cylinder body
    rect = patches.Rectangle((x, y + h*0.12), w, h*0.76, facecolor=bg_color, edgecolor="none", zorder=2)
    ax.add_patch(rect)
    
    # Left and right vertical borders
    ax.plot([x, x], [y + h*0.12, y + h*0.88], color=border_color, lw=1.5, zorder=3)
    ax.plot([x + w, x + w], [y + h*0.12, y + h*0.88], color=border_color, lw=1.5, zorder=3)
    
    # Disk lines to represent database
    for y_offset in [0.35, 0.60]:
        ellipse_mid = patches.Arc((x + w/2, y + h*y_offset), w, h*0.25, angle=0, theta1=180, theta2=360, color=border_color, lw=1.5, zorder=3)
        ax.add_patch(ellipse_mid)
        
    # Bottom ellipse arc
    ellipse_bottom = patches.Arc((x + w/2, y + h*0.12), w, h*0.25, angle=0, theta1=180, theta2=360, color=border_color, lw=1.5, zorder=3)
    ax.add_patch(ellipse_bottom)
    
    # Top ellipse (full)
    ellipse_top = patches.Ellipse((x + w/2, y + h*0.88), w, h*0.25, facecolor=bg_color, edgecolor=border_color, lw=1.5, zorder=3)
    ax.add_patch(ellipse_top)
    
    ax.text(x + w/2, y + h*0.48, text, ha="center", va="center", fontsize=font_size, color=text_color, weight="bold", zorder=4)

def draw_diamond(ax, x, y, size, text, bg_color=COLOR_YELLOW, border_color=COLOR_BORDER, font_size=9):
    pts = [[x, y + size/2], [x + size/2, y + size], [x + size, y + size/2], [x + size/2, y]]
    poly = patches.Polygon(pts, closed=True, facecolor=bg_color, edgecolor=border_color, lw=1.5, zorder=2)
    ax.add_patch(poly)
    ax.text(x + size/2, y + size/2, text, ha="center", va="center", fontsize=font_size, weight="bold", color=COLOR_TEXT_DARK, zorder=3)

def draw_oval(ax, x, y, w, h, text, bg_color="#FFFFFF", border_color=COLOR_BORDER, font_size=10, bold=False):
    ellipse = patches.Ellipse((x + w/2, y + h/2), w, h, facecolor=bg_color, edgecolor=border_color, lw=1.5, zorder=2)
    ax.add_patch(ellipse)
    weight = "bold" if bold else "normal"
    ax.text(x + w/2, y + h/2, text, ha="center", va="center", fontsize=font_size, weight=weight, color=COLOR_TEXT_DARK, zorder=3)

def draw_arrow(ax, x1, y1, x2, y2, label="", label_pos=(0.5, 0.5), color="#0F172A", lw=1.2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=12), zorder=1)
    if label:
        lx = x1 + (x2 - x1) * label_pos[0]
        ly = y1 + (y2 - y1) * label_pos[1]
        ax.text(lx, ly, label, fontsize=8, color=COLOR_TEXT_MUTED, weight="bold", ha="center", va="center",
                bbox=dict(boxstyle="square,pad=0.1", fc="#FFFFFF", ec="none"), zorder=4)

def draw_stick_figure(ax, cx, cy, height=0.18, label=""):
    # Head
    head_radius = height * 0.16
    head = Circle((cx, cy + height - head_radius), head_radius, facecolor="none", edgecolor=COLOR_BORDER, lw=1.8, zorder=3)
    ax.add_patch(head)
    
    # Body
    body_top_y = cy + height - 2*head_radius
    body_bottom_y = cy + height * 0.35
    ax.plot([cx, cx], [body_top_y, body_bottom_y], color=COLOR_BORDER, lw=1.8, zorder=3)
    
    # Arms
    arm_y = cy + height * 0.65
    arm_span = height * 0.35
    ax.plot([cx - arm_span/2, cx + arm_span/2], [arm_y, arm_y], color=COLOR_BORDER, lw=1.8, zorder=3)
    
    # Legs
    leg_span = height * 0.32
    ax.plot([cx, cx - leg_span/2], [body_bottom_y, cy], color=COLOR_BORDER, lw=1.8, zorder=3)
    ax.plot([cx, cx + leg_span/2], [body_bottom_y, cy], color=COLOR_BORDER, lw=1.8, zorder=3)
    
    if label:
        ax.text(cx, cy - 0.035, label, ha="center", va="top", fontsize=9.5, weight="bold", color=COLOR_TEXT_DARK, zorder=4)

# =============================================================
# 1. FIG 1: ARCHITECTURE DIAGRAM
# =============================================================
def generate_fig1_architecture():
    fig, ax = plt.subplots(figsize=(10, 8.8), dpi=300)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    
    # Outer frame - comfortably below the heading line
    frame = patches.Rectangle((0.03, 0.06), 0.94, 0.81, fill=False, edgecolor="#0F172A", lw=1.5)
    ax.add_patch(frame)
    
    # Headers - Cleanly positioned ABOVE the box with generous breathing room
    fig.text(0.08, 0.965, "Phase III: Design Phase", fontsize=13, weight="bold", family=FONT_FAMILY)
    fig.text(0.50, 0.915, "1. TrustHire Platform Architecture", fontsize=14, weight="bold", ha="center", family=FONT_FAMILY)
    fig.text(0.50, 0.02, "Fig1. Architecture", fontsize=12, weight="bold", ha="center", family=FONT_FAMILY)
    
    # Blocks
    # User Block
    draw_rounded_box(ax, 0.08, 0.69, 0.15, 0.09, "USER\n(Candidate)", bg_color="#1E3A8A", text_color="#FFFFFF", border_color="#1E3A8A", bold=True)
    
    # Ingestion Block
    draw_rounded_box(ax, 0.30, 0.69, 0.16, 0.09, "JOB OFFER\nINGESTION\n(Text / Image)", bold=True, bg_color="#F8FAFC")
    
    # OCR & Entity Parser
    draw_rounded_box(ax, 0.54, 0.69, 0.16, 0.09, "RAPID OCR &\nENTITY PARSER\n(UPI, Salary, Roles)", bold=True, bg_color="#F0F9FF", border_color=COLOR_PRIMARY_BLUE)
    
    # Database
    draw_cylinder(ax, 0.76, 0.39, 0.16, 0.22, "TRUSTHIRE\nDATABASE\n(Syndicates, Logs,\nMCA Registry)")
    
    # Hybrid Detection Engine
    draw_rounded_box(ax, 0.48, 0.43, 0.20, 0.12, "HYBRID DETECTION\nENGINE\n• Hard Vetoes (Fees)\n• Phishing Heuristics\n• TF-IDF + Classifier", bold=True, bg_color="#FEF3C7", border_color="#D97706", font_size=8.5)
    
    # Explainable AI (SHAP)
    draw_rounded_box(ax, 0.26, 0.43, 0.16, 0.12, "EXPLAINABLE AI\n(XAI)\n• SHAP Token Weights\n• Triggered Factors", bold=True, bg_color="#F0FDF4", border_color="#16A34A", font_size=8.5)
    
    # Student Dashboard
    draw_rounded_box(ax, 0.08, 0.43, 0.14, 0.12, "STUDENT\nVERDICT\nDASHBOARD\n(Risk Gauge)", bold=True, bg_color="#EFF6FF", border_color="#3B82F6", font_size=8.5)
    
    # Vis-Network Syndicate Graph (Admin)
    draw_rounded_box(ax, 0.08, 0.15, 0.22, 0.11, "SYNDICATE GRAPH\nDEFENSE\n(vis-network.js Ring Map)", bold=True, bg_color="#1E3A8A", text_color="#FFFFFF", border_color="#1E3A8A", font_size=9)
    
    # MCA Corporate Registry Verification
    draw_rounded_box(ax, 0.38, 0.15, 0.20, 0.11, "MCA CORPORATE\nREGISTRY AUDIT\n(CIN & Portal Match)", bold=True, bg_color="#F8FAFC", font_size=9)
    
    # Telemetry & Community Feed
    draw_rounded_box(ax, 0.66, 0.15, 0.24, 0.11, "THREAT TELEMETRY\n& RECRUITER\nLEADERBOARD", bold=True, bg_color="#F8FAFC", font_size=9)
    
    # Connectors
    draw_arrow(ax, 0.23, 0.735, 0.30, 0.735)
    draw_arrow(ax, 0.46, 0.735, 0.54, 0.735)
    draw_arrow(ax, 0.70, 0.735, 0.84, 0.735)
    draw_arrow(ax, 0.84, 0.735, 0.84, 0.61, label="Structured Feed")
    
    # Database to Engine & Engine flow
    draw_arrow(ax, 0.76, 0.49, 0.68, 0.49, label="Blacklist")
    draw_arrow(ax, 0.48, 0.49, 0.42, 0.49)
    draw_arrow(ax, 0.26, 0.49, 0.22, 0.49)
    
    # Bottom flow
    draw_arrow(ax, 0.84, 0.39, 0.84, 0.26)
    draw_arrow(ax, 0.66, 0.205, 0.58, 0.205)
    draw_arrow(ax, 0.38, 0.205, 0.30, 0.205)
    
    # Feedback loop to student dashboard
    draw_arrow(ax, 0.19, 0.26, 0.15, 0.43)
    
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "Fig1_Architecture.png"), dpi=300, bbox_inches="tight")
    plt.close()

# =============================================================
# 2. FIG 2.1 & FIG 2.2: DFD LEVEL 0 AND LEVEL 1
# =============================================================
def generate_dfd_diagrams():
    # Fig 2.1 Level 0 DFD
    fig, ax = plt.subplots(figsize=(9, 4), dpi=300)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    
    # Top grey banner like reference
    banner = patches.Rectangle((0.05, 0.25), 0.90, 0.60, facecolor="#F1F5F9", edgecolor="none", zorder=0)
    ax.add_patch(banner)
    
    draw_rounded_box(ax, 0.08, 0.42, 0.18, 0.24, "Student /\nJob Seeker", bold=True, font_size=10.5)
    draw_oval(ax, 0.40, 0.38, 0.22, 0.32, "0.0\nTrustHire Fraud\nDetection System", bold=True, font_size=10)
    draw_rounded_box(ax, 0.74, 0.42, 0.18, 0.24, "Risk Verdict &\nSHAP Explainable\nReport", bold=True, font_size=10)
    
    draw_arrow(ax, 0.26, 0.54, 0.40, 0.54, label="Job Text / Screenshot")
    draw_arrow(ax, 0.62, 0.54, 0.74, 0.54, label="Risk % & Factors")
    
    fig.text(0.50, 0.10, "Fig 2.1 Level 0 DFD", fontsize=12, weight="bold", ha="center", family=FONT_FAMILY)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "Fig2_1_Level0_DFD.png"), dpi=300, bbox_inches="tight")
    plt.close()
    
    # Fig 2.2 Level 1 DFD
    fig, ax = plt.subplots(figsize=(9.5, 7.5), dpi=300)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    
    # Outer rectangle system boundary
    sys_box = patches.Rectangle((0.32, 0.12), 0.36, 0.80, facecolor="#F8FAFC", edgecolor=COLOR_BORDER, lw=1.8, zorder=1)
    ax.add_patch(sys_box)
    ax.text(0.50, 0.88, "TrustHire Processing Subsystems", ha="center", fontsize=10.5, weight="bold")
    
    draw_rounded_box(ax, 0.04, 0.46, 0.20, 0.18, "Job Seeker\n(Text / Screenshot\nInput)", bold=True, font_size=9.5)
    draw_rounded_box(ax, 0.76, 0.46, 0.20, 0.18, "Inspection Output\n(Radial Gauge, Factors,\nSyndicate Graph)", bold=True, font_size=9.5)
    
    # Internal processes (Ovals)
    draw_oval(ax, 0.35, 0.71, 0.30, 0.14, "1.0 RapidOCR &\nImage Ingestion", font_size=9, bold=True)
    draw_oval(ax, 0.35, 0.52, 0.30, 0.14, "2.0 Entity Extraction\n(UPI, Salary, Roles)", font_size=9, bold=True)
    draw_oval(ax, 0.35, 0.33, 0.30, 0.14, "3.0 Tiered Scoring\n(Hard Veto + Phishing)", font_size=9, bold=True)
    draw_oval(ax, 0.35, 0.15, 0.30, 0.14, "4.0 Explainability & Graph\n(SHAP + vis-network)", font_size=9, bold=True)
    
    # Connectors
    draw_arrow(ax, 0.24, 0.55, 0.35, 0.76)
    draw_arrow(ax, 0.24, 0.55, 0.35, 0.58)
    
    draw_arrow(ax, 0.50, 0.71, 0.50, 0.66)
    draw_arrow(ax, 0.50, 0.52, 0.50, 0.47)
    draw_arrow(ax, 0.50, 0.33, 0.50, 0.29)
    
    draw_arrow(ax, 0.65, 0.38, 0.76, 0.52)
    draw_arrow(ax, 0.65, 0.22, 0.76, 0.52)
    
    fig.text(0.50, 0.04, "Fig 2.2 Level 1 DFD", fontsize=12, weight="bold", ha="center", family=FONT_FAMILY)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "Fig2_2_Level1_DFD.png"), dpi=300, bbox_inches="tight")
    plt.close()

# =============================================================
# 3. FIG 2.3: LEVEL 2 DFD (PIPELINE)
# =============================================================
def generate_fig2_3_level2_dfd():
    fig, ax = plt.subplots(figsize=(10.5, 3.5), dpi=300)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    
    box_w = 0.14
    box_h = 0.42
    y_pos = 0.32
    
    draw_rounded_box(ax, 0.03, y_pos, box_w, box_h, "Input Offer\n(Screenshot /\nRaw Text)", bold=True, font_size=8.5)
    draw_rounded_box(ax, 0.22, y_pos, box_w, box_h, "3.1 RapidOCR &\nPreprocessing", bold=True, font_size=8.5, bg_color="#F0F9FF")
    draw_rounded_box(ax, 0.41, y_pos, box_w, box_h, "3.2 Entity Parser\n(UPI, Phone, Roles)", bold=True, font_size=8.5, bg_color="#F0F9FF")
    draw_rounded_box(ax, 0.60, y_pos, box_w, box_h, "3.3 Hard Veto &\nPhishing Classifier", bold=True, font_size=8.5, bg_color="#FEF3C7")
    draw_rounded_box(ax, 0.79, y_pos, box_w, box_h, "Output Report\n(Risk Verdict,\nSHAP & Graph)", bold=True, font_size=8.5, bg_color="#F0FDF4")
    
    draw_arrow(ax, 0.17, 0.53, 0.22, 0.53)
    draw_arrow(ax, 0.36, 0.53, 0.41, 0.53)
    draw_arrow(ax, 0.55, 0.53, 0.60, 0.53)
    draw_arrow(ax, 0.74, 0.53, 0.79, 0.53)
    
    fig.text(0.50, 0.10, "Fig 2.3 Level 2 DFD", fontsize=12, weight="bold", ha="center", family=FONT_FAMILY)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "Fig2_3_Level2_DFD.png"), dpi=300, bbox_inches="tight")
    plt.close()

# =============================================================
# 4. FIG 3.1: USE CASE DIAGRAM (UML)
# =============================================================
def generate_fig3_1_usecase():
    fig, ax = plt.subplots(figsize=(8.5, 9.5), dpi=300)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    
    fig.text(0.50, 0.95, "3. UML Diagrams", fontsize=14, weight="bold", ha="center", family=FONT_FAMILY)
    
    # System boundary
    rect = patches.Rectangle((0.28, 0.10), 0.44, 0.80, facecolor="#FFFFFF", edgecolor=COLOR_BORDER, lw=1.8, zorder=1)
    ax.add_patch(rect)
    ax.text(0.50, 0.865, "TrustHire AI Platform", ha="center", fontsize=12, weight="bold")
    
    # Left Actor: Student
    draw_stick_figure(ax, 0.12, 0.48, height=0.18, label="Student /\nCandidate")
    
    # Right Actors: Instructor & Admin
    draw_stick_figure(ax, 0.88, 0.62, height=0.17, label="Faculty / Guide")
    draw_stick_figure(ax, 0.88, 0.26, height=0.17, label="Admin / Fraud\nInvestigator")
    
    # Use cases (Ovals inside boundary)
    cases = [
        (0.78, "Upload Chat Screenshot"),
        (0.66, "Scan Job Description"),
        (0.54, "View Risk % & Radial Gauge"),
        (0.42, "Inspect SHAP Token Explanations"),
        (0.30, "Explore Syndicate Network Graph"),
        (0.18, "Audit Recruiter & MCA Data")
    ]
    
    for y_val, text in cases:
        draw_oval(ax, 0.31, y_val, 0.38, 0.08, text, font_size=9, bold=True, bg_color="#F8FAFC")
        # Line from student to all use cases
        ax.plot([0.16, 0.31], [0.57, y_val + 0.04], color=COLOR_BORDER, lw=1.2, zorder=2)
    
    # Right actor connections
    # Faculty/Guide connections
    ax.plot([0.69, 0.84], [0.58, 0.70], color=COLOR_BORDER, lw=1.2, zorder=2)
    ax.plot([0.69, 0.84], [0.46, 0.70], color=COLOR_BORDER, lw=1.2, zorder=2)
    
    # Admin connections
    ax.plot([0.69, 0.84], [0.34, 0.35], color=COLOR_BORDER, lw=1.2, zorder=2)
    ax.plot([0.69, 0.84], [0.22, 0.35], color=COLOR_BORDER, lw=1.2, zorder=2)
    
    fig.text(0.50, 0.03, "Fig 3.1 Use Case Diagram", fontsize=12, weight="bold", ha="center", family=FONT_FAMILY)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "Fig3_1_UseCase_Diagram.png"), dpi=300, bbox_inches="tight")
    plt.close()

# =============================================================
# 5. FIG 3.2: CLASS DIAGRAM (UML)
# =============================================================
def generate_fig3_2_class_diagram():
    fig, ax = plt.subplots(figsize=(10.5, 9.5), dpi=300)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    
    def draw_uml_class(x, y, w, h, class_name, attrs, methods):
        # Outer box
        rect = patches.Rectangle((x, y), w, h, facecolor="#FFFFFF", edgecolor=COLOR_BORDER, lw=1.5, zorder=2)
        ax.add_patch(rect)
        
        # Header box
        header_h = h * 0.22
        h_rect = patches.Rectangle((x, y + h - header_h), w, header_h, facecolor="#F1F5F9", edgecolor=COLOR_BORDER, lw=1.5, zorder=3)
        ax.add_patch(h_rect)
        ax.text(x + w/2, y + h - header_h/2, class_name, ha="center", va="center", fontsize=9.5, weight="bold", zorder=4)
        
        # Split attributes and methods
        attr_h = (h - header_h) * 0.48
        ax.plot([x, x + w], [y + h - header_h - attr_h, y + h - header_h - attr_h], color=COLOR_BORDER, lw=1.2, zorder=3)
        
        # Attributes text
        ax.text(x + 0.015, y + h - header_h - 0.02, "\n".join(attrs), va="top", fontsize=7.5, color=COLOR_TEXT_DARK, zorder=4)
        
        # Methods text
        ax.text(x + 0.015, y + h - header_h - attr_h - 0.02, "\n".join(methods), va="top", fontsize=7.5, color=COLOR_TEXT_DARK, zorder=4)

    # Class 1: Candidate / Student
    draw_uml_class(0.05, 0.70, 0.26, 0.24, "JobApplicant", 
                   ["applicantID : string", "email : string", "uploadedImage : Image", "pastedText : string"],
                   ["submitPosting() : void", "uploadScreenshot() : void", "viewVerdict() : Report"])
                   
    # Class 2: RapidOCREngine
    draw_uml_class(0.38, 0.70, 0.26, 0.24, "RapidOCREngine", 
                   ["modelPath : string", "confidenceThreshold : float", "language : string"],
                   ["extractText(img) : string", "detectBoundingBoxes() : list", "preprocessImage() : array"])
                   
    # Class 3: StructuredEntityParser
    draw_uml_class(0.70, 0.70, 0.26, 0.24, "StructuredEntityParser", 
                   ["upiRegexList : list", "salaryRegexList : list", "phonePattern : regex"],
                   ["extractUPIHandles() : list", "parseSalaryBracket() : string", "countStackedRoles() : int"])
                   
    # Class 4: DetectionEngine
    draw_uml_class(0.05, 0.35, 0.26, 0.26, "TieredDetectionEngine", 
                   ["feePatterns : list", "syndicateContacts : list", "phishingThreshold : float"],
                   ["evaluateHardVeto() : bool", "evaluatePhishingBait() : float", "computeCompositeScore() : float"])
                   
    # Class 5: SHAPExplainer
    draw_uml_class(0.38, 0.35, 0.26, 0.26, "SHAPExplainer", 
                   ["vectorizer : TFIDF", "classifier : Model", "featureNames : list"],
                   ["computeShapValues() : list", "getTopScamTokens() : list", "getGenuineTokens() : list"])
                   
    # Class 6: ScamNetworkGraph
    draw_uml_class(0.70, 0.35, 0.26, 0.26, "ScamNetworkGraph", 
                   ["nodes : list", "edges : list", "shellDomains : list"],
                   ["addPhoneActor() : void", "traverseLinks() : list", "renderVisNetwork() : html"])
                   
    # Class 7: DatabaseService
    draw_uml_class(0.38, 0.06, 0.26, 0.20, "DatabaseService", 
                   ["connectionUri : string", "syndicateRegistry : table", "mcaDirectory : table"],
                   ["querySyndicatePhone() : bool", "logScanResult() : void", "fetchThreatTelemetry() : dict"])
                   
    # Association Arrows
    draw_arrow(ax, 0.31, 0.82, 0.38, 0.82)
    draw_arrow(ax, 0.64, 0.82, 0.70, 0.82)
    draw_arrow(ax, 0.83, 0.70, 0.83, 0.61)
    draw_arrow(ax, 0.18, 0.70, 0.18, 0.61)
    draw_arrow(ax, 0.31, 0.48, 0.38, 0.48)
    draw_arrow(ax, 0.64, 0.48, 0.70, 0.48)
    draw_arrow(ax, 0.51, 0.35, 0.51, 0.26)
    
    fig.text(0.50, 0.015, "Fig 3.2 Class Diagram", fontsize=12, weight="bold", ha="center", family=FONT_FAMILY)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "Fig3_2_Class_Diagram.png"), dpi=300, bbox_inches="tight")
    plt.close()

# =============================================================
# 6. FIG 3.3: ACTIVITY DIAGRAM (UML)
# =============================================================
def generate_fig3_3_activity_diagram():
    fig, ax = plt.subplots(figsize=(9.5, 9.5), dpi=300)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    
    # Column Headers like reference
    ax.text(0.28, 0.94, "Student / Candidate Side", ha="center", fontsize=12, weight="bold")
    ax.text(0.72, 0.94, "Admin / Investigator Side", ha="center", fontsize=12, weight="bold")
    
    # Swimlane vertical divider
    ax.plot([0.50, 0.50], [0.08, 0.92], color="#94A3B8", lw=1.2, ls="--")
    
    # ---------------- Student Side ----------------
    # Start node
    start1 = Circle((0.28, 0.89), 0.02, facecolor="#000000", edgecolor="#000000", zorder=3)
    ax.add_patch(start1)
    
    draw_rounded_box(ax, 0.15, 0.76, 0.26, 0.07, "Upload Chat Screenshot\nor Paste Job Text", bold=True, font_size=8.5)
    draw_diamond(ax, 0.24, 0.64, 0.08, "Image?", font_size=8)
    draw_rounded_box(ax, 0.04, 0.53, 0.20, 0.06, "Run RapidOCR &\nExtract Text", font_size=8, bold=True, bg_color="#F0F9FF")
    draw_rounded_box(ax, 0.15, 0.42, 0.26, 0.06, "Entity Parser (UPI, Salary, Roles)", font_size=8, bold=True)
    draw_rounded_box(ax, 0.15, 0.31, 0.26, 0.06, "Evaluate Hard Veto & Phishing", font_size=8, bold=True, bg_color="#FEF3C7")
    draw_rounded_box(ax, 0.15, 0.20, 0.26, 0.06, "View Risk Gauge & SHAP Factors", font_size=8, bold=True, bg_color="#F0FDF4")
    
    # End node (bullseye)
    end1_out = Circle((0.28, 0.10), 0.022, facecolor="none", edgecolor="#000000", lw=1.8, zorder=3)
    end1_in = Circle((0.28, 0.10), 0.013, facecolor="#000000", edgecolor="#000000", zorder=4)
    ax.add_patch(end1_out)
    ax.add_patch(end1_in)
    
    # Student connections
    draw_arrow(ax, 0.28, 0.87, 0.28, 0.83)
    draw_arrow(ax, 0.28, 0.76, 0.28, 0.72)
    # Decision branch
    draw_arrow(ax, 0.24, 0.68, 0.14, 0.59, label="Yes")
    draw_arrow(ax, 0.14, 0.53, 0.24, 0.48)
    draw_arrow(ax, 0.32, 0.68, 0.32, 0.48, label="No (Text)")
    draw_arrow(ax, 0.28, 0.42, 0.28, 0.37)
    draw_arrow(ax, 0.28, 0.31, 0.28, 0.26)
    draw_arrow(ax, 0.28, 0.20, 0.28, 0.125)
    
    # ---------------- Admin Side ----------------
    start2 = Circle((0.72, 0.89), 0.02, facecolor="#000000", edgecolor="#000000", zorder=3)
    ax.add_patch(start2)
    
    draw_rounded_box(ax, 0.59, 0.76, 0.26, 0.07, "Admin / Investigator\nAuthentication", bold=True, font_size=8.5)
    draw_diamond(ax, 0.68, 0.64, 0.08, "Auth?", font_size=8)
    
    draw_rounded_box(ax, 0.59, 0.50, 0.26, 0.07, "Access Threat Telemetry\n& Flagged Feed", bold=True, font_size=8.5)
    draw_rounded_box(ax, 0.59, 0.36, 0.26, 0.07, "Traverse Syndicate Graph\n(vis-network.js)", bold=True, font_size=8.5, bg_color="#EFF6FF")
    draw_rounded_box(ax, 0.59, 0.22, 0.26, 0.07, "Update Blacklist & Audit\nMCA Disclosures", bold=True, font_size=8.5, bg_color="#FEF2F2")
    
    end2_out = Circle((0.72, 0.10), 0.022, facecolor="none", edgecolor="#000000", lw=1.8, zorder=3)
    end2_in = Circle((0.72, 0.10), 0.013, facecolor="#000000", edgecolor="#000000", zorder=4)
    ax.add_patch(end2_out)
    ax.add_patch(end2_in)
    
    # Admin connections
    draw_arrow(ax, 0.72, 0.87, 0.72, 0.83)
    draw_arrow(ax, 0.72, 0.76, 0.72, 0.72)
    draw_arrow(ax, 0.72, 0.64, 0.72, 0.57, label="Yes")
    # Loop back on failed auth
    ax.plot([0.76, 0.88, 0.88, 0.85], [0.68, 0.68, 0.795, 0.795], color=COLOR_BORDER, lw=1.2)
    ax.annotate("", xy=(0.85, 0.795), xytext=(0.87, 0.795), arrowprops=dict(arrowstyle="-|>", color=COLOR_BORDER, lw=1.2))
    ax.text(0.90, 0.73, "No", fontsize=8, color="#DC2626", weight="bold")
    
    draw_arrow(ax, 0.72, 0.50, 0.72, 0.43)
    draw_arrow(ax, 0.72, 0.36, 0.72, 0.29)
    draw_arrow(ax, 0.72, 0.22, 0.72, 0.125)
    
    fig.text(0.50, 0.02, "Fig 3.3 Activity Diagram", fontsize=12, weight="bold", ha="center", family=FONT_FAMILY)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "Fig3_3_Activity_Diagram.png"), dpi=300, bbox_inches="tight")
    plt.close()

if __name__ == "__main__":
    print("Generating all 7 academic design diagrams matching reference format...")
    generate_fig1_architecture()
    print("[OK] Fig 1 Architecture generated.")
    generate_dfd_diagrams()
    print("[OK] Fig 2.1 & 2.2 DFD generated.")
    generate_fig2_3_level2_dfd()
    print("[OK] Fig 2.3 Level 2 DFD generated.")
    generate_fig3_1_usecase()
    print("[OK] Fig 3.1 Use Case Diagram generated.")
    generate_fig3_2_class_diagram()
    print("[OK] Fig 3.2 Class Diagram generated.")
    generate_fig3_3_activity_diagram()
    print("[OK] Fig 3.3 Activity Diagram generated.")
    print(f"All figures successfully generated in: {OUTPUT_DIR}")
