from typing import Self

import pytest
from lib.lineage.lineage import AbstractLineageTest

from gbserver.lineage.lakehouse_jobstats import LakehouseLineageStore

pytestmark = pytest.mark.ibm


class TestLHJobStatsLineage(AbstractLineageTest):

    def _get_tested_lineage_storage(self: Self):
        return LakehouseLineageStore()
