from ftmscan.enums.actions_enum import ActionsEnum as actions
from ftmscan.enums.fields_enum import FieldsEnum as fields
from ftmscan.enums.modules_enum import ModulesEnum as modules


class Stats:
    @staticmethod
    def get_total_ftm_supply() -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.ETH_SUPPLY}"
        )
        return url

    @staticmethod
    def get_ftm_last_price() -> str:
        url = (
            f"{fields.MODULE}"
            f"{modules.STATS}"
            f"{fields.ACTION}"
            f"{actions.ETH_PRICE}"
        )
        return url
