from datetime import datetime
from enum import Enum
from pydantic import BaseModel, EmailStr, Field


class AgentType(str, Enum):
    human = "human"
    ai = "ai"


class LeadStatus(str, Enum):
    new = "new"
    attempted = "attempted"
    connected = "connected"
    converted = "converted"
    rejected = "rejected"
    follow_up = "follow_up"


class LoginRequest(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)


class LeadBase(BaseModel):
    full_name: str
    phone_number: str
    source: str | None = None
    tags: list[str] = Field(default_factory=list)


class LeadCreate(LeadBase):
    assigned_to_type: AgentType
    assigned_to_id: str


class LeadUpdate(BaseModel):
    status: LeadStatus
    comment: str | None = None


class TranscriptEntry(BaseModel):
    call_id: str
    speaker: str
    utterance: str
    timestamp: datetime


class AgentAvailability(BaseModel):
    agent_id: str
    status: str
    active_calls: int
    max_concurrent_calls: int


class DashboardKPI(BaseModel):
    date: datetime
    total_calls: int
    connected_calls: int
    converted_calls: int
    avg_duration_seconds: float
