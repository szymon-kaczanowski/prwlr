# -*- coding: utf-8 -*-


from weakref import WeakKeyDictionary
from errors import *
import numpy as np
import pandas as pd


class Profile(object):
    """
    Profile object.
    """

    def __init__(self,
                 reference,
                 query):
        try:
            iter(reference)
        except TypeError:
            raise ProfileConstructorError("Reference must be an iterable.")
        try:
            iter(query)
        except TypeError:
            raise ProfileConstructorError("Query must be an iterable.")
        if len(reference) < len(query):
            raise ProfileLengthError("Reference longer than query")
        self.reference = tuple(reference)
        self.query = tuple(query)
        self._construct()

    def _construct(self):
        """
        Construct profile from Profile.reference and Profile.query.
        """
        self.profile = [True if i in self.reference else False for i in self.query]

    def _convert(self,
                 positive_sign,
                 negative_sign):
        """
        Convert profile to given sign.
        """
        return [positive_sign if True else negative_sign for i in self.profile]

    def to_string(self,
                  positive_sign="+",
                  negative_sign="-"):
        """
        Return profile as str.
        """
        return "".join(self._convert(positive_sign,
                                     negative_sign))

    def to_list(self,
                positive_sign="+",
                negative_sign="-"):
        """
        Retrun profile as list.
        """
        return list(self._convert(positive_sign,
                                  negative_sign))

    def to_tuple(self,
                 positive_sign="+",
                 negative_sign="-"):
        """
        Return profile as tuple.
        """
        return tuple(self._convert(positive_sign,
                                   negative_sign))

    def to_array(self,
                 positive_sign="+",
                 negative_sign="-"):
        """
        Return profile as an numpy.array.
        """
        return np.array(self._convert(positive_sign,
                                      negative_sign))

    def to_series(self,
                  positive_sign="+",
                  negative_sign="-"):
        """
        Return profile as pandas.Series
        """
        return pd.Series(self._convert(positive_sign,
                                       negative_sign))
