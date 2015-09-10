# -*- coding: utf-8 -*-
# Coh-Metrix-Dementia - Automatic text analysis and classification for dementia.
# Copyright (C) 2014  Andre Luiz Verucci da Cunha
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import unicode_literals, print_function, division

from coh.base import (
    Text,
    Category,
    Metric,
    MetricsSet,
    ResultSet,
)

from coh.resource_pool import (
    ResourcePool,
    DefaultResourcePool,
    rp,
)

from coh.metrics import *
from coh.tools import *
from coh.conf import config

all_metrics = MetricsSet([BasicCounts(),
                          LogicOperators(),
                          Frequencies(),
                          Hypernyms(),
                          Tokens(),
                          Connectives(),
                          Ambiguity(),
                          # SyntacticalComplexity(),
                          # SemanticDensity(),
                          Constituents(),
                          Anaphoras(),
                          Coreference(),
                          # Lsa(),
                          # Disfluencies(),
                          ])


rp = DefaultResourcePool()


__all__ = sorted([m for m in locals().keys()
                  if not m.startswith('_')])
