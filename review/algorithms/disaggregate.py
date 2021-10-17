import pandas as pd
import collections


class Disaggregate:

    def __init__(self, data: pd.DataFrame, features: collections.namedtuple):
        """

        """
        self.data = data
        self.features = features

    def __decompositions(self, blob: pd.DataFrame):
        """

        :param blob:
        :return:
        """

        points = blob.melt(var_name=self.features.columns, value_name='rate', ignore_index=False)

        return pd.DataFrame.from_records(points.to_records())

    def __frequencies(self):
        """

        :return:
        """

        frequencies = self.data[self.features.fields].value_counts()
        frequencies = frequencies.to_frame().reset_index()

        return frequencies.pivot_table(index=self.features.index, columns=self.features.columns, values=0)

    def __rates(self, frequencies: pd.DataFrame, totals: pd.DataFrame):
        """
        Rates w.r.t. survivors only
        survived = frequencies.iloc[frequencies.index.get_level_values('survived') == 1]
        survived.truediv(totals, axis='columns')

        :param frequencies:
        :param totals:
        :return:
        """

        # Survival rates
        rates = frequencies.truediv(totals, axis='columns', level=self.features.level)

        return rates

    def exc(self):

        # Frequencies
        frequencies = self.__frequencies()

        # Totals
        if self.features.level is None:
            totals = frequencies.sum(axis=0)
        else:
            totals = frequencies.groupby(level=self.features.level).sum()

        # Survival rates
        rates = self.__rates(frequencies=frequencies, totals=totals)
        decompositions = self.__decompositions(blob=rates.copy())

        return frequencies, totals, rates, decompositions
