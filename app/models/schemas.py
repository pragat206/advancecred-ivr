from datetime import datetime
from enum import Enum
<<<<<<< HEAD

=======
>>>>>>> origin/main
from pydantic import BaseModel, EmailStr, Field


class AgentType(str, Enum):
    human = "human"
    ai = "ai"


<<<<<<< HEAD
class RoleType(str, Enum):
    admin = "admin"
    human_agent = "human_agent"
    ai_agent = "ai_agent"


=======
>>>>>>> origin/main
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


<<<<<<< HEAD
class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    role: RoleType
    tenant_id: int


=======
>>>>>>> origin/main
class LeadBase(BaseModel):
    full_name: str
    phone_number: str
    source: str | None = None
    tags: list[str] = Field(default_factory=list)


class LeadCreate(LeadBase):
    assigned_to_type: AgentType
<<<<<<< HEAD
    assigned_to_id: int


class LeadRead(LeadBase):
    id: int
    status: LeadStatus
    comment: str | None = None
=======
    assigned_to_id: str
>>>>>>> origin/main


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
