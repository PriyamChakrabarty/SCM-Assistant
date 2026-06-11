from analytics.rebate_engine import (
    find_rebate_eligible_suppliers,
)

from analytics.swl_engine import (
    get_swl_suppliers,
)

from analytics.disruption_engine import (
    active_disruption_suppliers,
)

from analytics.spend_engine import (
    calculate_regional_spend,
)

from analytics.defect_engine import (
    highest_average_defect_category,
)

from backend.config import DATA_FILE


class SupplierAnalyticsService:

    @staticmethod
    def rebate_suppliers():

        result = find_rebate_eligible_suppliers(
            DATA_FILE
        )

        return result.to_dict(
            orient="records"
        )

    @staticmethod
    def swl_suppliers():

        result = get_swl_suppliers(
            DATA_FILE
        )

        return result.to_dict(
            orient="records"
        )

    @staticmethod
    def disruption_suppliers():

        result = active_disruption_suppliers(
            DATA_FILE
        )

        return result.to_dict(
            orient="records"
        )

    @staticmethod
    def regional_spend():

        result = calculate_regional_spend(
            DATA_FILE
        )

        return result.to_dict(
            orient="records"
        )

    @staticmethod
    def defect_category():

        result = highest_average_defect_category(
            DATA_FILE
        )

        return result.to_dict(
            orient="records"
        )