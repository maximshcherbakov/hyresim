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
        return self.components

    def print_components_list(self):
        print('HRES contains on Components:')
        for i, component in enumerate(self.components):
            print("\n", component.get_name())

    def get_components_names(self):
        names = []
        for i, component in enumerate(self.components):
            names.append(component.get_name())
        return names

    def get_components_count(self):
        return len(self.components)
