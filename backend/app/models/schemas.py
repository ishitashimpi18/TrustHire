from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class AnalyzeRequest(BaseModel):
    url: Optional[str] = None
    text: Optional[str] = None
    company_name: Optional[str] = None
    recruiter_email: Optional[str] = None
    salary: Optional[str] = None

class SHAPExplanationItem(BaseModel):
    term: str
    impact: float
    direction: str  # 'SCAM' or 'GENUINE'

class NetworkNode(BaseModel):
    id: str
    label: str
    type: str  # 'email', 'phone', 'domain', 'company', 'upi'
    risk: Optional[str] = "unknown"

class NetworkEdge(BaseModel):
    source: str
    target: str
    weight: int = 1

class NetworkGraphResponse(BaseModel):
    entity: str
    nodes: List[NetworkNode]
    edges: List[NetworkEdge]
    warnings: List[str]

class AnalyzeResponse(BaseModel):
    fraud_score: float = Field(..., ge=0.0, le=100.0, description="Risk Score from 0 to 100")
    risk_level: str = Field(..., description="LOW, MEDIUM, or HIGH")
    is_hard_veto: bool = False
    veto_reason: Optional[str] = None
    factors: List[str] = []
    ml_explanation: List[SHAPExplanationItem] = []
    duplicate_risk: float = 0.0
    duplicate_matched_title: Optional[str] = None
    network_warnings: List[str] = []
    recruiter_trust_score: Optional[int] = None
    extracted_text: Optional[str] = None

class ReportRequest(BaseModel):
    job_url: Optional[str] = None
    recruiter_email: Optional[str] = None
    phone_number: Optional[str] = None
    company_name: Optional[str] = None
    reason: str
    description: Optional[str] = None

class RecruiterCheckResponse(BaseModel):
    recruiter_identifier: str
    company_name: Optional[str] = None
    trust_score: int
    postings_analyzed: int
    reports_against: int
    status: str
