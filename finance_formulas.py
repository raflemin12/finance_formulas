

def accounting_equation(assets:float, liabilities:float, shareholder_equity:float) -> bool:
    """Assets = Libabilities + Shareholders Equity
    Returns true when accounting equation is balanced
    Returns the difference when accounting equation is not balanced
    """
    balanced = assets == liabilities + shareholder_equity

    if not balanced:
        return assets - liabilities - shareholder_equity
    return balanced

def current_ratio(current_assets: float, current_liabilities:float) -> float:
    """
    Calculates if company can pay its current bills.
    In general, above 1.5 is safe and below 1.5 is risky
    """
    return current_assets / current_liabilities

def debt_ratio(total_liabilities: float, total_assets: float) -> float:
    """
    Amount of assets that go into paying debts.
    In general, bigger ratio is considered riskier.
    """
    return total_liabilities / total_assets

def equity_ratio(total_shareholder_equity: float, total_assets: float, intangible_assets = 0) -> float:
    """
    Amount of assets that go to shareholders.
    In general, want it to be higher than debt ratio
    """
    return total_shareholder_equity / (total_assets - intangible_assets)

def acid_test_ratio(cash: float, short_investments: float, net_acc_receive: float, current_liabilities: float) -> float:
    """
    Most liquid assets that go into paying debts.
    In general, looking for 0.9 - 1.o
    """
    return (cash + short_investments + net_acc_receive) / current_liabilities

def inventory_turnover(cogs: float, avg_inventory: float) -> float:
    """
    The number of times sold through your inventory.
    The higher the better.
    """
    return cogs / avg_inventory

def days_sales_inventory(inventory_turn: float) -> float:
    """
    Average number of days it takes to sell off inventory. Measures efficiency of sales.
    Lower is better.
    """
    return 365 / inventory_turn
