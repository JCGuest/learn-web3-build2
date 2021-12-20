from brownie import network, EIP20, accounts, config


def deploy():
    account = get_account()
    eip20 = EIP20.deploy({"from": account})

    eip20(100000000, "HUGO", 1000, "HGO")

    print(f"deployed: {eip20}")


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy()
