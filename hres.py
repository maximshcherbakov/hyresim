"""
    HRES - Hybrid renewable system class
"""
__author__ = 'maxim.shcherbakov'


class HRES:
    """
    Parameters
    ----------
    components_list_ : list
        List of HRES components or instances Component class

    location : list [lat, lon]
        List of longitude and latitude pf HRES position

    Attributes
    ----------
    components : list
        List of HRES components or instances Component class

    """
    location = None
    components = []

    def __init__(self, components_list_, location_):
        """
            Create HRES

        :param
        components_list_: list
            List of components, e.g. instances of Component class (and their childs)

        :param location_:
        :return:
        """
        print('Creating the HRES using list of components')
        self.components = components_list_
        self.location = location_

    def get_components(self):
        """
            Return the list of comonents
        :return:
            self.components a list of components
        """
        return self.components

    def print_components_list(self):
        """
            Print a list of components.
            Need to be omitted in the next version
        :return:
        """
        print('HRES contains on Components:')
        for i, component in enumerate(self.components):
            print("\n", component.get_name())

    @property
    def get_description(self):
        """
            Get a list of description of the HRES
        :return:
        """
        description = ["HRES contains the following components"]
        for i, component in enumerate(self.components):
            description.append(component.get_name())
        return description

    def get_components_names(self):
        """
            Return a list of components' name
        :return:
            names : list of N items, where N is the length of self.components
        """
        names = []
        for i, component in enumerate(self.components):
            names.append(component.get_name())
        return names

    def get_components_count(self):
        """
            Return counts of components
        :return:
            N : integer, where N is the length of self.components
        """
        return len(self.components)

    def get_state_of_component_by_name(self, name_):
        """
            Return the current state of component by its name
        :param name_: (string) a name of components of HRES
        :return:
            state parameter of component
        """
        current_state = None
        for i, component in enumerate(self.components):
            if component.name == name_:
                current_state = component.get_state()
        return current_state

    def get_component_by_name(self, name_):
        """
            Return component (an instance of Component class) by it's name. If component did not found, returns None
        :param name_: (string) the search component name
        :return:
            search_component (an instance of Component class) found component
        """
        search_component = None
        for i, component in enumerate(self.components):
            if component.name == name_:
                search_component = component
        return search_component

    def get_consumption(self, current_datetime):
        """
            Return total consumption over all consumption components
        :param current_datetime:
        :return:
        """
        total_consumption = 0
        for i, component in enumerate(self.components):
            if component.__class__.__name__ == "Consumer":
                # print("get consumer!")
                total_consumption = total_consumption + component.get_state(current_datetime)
        return total_consumption

    def get_production(self, current_datetime):
        """
            Return total production by PV at current datetime

        :type current_datetime: object
        :param current_datetime: current datetime
        :return: total_production (float): total production by PV at current datetime

        """
        total_production = 0
        for i, component in enumerate(self.components):
            if component.__class__.__name__ == "SolarPanel":
                # print("get consumer!")
                total_production = total_production + component.state
        return total_production
