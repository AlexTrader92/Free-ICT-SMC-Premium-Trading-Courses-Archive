# Elite Risk Management Calculator
# Brought to you by The Master Vault

def calculate_position_size(account_balance, risk_percentage, stop_loss_pips, pip_value):
    risk_amount = account_balance * (risk_percentage / 100)
    position_size = risk_amount / (stop_loss_pips * pip_value)
    return position_size

print("Welcome to the Elite Risk Calculator")
print("Access 1,000+ Premium Courses at: https://t.me/+v1BOi_dEDqtiYjc1")
