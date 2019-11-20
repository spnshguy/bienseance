# coding: utf-8

"""
Copyright 2017 Square, Inc.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


from pprint import pformat
from six import iteritems
import re


class OrderLineItemModifier(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, catalog_object_id=None, name=None, base_price_money=None, total_price_money=None):
        """
        OrderLineItemModifier - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'catalog_object_id': 'str',
            'name': 'str',
            'base_price_money': 'Money',
            'total_price_money': 'Money'
        }

        self.attribute_map = {
            'catalog_object_id': 'catalog_object_id',
            'name': 'name',
            'base_price_money': 'base_price_money',
            'total_price_money': 'total_price_money'
        }

        self._catalog_object_id = catalog_object_id
        self._name = name
        self._base_price_money = base_price_money
        self._total_price_money = total_price_money

    @property
    def catalog_object_id(self):
        """
        Gets the catalog_object_id of this OrderLineItemModifier.
        The catalog object id referencing [CatalogModifier](#type-catalogmodifier).

        :return: The catalog_object_id of this OrderLineItemModifier.
        :rtype: str
        """
        return self._catalog_object_id

    @catalog_object_id.setter
    def catalog_object_id(self, catalog_object_id):
        """
        Sets the catalog_object_id of this OrderLineItemModifier.
        The catalog object id referencing [CatalogModifier](#type-catalogmodifier).

        :param catalog_object_id: The catalog_object_id of this OrderLineItemModifier.
        :type: str
        """

        if catalog_object_id is None:
            raise ValueError("Invalid value for `catalog_object_id`, must not be `None`")
        if len(catalog_object_id) > 192:
            raise ValueError("Invalid value for `catalog_object_id`, length must be less than `192`")

        self._catalog_object_id = catalog_object_id

    @property
    def name(self):
        """
        Gets the name of this OrderLineItemModifier.
        The name of the item modifier.

        :return: The name of this OrderLineItemModifier.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OrderLineItemModifier.
        The name of the item modifier.

        :param name: The name of this OrderLineItemModifier.
        :type: str
        """

        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than `255`")

        self._name = name

    @property
    def base_price_money(self):
        """
        Gets the base_price_money of this OrderLineItemModifier.
        The base price for the modifier.  `base_price_money` is required for ad hoc modifiers. If both `catalog_object_id` and `base_price_money` are set, `base_price_money` will override the predefined [CatalogModifier](#type-catalogmodifier) price.

        :return: The base_price_money of this OrderLineItemModifier.
        :rtype: Money
        """
        return self._base_price_money

    @base_price_money.setter
    def base_price_money(self, base_price_money):
        """
        Sets the base_price_money of this OrderLineItemModifier.
        The base price for the modifier.  `base_price_money` is required for ad hoc modifiers. If both `catalog_object_id` and `base_price_money` are set, `base_price_money` will override the predefined [CatalogModifier](#type-catalogmodifier) price.

        :param base_price_money: The base_price_money of this OrderLineItemModifier.
        :type: Money
        """

        self._base_price_money = base_price_money

    @property
    def total_price_money(self):
        """
        Gets the total_price_money of this OrderLineItemModifier.
        The total price of the item modifier for its line item. This is the modifier's base_price_money multiplied by the line item's quantity.

        :return: The total_price_money of this OrderLineItemModifier.
        :rtype: Money
        """
        return self._total_price_money

    @total_price_money.setter
    def total_price_money(self, total_price_money):
        """
        Sets the total_price_money of this OrderLineItemModifier.
        The total price of the item modifier for its line item. This is the modifier's base_price_money multiplied by the line item's quantity.

        :param total_price_money: The total_price_money of this OrderLineItemModifier.
        :type: Money
        """

        self._total_price_money = total_price_money

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
