from abc import abstractmethod


class BaseAdapter:
    """
    Abstraction of the Port. Here all the operations must be declared but NOT implemented.
    """

    @abstractmethod
    def get_all(self):
        """
        Retrieve all the items
        """
        raise NotImplementedError()

    @abstractmethod
    def get_by_field(self, field, value):
        """
        Retrieve that matches the field and value
        """
        raise NotImplementedError()

    @abstractmethod
    def get_by_partition_key(self, value):
        """
        Retrieve that matches the field and value
        """
        raise NotImplementedError()

    @abstractmethod
    def get_by_id(self, item_id):
        """
        Retrieve all the items
        """
        raise NotImplementedError()

    @abstractmethod
    def delete(self, item_id: int):
        """
        Soft delete/update an entity
        """
        raise NotImplementedError()

    @abstractmethod
    def update(self, updated_item):
        """
        Update an entity.
        """
        raise NotImplementedError()

    @abstractmethod
    def create(self, new_item):
        """
        Create an entity.
        """
        raise NotImplementedError()

    @abstractmethod
    def exist(self, item_id: int):
        """
        Validates an entity.
        """
        raise NotImplementedError()
