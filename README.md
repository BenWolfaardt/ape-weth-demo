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

## TODOs

- [ ] As an exercise, see if you can make use of the approve and transferFrom
- [ ] Great! We're off to the races. Try your hand at writing a couple tests of your own using the available contract methods
- [ ] Improve Ruff

## Links

- [User Guide - CLIs](https://docs.apeworx.io/ape/stable/userguides/clis.html?ref=snakecharmers.ethereum.org)

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
