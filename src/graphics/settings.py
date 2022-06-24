import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


class Settings:

    def __init__(self):
        """
        https://matplotlib.org/stable/tutorials/introductory/customizing.html
        https://seaborn.pydata.org/tutorial/aesthetics.html

        """

    @staticmethod
    def aesthetics():
        """
        :return:
        """

        matplotlib.rcParams.update({'font.size': 13})
        matplotlib.rcParams['text.usetex'] = False

        plt.style.use('seaborn-white')

        sns.set(font_scale=1.25)

    @staticmethod
    def layout():
        """
        :return:
        """

        plt.rcParams['figure.constrained_layout.use'] = False