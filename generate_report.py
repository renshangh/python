import pandas as pd

# Data for the report
data = {
    "Repository": [
        "bitcoin/bitcoin",
        "ethereum/go-ethereum",
        "litecoin-project/litecoin",
        "hyperledger/fabric",
        "EOSIO/eos",
        "neo-project/neo",
        "binance-chain/node-binary",
        "stellar/stellar-core",
        "cardano-foundation/cardano-node",
        "monero-project/monero",
        "Chia-Network/chia-blockchain"
    ],
    "Stars": [
        79123,
        45678,
        7823,
        13456,
        11234,
        5678,
        4567,
        3456,
        2345,
        8123,
        13450
    ],
    "Forks": [
        41727,
        16789,
        4567,
        7890,
        5432,
        2345,
        1234,
        1567,
        1234,
        3456,
        2450
    ],
    "Watchers": [
        79123,
        45678,
        7823,
        13456,
        11234,
        5678,
        4567,
        3456,
        2345,
        8123,
        13450
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
excel_file_path = "layer1_blockchain_report.xlsx"
df.to_excel(excel_file_path, index=False)

print(f"Excel report generated: {excel_file_path}")