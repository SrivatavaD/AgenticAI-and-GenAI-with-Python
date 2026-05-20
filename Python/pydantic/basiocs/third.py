from pydantic import Optional
from pydantic import BaseModel, Field

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="The employee's full name"
        example="John Doe"
    )
    department: Optional[str] = 'general'
    salary: float = Field(
        ...,
        ge = 10000,
    )        