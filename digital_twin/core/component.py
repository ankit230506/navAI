from abc import ABC, abstractmethod

from datetime import datetime


class Component(ABC):
    """
    Base class for every Digital Twin component.
    """

    def __init__(
        self,
        component_id: str,
        name: str,
        health: float = 100.0
    ):

        self.component_id = component_id
        self.name = name

        self.health = health

        self.age = 0

        self.status = "Healthy"

        self.last_maintenance = datetime.now()

    def degrade(self, rate: float):

        """
        Reduce component health.
        """

        self.health -= rate

        if self.health < 0:
            self.health = 0

    def repair(self):

        """
        Restore component health.
        """

        self.health = 100

        self.status = "Healthy"

        self.last_maintenance = datetime.now()

    def calculate_health(self):

        """
        Update component status based on health.
        """

        if self.health > 90:
            self.status = "Healthy"

        elif self.health > 70:
            self.status = "Monitor"

        elif self.health > 40:
            self.status = "Warning"

        else:
            self.status = "Critical"

    @abstractmethod
    def update(self):
        """
        Every component must implement its own update().
        """
        pass

    def get_state(self):

        return {

            "id": self.component_id,

            "name": self.name,

            "health": round(self.health, 2),

            "status": self.status,

            "age": self.age

        }