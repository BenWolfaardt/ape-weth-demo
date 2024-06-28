# [An Introduction to the Ape Framework](https://snakecharmers.ethereum.org/intro-to-ape/)

1. `ape init`
2. `ape compile` -> compile smart contracts to get ABI
3. `ape plugins install .`  # after adding the solidity plugin to `ape-config.yaml`
4. Can only compile Solidity after compiler plugin has been installed.
5. `ape plugins list -a`  # https://docs.apeworx.io/
6. `ape console`
7. `ape networks list`  # https://docs.apeworx.io/ape/stable/userguides/networks.html?ref=snakecharmers.ethereum.org
8. `ape test`
9. `ape run deploy`  # default to local eth-tester environment
10. `ape run deploy --network ethereum:mainnet:geth`  
  10.1 You can specify another chain/provider.  
  10.2 You can only specify something from: `ape networks list`

## Test out the Waters

```python
from ape import networks
from ape.managers.networks import NetworkManager
from ape.api.providers import ProviderAPI
from typing import cast

networks: NetworkManager = networks
alchemy = cast(ProviderAPI, networks.provider)

print(alchemy.is_connected)
```

## TODOs

- [ ] As an exercise, see if you can make use of the approve and transferFrom
- [ ] Great! We're off to the races. Try your hand at writing a couple tests of your own using the available contract methods
- [ ] Improve Ruff

## Links

- [User Guide - CLIs](https://docs.apeworx.io/ape/stable/userguides/clis.html?ref=snakecharmers.ethereum.org)
- [Uniswap V2 - Contract walk-through](https://ethereum.org/en/developers/tutorials/uniswap-v2-annotated-code/)

## Notes

Notes on various things to remembere

### `pytest`

> Prior to running your tests be sure to have run `ape plugins install .` (for `Solidity`) and `ape compile` to generate your `ABI`s

While you're writing and running tests, know that pytest's normal flags are available to you. Here are a few that you might find useful:

- Run tests that match a pattern, e.g., includes 'deposit':  
`$ ape test -k deposit`
- increase the verbosity level to see more info/print statements:  
`$ ape test -s`
- exit as soon as one failure occurs:  
`$ ape test -x`
- upon failure, open an interactive REPL for debugging:  
`$ ape test --pdb`
- multiple flags may be used:  
`$ ape test --pdb -x -s -k depos`it

### `ape-eth` Install

When installing `ape-eth` if you chose to add the `"reccomended-plugings"` as extra arguments in `pyproject.yaml` note that the following will be included:

- ape-alchemy (0.8.0)
- ape-ens (0.8.0)
- ape-etherscan (0.8.0)
- ape-foundry (0.8.0)
- ape-hardhat (0.8.0)
- ape-infura (0.8.0)
- ape-solidity (0.8.2)
- ape-template (0.8.0)
- ape-tokens (0.8.0)
- ape-vyper (0.8.1)

### Setting up `Hardhat`

> Note: Ape generates a config in `$HOME/.ape/hardhat` to avoid configs but can use a local `ape-config.yaml` if configured.

- See [documentation](https://github.com/ApeWorX/ape-hardhat)
- Add to the `ape-config.yaml`
- Install with: `npm install --save-dev hardhat`
  - It was necessary to install globally to be able to find the `hardhat` binary
  - `npm install -g hardhat` confirming it is installed with: `hardhat --version`
- Now you can use the `--network ethereum:local:hardhat` with the `Ape CLI`
- Use `ape networks list` to see available networks
- `ape accounts generate <account_name> --word-count 24` saves encrypted file to `$HOME/.ape/accounts`
  - `SUCCESS: A new account '0xe3f7A408a64E147e120f79Daa2973D890Cd9d830' with HDPath m/44'/60'/0'/0/0 has been added with the id 'test'`

> You can now deploy a contract: `ape run deploy --network ethereum:sepolia:alchemy`. Ensuring that you have funds in your account for the relavent network.
