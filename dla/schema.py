from typing import List

from pydantic import BaseModel, Field, UUID1

class FileStructure(BaseModel): 
    bbox: List[int]


class FileFormat(BaseModel): 
    id: UUID1
    filename: str
    format: str
    structure: FileStructure

