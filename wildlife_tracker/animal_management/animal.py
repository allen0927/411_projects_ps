from typing import Any, Optional

class Animal:
    def __init__(self, animal_id: int,
                 species: str,
                 current_location: str,
                 health_status: Optional[str] = None, 
                 age: Optional[int] = None) -> None:
        self.animal_id = animal_id
        self.species = species
        self.current_location = current_location
        self.health_status = health_status
        self.age = age
        pass

    def update_animal_details(animal_id: int, **kwargs: Any) -> None:
        pass

    def get_animal_details(animal_id) -> dict[str, Any]:
        pass


