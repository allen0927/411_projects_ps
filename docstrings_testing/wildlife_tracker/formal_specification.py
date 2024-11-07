from typing import Any, List, Optional
from wildlife_tracker.animal_management.animal import Animal
from wildlife_tracker.habitat_management.habitat import Habitat
from wildlife_tracker.migration_tracking.migration import Migration
from wildlife_tracker.migration_tracking.migration_path import MigrationPath

age: Optional[int] = None   #????????????????????
animal_id: int #OK
animals: dict[int, Animal] = {} # OK
animals: List[int] = [] #OK
current_date: str       #MigrationManager
current_location: str   #OK
destination: Habitat    #OK
duration: Optional[int] = None  #OK
environment_type: str   #OK
geographic_area: str    #OK
habitat_id: int #OK
habitats: dict[int, Habitat] = {}   #OK
health_status: Optional[str] = None         #??????????????????????????????
migration_id: int   #OK
migration_path: MigrationPath   #OK
migrations: dict[int, Migration] = {}   #OK
path_id: int    #OK
paths: dict[int, MigrationPath] = {}    #OK
size: int   #OK
species: str    #OK ?????????? one used in animal??
species: str    # OK
start_date: str #OK
start_location: Habitat #OK
status: str = "Scheduled"   #OK

#OK
def assign_animals_to_habitat(animals: List[Animal]) -> None:
    pass
#OK
def assign_animals_to_habitat(habitat_id: int, animals: List[Animal]) -> None:
    pass
#OK
def cancel_migration(migration_id: int) -> None:
    pass
#OK
def create_habitat(habitat_id: int, geographic_area: str, size: int, environment_type: str) -> Habitat:
    pass
#OK
def create_migration_path(species: str, start_location: Habitat, destination: Habitat, duration: Optional[int] = None) -> None:
    pass
#OK
def get_animal_by_id(animal_id: int) -> Optional[Animal]:
    pass
#OK
def get_animal_details(animal_id) -> dict[str, Any]:
    pass
#OK
def get_animals_in_habitat(habitat_id: int) -> List[Animal]:
    pass
#OK
def get_habitat_by_id(habitat_id: int) -> Habitat:
    pass
#OK
def get_habitat_details(habitat_id: int) -> dict:
    pass
#OK
def get_habitats_by_geographic_area(geographic_area: str) -> List[Habitat]:
    pass
#OK
def get_habitats_by_size(size: int) -> List[Habitat]:
    pass
#OK
def get_habitats_by_type(environment_type: str) -> List[Habitat]:
    pass
#OK
def get_migration_by_id(migration_id: int) -> Migration:
    pass
#OK
def get_migration_details(migration_id: int) -> dict[str, Any]:
    pass
#OK
def get_migration_path_by_id(path_id: int) -> MigrationPath:
    pass
#OK
def get_migration_paths() -> list[MigrationPath]:
    pass
#OK
def get_migration_paths_by_destination(destination: Habitat) -> list[MigrationPath]:
    pass
#OK
def get_migration_paths_by_species(species: str) -> list[MigrationPath]:
    pass
#OK
def get_migration_paths_by_start_location(start_location: Habitat) -> list[MigrationPath]:
    pass
#OK
def get_migrations() -> list[Migration]:
    pass
#OK
def get_migrations_by_current_location(current_location: str) -> list[Migration]:
    pass
#OK
def get_migrations_by_migration_path(migration_path_id: int) -> list[Migration]:
    pass
#OK
def get_migrations_by_start_date(start_date: str) -> list[Migration]:
    pass
#OK
def get_migrations_by_status(status: str) -> list[Migration]:
    pass
#OK
def get_migration_path_details(path_id) -> dict:
    passf
#OK
def register_animal(animal: Animal) -> None:
    pass
#OK
def remove_animal(animal_id: int) -> None:
    pass
#OK
def remove_habitat(habitat_id: int) -> None:
    pass
#OK
def remove_migration_path(path_id: int) -> None:
    pass
#OK
def schedule_migration(migration_path: MigrationPath) -> None:
    pass
#OK
def update_animal_details(animal_id: int, **kwargs: Any) -> None:
    pass
#OK
def update_habitat_details(habitat_id: int, **kwargs: dict[str, Any]) -> None:
    pass
#OK
def update_migration_details(migration_id: int, **kwargs: Any) -> None:
    pass
#OK
def update_migration_path_details(path_id: int, **kwargs) -> None:
    pass