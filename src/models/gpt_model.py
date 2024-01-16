from pydantic import BaseModel

# Schema for endpoints for MessageGPT methods http
class MessageGPT(BaseModel):
    message: str