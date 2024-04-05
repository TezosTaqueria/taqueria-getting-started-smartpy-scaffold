# Getting Started Scaffold for Taqueria (SmartPy version)

This scaffold is a Taqueria project that provides the following:
1. Pre-installed plugins to get off the ground quickly (@taqueria/plugin-smartpy, @taqueria/plugin-taquito, @taqueria/plugin-flextesa)
2. An example contract called `IncDec.py` in the **contracts/** directory
3. A working Taqueria project configuration

To get started, you may run the following:
- `taq start` - to display this useful introduction
- `taq start sandbox` - to run a local Tezos network sandbox on your computer using Docker.
- `taq compile IncDec.py` - to compile the SmartPy Smart Contract into a Michelson artfact, stored in the **artifacts/** folder.
- `taq test IncDec.py` - to run automated unit tests for the IncDec smart contract.
- `taq deploy IncDec.tz` - to deploy (originate) the smart contract to the local sandbox.

To expand on this scaffold, you may wish to create a new contract from one of our templates using `taq create [contractName].py`.