import random

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1  # compteur auto-incrémenté pour les IDs
        
        # Les 3 membres initiaux de la famille Jackson
        self._members = [
            self._make_member("John", 33, [7, 13, 22]),
            self._make_member("Jane", 35, [10, 14, 3]),
            self._make_member("Jimmy", 5, [1]),
        ]

    def _generate_id(self):
        """Génère un ID unique auto-incrémenté"""
        new_id = self._next_id
        self._next_id += 1
        return new_id

    def _make_member(self, first_name, age, lucky_numbers):
        """Helper pour créer un membre avec le bon format"""
        return {
            "id": self._generate_id(),
            "first_name": first_name,
            "last_name": self.last_name,
            "age": age,
            "lucky_numbers": lucky_numbers
        }

    def add_member(self, member):
        """Ajoute un membre. Si pas d'ID fourni, on en génère un."""
        if "id" not in member or member["id"] is None:
            member["id"] = self._generate_id()
        self._members.append(member)
        return member

    def delete_member(self, id):
        """Supprime un membre par son ID. Retourne True si trouvé, False sinon."""
        for i, member in enumerate(self._members):
            if member["id"] == id:
                self._members.pop(i)
                return True
        return False

    def get_member(self, id):
        """Retourne un membre par son ID, ou None si pas trouvé."""
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    def get_all_members(self):
        """Retourne tous les membres."""
        return self._members