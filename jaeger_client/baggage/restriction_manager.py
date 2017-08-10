# Copyright (c) 2017 Uber Technologies, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from .restriction import Restriction

DEFAULT_MAX_VALUE_LENGTH = 2048


class BaggageRestrictionManager(object):
    """
    BaggageRestrictionManager manages baggage restrictions for baggage keys.
    The manager will return a Restriction for a specific baggage key which
    will determine whether the baggage key is allowed for the current service
    and any other applicable restrictions on the baggage value.
    """

    def get_restriction(self, service, baggage_key):
        raise NotImplementedError()


class DefaultBaggageRestrictionManager(BaggageRestrictionManager):
    """
    DefaultBaggageRestrictionManager allows any baggage key.
    """
    def __init__(self, max_value_length=DEFAULT_MAX_VALUE_LENGTH):
        self._restriction = Restriction(key_allowed=True, max_value_length=max_value_length)

    def get_restriction(self, service, baggage_key):
        return self._restriction
