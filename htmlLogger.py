"""
    HTML Logger allows to log all remarks into HTML
"""
__author__ = 'maxim.shcherbakov'

import pandas as pd

class htmlLogger():
    """
    Attributes
    ----------
    file_name : String
        Name of the file for logging

    file_pointer : pointer
        Pointer to open file

    """
    file_name = ''
    file_pointer = None

    def __init__(self, name):
        """
        Create the pointer to file

        :param
        name : String
            File name of logger.

        """
        self.name = name
        try:
            self.file_pointer = open(self.name, 'w')
            self.file_pointer.write('<html>')
        except:
            print("Error occurs in attempt of file open")

    def __del__(self):
        self.file_pointer.write('</html>')
        self.file_pointer.close()

    def appendImage(self, _image_name, _image_file):
        """
        Append image into log file

        :param
        _image_name : String
            Name of the image

        :param
        _image_file : String
            Path and filename of image stored on the disk

        :return:
        """
        self.file_pointer.write("<img src=\"" + _image_file + "\" alt=\"" + _image_name + "\">")

    def appendParagraph(self, _message):
        self.file_pointer.write("<p>" + _message + "</p>")

    def appendDataFrame(self, dataframe_):
        self.file_pointer.write(dataframe_.to_html())

    def append_list_of_paragraphs(self, paragraphs_list_):
        for paragraph in paragraphs_list_:
            self.appendParagraph(paragraph)
