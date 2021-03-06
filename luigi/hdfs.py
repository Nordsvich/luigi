# -*- coding: utf-8 -*-
#
# Copyright 2012-2015 Spotify AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""
luigi.hdfs has moved to :py:mod:`luigi.contrib.hdfs`
"""
# Delete this file any time after 28 July 2015

import warnings

from luigi.contrib.hdfs import *  # NOQA

warnings.warn("luigi.hdfs module has been moved to luigi.contrib.hdfs",
              DeprecationWarning)
