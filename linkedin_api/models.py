from pydantic import BaseModel, Field
from typing import Generic, List, Optional, TypeVar, Union


# Define a type variable for the generic data type
T = TypeVar("T")


# Define a base response model
class Response(BaseModel, Generic[T]):
    data: Union[T, None] = None
    error: Union[str, None] = None

    @classmethod
    def success(cls, data: T):
        return cls(data=data, error=None)

    @classmethod
    def failure(cls, error: str):
        return cls(data=None, error=error)


class GetProfileParams(BaseModel):
    # public_id: Optional[str] = Field(
    #     default=None,
    #     description="The public identifier for the LinkedIn user, used for accessing public profiles.",
    # )
    urn_id: Optional[str] = Field(
        default=None,
        description="The LinkedIn Uniform Resource Name (URN) identifier for the user, used for more specific queries within LinkedIn's system.",
    )


class Profile(BaseModel):
    urn_id: str = Field(
        description="The unique identifier for the profile, derived from the LinkedIn URN."
    )
    profile_id: Optional[str] = Field(
        default=None, description="Clean numeric ID extracted from the URN."
    )
    profile_urn: Optional[str] = Field(
        default=None, description="Full URN of the LinkedIn profile."
    )
    member_urn: Optional[str] = Field(
        default=None,
        description="URN that uniquely identifies the LinkedIn member.",
    )
    public_id: Optional[str] = Field(
        default=None, description="Public identifier used in the profile's URL."
    )
    headline: Optional[str] = Field(
        default=None, description="Professional headline of the user."
    )
    summary: Optional[str] = Field(
        default=None,
        description="Summary of the user's professional background.",
    )
    industryName: Optional[str] = Field(
        default=None, description="Industry in which the user operates."
    )
    locationName: Optional[str] = Field(
        default=None, description="User's reported location."
    )
    experience: List[dict] = Field(
        default_factory=list,
        description="List of work experiences associated with the profile.",
    )
    education: List[dict] = Field(
        default_factory=list,
        description="List of educational background entries.",
    )
    languages: List[dict] = Field(
        default_factory=list,
        description="List of languages known by the profile owner.",
    )
    publications: List[dict] = Field(
        default_factory=list,
        description="List of publications credited to the profile owner.",
    )
    certifications: List[dict] = Field(
        default_factory=list,
        description="List of certifications achieved by the profile owner.",
    )
    volunteer: List[dict] = Field(
        default_factory=list, description="List of volunteer experiences."
    )
    honors: List[dict] = Field(
        default_factory=list, description="List of honors received."
    )
    projects: List[dict] = Field(
        default_factory=list, description="List of projects worked on."
    )
    skills: List[dict] = Field(
        default_factory=list,
        description="List of skills possessed by the profile owner.",
    )
