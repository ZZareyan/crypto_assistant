const EXCHANGES = [
  {
    name: "Coinbase",
    bestFor: "Absolute beginners",
    fiatOnRamp: true,
    kyc: true,
    note: "Simplest UI, highest fees",
  },
  {
    name: "Kraken",
    bestFor: "Intermediate users",
    fiatOnRamp: true,
    kyc: true,
    note: "Low fees, strong security record",
  },
  {
    name: "Binance",
    bestFor: "All levels",
    fiatOnRamp: true,
    kyc: true,
    note: "Largest coin selection",
  },
  {
    name: "Uniswap",
    bestFor: "DeFi / no KYC",
    fiatOnRamp: false,
    kyc: false,
    note: "DEX — non-custodial, crypto only",
  },
];

export function ExchangeComparison() {
  return (
    <div className="overflow-x-auto">
      <table className="w-full text-sm">
        <thead>
          <tr className="border-b text-left text-gray-500">
            <th className="py-2 pr-4">Exchange</th>
            <th className="py-2 pr-4">Best for</th>
            <th className="py-2 pr-4 text-center">Fiat on-ramp</th>
            <th className="py-2 pr-4 text-center">KYC required</th>
            <th className="py-2">Note</th>
          </tr>
        </thead>
        <tbody>
          {EXCHANGES.map((ex) => (
            <tr key={ex.name} className="border-b">
              <td className="py-3 pr-4 font-medium">{ex.name}</td>
              <td className="py-3 pr-4 text-gray-600">{ex.bestFor}</td>
              <td className="py-3 pr-4 text-center">{ex.fiatOnRamp ? "✓" : "—"}</td>
              <td className="py-3 pr-4 text-center">{ex.kyc ? "✓" : "—"}</td>
              <td className="py-3 text-gray-500">{ex.note}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
