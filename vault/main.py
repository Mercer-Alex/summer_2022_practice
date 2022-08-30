def steal(vault_val, vaults):
    if vaults < 0:
        return 0
    if vaults == 0:
        return vault_val[0]

    pick = vault_val[vaults] + steal(vault_val, vaults - 2)
    not_pick = steal(vault_val, vaults - 1)

    return max(pick, not_pick)


values = [6, 7, 1, 3, 8, 2, 4]
print(steal(values, len(values) - 1))
